from django.shortcuts import render, get_object_or_404, redirect
from products_app.models import ProductCategory, IndividualProduct
from products_app.forms import AddProductForm
from cart_app.models import Cart, CartAmount
from q_and_a_app.models import Question
from q_and_a_app.forms import QuestionForm
from django.http import JsonResponse
from django.db.models import Avg
from rating_app.models import Rating
from review_app.forms import ReviewForm
from review_app.models import ReviewModel
from profile_app.signals import object_viewed_signals
from django.http import HttpResponse
from wish_app.models import Wish
from profile_app.models import ObjectViewed
from rec_engine_app.models import UserPreference
import random

def featured_view(request):
    wish_obj = []
    if request.user.is_authenticated():
        instance = Wish.objects.filter(user=request.user)
        for x in instance:
            wish_obj.append(x.products)
    cart_obj, new_cart = Cart.objects.new_or_get(request)
    cat = ProductCategory.objects.all()
    featured_products = IndividualProduct.objects.filter(featured=True)
    word = 'Our Featured Products'
    context = {
        'cat': cat,
        'products': featured_products,
        'word': word,
        'cart': cart_obj,
        'wish': wish_obj,
    }
    # return HttpResponse('Hello World')
    return render(request, 'products/product-group.html',context)
    

def best_selling_view(request):
    wish_obj = []
    if request.user.is_authenticated():
        instance = Wish.objects.filter(user=request.user)
        for x in instance:
            wish_obj.append(x.products)
    cart_obj, new_cart = Cart.objects.new_or_get(request)
    cat = ProductCategory.objects.all()
    best_selling_products = IndividualProduct.objects.filter(best_selling=True)
    word = 'Our Best Selling Products'
    context = {
        'cat': cat,
        'products': best_selling_products,
        'word': word,
        'cart': cart_obj,
        'wish': wish_obj,
    }
    return render(request, 'products/product-group.html',context)

def latest_view(request):
    wish_obj = []
    if request.user.is_authenticated():
        instance = Wish.objects.filter(user=request.user)
        for x in instance:
            wish_obj.append(x.products)
    cart_obj, new_cart = Cart.objects.new_or_get(request)
    cat = ProductCategory.objects.all()
    latest_products = IndividualProduct.objects.all().order_by('-timestamp')[:20]
    word = 'Our Latest Products'
    context = {
        'cat': cat,
        'products': latest_products,
        'word': word,
        'cart': cart_obj,
        'wish': wish_obj,
    }
    return render(request, 'products/product-group.html',context)


def all_products_in_a_category_view(request, pk):
    wish_obj = []
    if request.user.is_authenticated():
        instance = Wish.objects.filter(user=request.user)
        for x in instance:
            wish_obj.append(x.products)
    cart_obj, new_cart = Cart.objects.new_or_get(request)
    cat = ProductCategory.objects.all()
    qs = IndividualProduct.objects.filter(product_category=pk)
    context ={
        'products': qs,
        'cat': cat,
        'cat_name': ProductCategory.objects.get(id=pk).title,
        'cart': cart_obj,
        'wish': wish_obj,
    }
    return render(request, 'products/all_products_in_a_category.html', context)

def individual_product_detail_view(request, pk):

    # This is this rec section
    recommendation = []
    if request.user.is_authenticated() and ObjectViewed.objects.filter(user=request.user).count() > 0:
        if UserPreference.objects.filter(user=request.user).count() > 0:
            prefer_type_id = UserPreference.objects.get(user=request.user).prefer_type
            cat_id = ProductCategory.objects.get(id=prefer_type_id)
            recommendation_list = IndividualProduct.objects.filter(product_category=cat_id)
            current_page_item = IndividualProduct.objects.get(id=pk)
            temp_choice = random.choices(recommendation_list)
            while temp_choice[0] == current_page_item:
                temp_choice = random.choices(recommendation_list)
            recommendation = temp_choice


    cat = ProductCategory.objects.all()
    request.session['individualdetail_id']=pk
    # For getting product instance
    qs = get_object_or_404(IndividualProduct, id=pk)
    
    # getting avg rating of that product from db
    rating_count = Rating.objects.filter(product=qs).count()
    avg_rating = Rating.objects.filter(product=qs).aggregate(Avg('rating'))
    
    
    # for formatting avg_rating value
    if rating_count > 0:
        floor_avg = int(avg_rating['rating__avg'])
        diff_avg = avg_rating['rating__avg'] - floor_avg
        if diff_avg == 0:
            new_avg = int(avg_rating['rating__avg'])
        else:
            new_avg = avg_rating['rating__avg']
    else:
        new_avg = 0

    cart_obj, new_obj = Cart.objects.new_or_get(request)
    wish = []
    if request.user.is_authenticated():
        wish_obj = Wish.objects.filter(user=request.user)
        if wish_obj.count() > 0:
            wish = [x.products for x in wish_obj] 
    # print('oi',wish)
    form = QuestionForm(request.POST or None)
    review_form = ReviewForm(request.POST or None)
    ques = Question.objects.filter(product=qs).order_by('-updated')[:10]
    reviews = ReviewModel.objects.filter(product=qs).order_by('-updated')[:10]
    ques_count = Question.objects.filter(product=qs).count()
    reviews_count = ReviewModel.objects.filter(product=qs).count()

    # this is for cart amount
    cart_amount_instance = CartAmount.objects.filter(products=qs, cart=cart_obj)
    cart_amount_count = 1
    if cart_amount_instance.count() > 0:
        for x in cart_amount_instance:
            cart_amount_count = x.amount 

    # this is for question and answer section
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.product = qs
        instance.save()
        ques = Question.objects.filter(product=qs).order_by('-updated')[:10]
        ques_count = Question.objects.filter(product=qs).count()
        info = [{'question':x.question, 
                'user': x.user.get_full_name(),
                'updated': x.updated.date()} for x in ques]
        if request.is_ajax():
            jason_data ={
                'info':info,
                'ques_count':ques_count
            }
            return JsonResponse(jason_data)
        return redirect('products:individual_product_detail', pk=pk)

    # this is for review section
    if review_form.is_valid():
        instance = review_form.save(commit=False)
        instance.user = request.user
        instance.product = qs
        instance.save()
        reviews = ReviewModel.objects.filter(product=qs).order_by('-updated')[:10]
        reviews_count = ReviewModel.objects.filter(product=qs).count()
        info = [{'review':x.review, 
                'user': x.user.get_full_name(),
                'updated': x.updated.date()} for x in reviews]
        if request.is_ajax():
            jason_data ={
                'info':info,
                'reviews_count': reviews_count
            }
            return JsonResponse(jason_data)
        return redirect('products:individual_product_detail', pk=pk)


    context ={
        'obj': qs,
        'cart': cart_obj,
        'wish': wish,
        'form': form,
        'review_form': review_form,
        'ques': ques,
        'reviews':reviews,
        'ques_count':ques_count,
        'reviews_count': reviews_count,
        'avg_rating': new_avg,
        'rating_count': rating_count,
        'cart_amount_count': cart_amount_count,
        'cat': cat,
        'recommendation': recommendation,
    }
    object_viewed_signals.send(sender = qs.__class__, instance=qs, request=request)
    return render(request, 'products/product_detail.html',context)

def product_add(request):
    cat = ProductCategory.objects.all()
    form = AddProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = AddProductForm()
        context ={
        'form': form,
        'cat': cat
        }
        return render(request, 'products/add_product.html', context)
    context ={
        'form': form,
        'cat': cat
    }
    return render(request, 'products/add_product.html', context)


    
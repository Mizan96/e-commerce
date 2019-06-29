from django.shortcuts import render, get_object_or_404
from products_app.models import IndividualProduct
from django.http import JsonResponse
from rating_app.models import Rating
from django.db.models import Avg


def rating_api_view(request):
    if request.user.is_authenticated():
        user = request.user
        product = IndividualProduct.objects.get(id=request.session['individualdetail_id'])
        rating = request.POST.get('rating-option')
        counter = Rating.objects.filter(product=product).count()

        if request.is_ajax():
            qs = Rating.objects.filter(user=user, product=product)
            if qs.count() > 0:
                instance = qs.first()
                instance.rating = rating
                instance.save() 
            else:
                Rating.objects.create(user=user,product=product, rating=rating)
            qs2 = get_object_or_404(IndividualProduct, id=request.session['individualdetail_id'])
            avg_rating = Rating.objects.filter(product=qs2).aggregate(Avg('rating'))
            counter = Rating.objects.filter(product=product).count()
            return JsonResponse({'avg_rating': avg_rating['rating__avg'], 'counter': counter})

from django.shortcuts import render
from products_app.models import IndividualProduct
from django.http import JsonResponse
from search_app.models import SearchHistory
from products_app.models import ProductCategory

def search_view(request):
    cat = ProductCategory.objects.all()
    words = request.POST.get('name_search')
    qs = IndividualProduct.objects.filter(title__icontains=words)
    result = [{'id':x.id, 'title':x.title, 'image':x.image1.url} for x in qs]
    result_count = qs.count()
    if request.is_ajax():
        return JsonResponse({'result': result})
    else:
        if request.user.is_authenticated():
            SearchHistory.objects.create(user=request.user, word=words)
    context = {
        'qs': qs, 
        'results': result_count,
        'cat': cat
    }
    return render(request, 'search/search.html', context)

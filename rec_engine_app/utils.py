from profile_app.models import ObjectViewed
from products_app.models import IndividualProduct, ProductCategory

def preference_calculation(request):
    all_viewed_objects = ObjectViewed.objects.all()
    all_category_objects = ProductCategory.objects.all()
    category_count_list = {}
    for category in all_category_objects:
        category_count_list[category.id] = 0

    for viewed_item in all_viewed_objects:
        product_id = viewed_item.obj_id
        product_obj = IndividualProduct.objects.get(id=product_id)
        cat_id = product_obj.product_category.id
        category_count_list[cat_id] += 1
    most_viewed_category = max(category_count_list.keys(), key=(lambda i: category_count_list[i]))
    return most_viewed_category
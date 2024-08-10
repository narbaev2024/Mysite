from django_filters.rest_framework import FilterSet
from .models import Category, Product



# class CategoryFilter(FilterSet):
#     class Meta:y
#         model = Category
#         fields = {
#             'category': ['exact']
#         }

class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'price': ['gt', 'lt'],
            'active': ['exact'],
            'date': ['gt', 'lt'],
            'category': ['exact'],
        }








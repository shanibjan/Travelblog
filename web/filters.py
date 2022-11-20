import django_filters
from django.db.models import Q
from django_filters import CharFilter,DateFilter
from .models import *


class ProfileFilter(django_filters.FilterSet):
    check_date = DateFilter(field_name='date',lookup_expr='date')
    place = CharFilter(field_name='title',lookup_expr='icontains')

    class Meta:
        models = Blog
        fields = '__all__'
        exclude = ['user']


class PostFilter(django_filters.FilterSet):
    checkDate = DateFilter(field_name='date',lookup_expr='date')
    search = CharFilter(method='my_custom_filter')
    class Meta:
        models = Blog
        fields = ['checkDate','search']

    def my_custom_filter(self,queryset,name,value):
        return Blog.objects.filter(
            Q(title__icontains=value) | Q(place__icontains=value)
        )


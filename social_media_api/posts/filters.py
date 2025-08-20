import django_filters
from .models import Post

class PostFilter(django_filters.FilterSet):
    min_post_view = django_filters.NumberFilter(field_name="title", lookup_expr='gte')
    max_post_view = django_filters.NumberFilter(field_name="title", lookup_expr='lte')

    class Meta:
        model = Post
        fields = ['title']
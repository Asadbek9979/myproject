from django import template
from django.db.models import Count
from ..models import Post



register = template.Library()

@register.inclusion_tag('tags/lastest_posts.html')
def show_lastest_posts(count=5):
    lastest_posts = Post.objects.filter(status='active').order_by('-created_at')[:count]
    return {'lastest_posts': lastest_posts}

@register.inclusion_tag('tags/most_viewed.html')
def most_viewed(count=5):
    most_viewed = Post.objects.filter(status='active').order_by('-see')[:5]
    return {'most_viewed': most_viewed}




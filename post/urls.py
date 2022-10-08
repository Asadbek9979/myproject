from django.urls import path
from .views import list_view, detail_view, post_share, contact_view, about_view

app_name = "post"

urlpatterns = [
	path('about/',about_view, name="about"),
	path('contact/',contact_view, name="contact"),
	path('<int:id>/share/', post_share, name="post_share"),
	path('<int:id>/<slug:slug>/', detail_view, name='post_detail'),
	path('', list_view, name='post_list'),
]


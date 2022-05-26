from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('about', views.about_view, name='about'),
    path('contact', views.contact_view, name='contact'),
    path('product', views.product_view, name='product'),
    path('blog', views.blog_view,name='blog'),
    path('pw', views.pw_view,name='web programming')
]

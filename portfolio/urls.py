from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('about', views.about_view, name='about'),
    path('contact', views.contact_view, name='contact'),
    path('produtct', views.product_view, name='product'),
]

# shop app urls file

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('basic/',views.basic,name="basic"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('productview/<int:pid>',views.productview,name="productview"),
    path('order/',views.order,name="order"),
    path('search/',views.search,name="search"),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),
]
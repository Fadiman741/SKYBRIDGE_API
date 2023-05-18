
from django.contrib import admin
from django.urls import path
from api.views import property_list ,create_property, update_property

urlpatterns = [
    path('list/', property_list),
    path('create/', create_property),
    path('<int:pk>', update_property)
] 

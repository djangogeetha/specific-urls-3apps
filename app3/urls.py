from django.urls import path


from app3.views import *
app_name='something nothing'

urlpatterns=[
    path('seven/',seven,name='seven'),
    path('eight/',eight,name='eight'),
    ]
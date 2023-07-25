from django.urls import path


from app2.views import *
app_name='something something'

urlpatterns=[
    path('four/',four,name='four'),
    path('five/',five,name='five'),
    ]
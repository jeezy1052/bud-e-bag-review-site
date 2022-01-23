from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('review_form', views.review_form, name='review_form'),
    path('database_page', views.database_page, name='database_page'),
    path('success', views.success, name="success")
]
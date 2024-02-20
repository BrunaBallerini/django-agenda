from django.urls import path

from contact import views

app_name = 'contact'

urlpatterns = [
    path('contact/<int:contact_id>/detail/',
         views.contact, name='contact'),  # read
    path('contact/create/', views.create, name='create'),  # create
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
]

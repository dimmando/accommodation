from . import views
from django.urls import path
from django.http import HttpResponse


urlpatterns = [
    path("", views.BookView.as_view(), name="home"),
    path("about", views.about_view, name="about"),
    path("<slug:slug>/", views.BookDetail.as_view(), name="book_detail"),
    path("add-book", views.BookCreateView.as_view(), name="property_create"),
    path("property-list", views.PropertyView.as_view(), name="property_list"),
    path("<slug:slug>/edit", views.BookUpdateView.as_view(), name="book_update"),
    path("<slug:slug>/delete", views.BookDeleteView.as_view(), name="book_delete"),
]

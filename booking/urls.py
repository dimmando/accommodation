from . import views
from django.urls import path
from django.http import HttpResponse


urlpatterns = [
    # url for the root page
    path("", views.BookView.as_view(), name="home"),
    # url for the booking detail page
    path("<slug:slug>/", views.BookDetail.as_view(), name="book_detail"),
    # url for adding property
    path("add-book", views.BookCreateView.as_view(), name="property_create"),
    # url for editing the property
    path("<slug:slug>/edit", views.BookUpdateView.as_view(), name="book_update"),
    # url for deleting the property
    path("<slug:slug>/delete", views.BookDeleteView.as_view(), name="book_delete"),
]

# path("<slug:slug>/", views.post_detail, name="post_detail"),

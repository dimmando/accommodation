from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
# from .models import Post, Comment
# from .forms import CommentForm


# Create your views here.


# class AccommodationList(generic.ListView):
#     queryset = Post.objects.order_by("-created_on")
#     template_name = "booking/index.html"
#     paginate_by = 6

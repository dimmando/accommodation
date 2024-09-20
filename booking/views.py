# from django.shortcuts import render, get_object_or_404, reverse

from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse
from .models import BookPost
from .forms import BookForm


class BookView(generic.ListView):
    """
    https://docs.djangoproject.com/en/4.2/topics/class-based-views/generic-display/
    View from generic for viewing the current real estate scope
    """
    model = BookPost
    queryset = BookPost.objects.order_by('-created_on')
    template_name = 'index.html'
    context_object_name = 'book_list'
    paginate_by = 6


class BookDetail(View):
    """
    View to display the details of the property for booking
    """

    def get(self, request, slug, *arg, **kwarg):
        queryset = BookPost.objects.all()
        book = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "book_detail.html",
            {
                "book": book
            },
        )


class BookCreateView(LoginRequiredMixin, CreateView):
    """
    CreateView to create a new book post, sets the
    post_owner to the currently logged in user using the form.
    """
    model = BookPost
    template_name = 'book_form.html'
    form_class = BookForm

    def form_valid(self, form):
        """
        Method to set the owner of the post as the currently
        logged in user.
        https://www.youtube.com/watch?v=-s7e_Fy6NRU
        Also added messages:
        https://docs.djangoproject.com/en/4.2/ref/contrib/messages/
        https://stackoverflow.com/questions/28723266/django-display-message-after-post-form-submit
        """
        messages.success(self.request, 'Successfully added your Property!')
        form.instance.post_owner = self.request.user
        return super().form_valid(form)


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    UpdateView to allow the user to update their book post.
    Only the owner of the post can edit it.
    """
    model = BookPost
    template_name = 'book_form.html'
    form_class = BookForm

    def test_func(self):
        """
        Method to only allow the owner of the property post to update that post
        https://stackoverflow.com/questions/65402719/updateview-and-preventing-users-from-editing-other-users-content
        """
        book = self.get_object()
        if self.request.user == book.post_owner:
            return True
        return False

    def form_valid(self, form):
        """
        Method to set the user that edited to the post_owner
        message set to update the user when the property has been posted
        https://stackoverflow.com/questions/28723266/django-display-message-after-post-form-submit
        """
        messages.success(self.request, 'Successfully updated your Property!')
        form.instance.post_owner = self.request.user
        return super().form_valid(form)


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    DeleteView to delete the book posts, only allowed by the owner of the post.
    https://www.geeksforgeeks.org/deleteview-class-based-views-django/
    """
    model = BookPost

    def test_func(self):
        """
        Method to only allow the post_owner of the
        book post to delete that post
        https://stackoverflow.com/questions/65402719/updateview-and-preventing-users-from-editing-other-users-content
        """
        book = self.get_object()
        if self.request.user == book.post_owner:
            return True
        return False

    def get_success_url(self):
        """
        On success, report success message for deletion
        https://stackoverflow.com/questions/24822509/success-message-in-deleteview-not-shown
        """
        messages.success(self.request, "Your Property has been deleted!")
        return reverse('home')
    template_name = 'book_delete.html'


class PropertyView(LoginRequiredMixin, generic.ListView):
    """
    https://docs.djangoproject.com/en/4.2/topics/class-based-views/generic-display/
    View from generic for viewing the current book posts
    """
    model = BookPost
    # queryset = BookPost.objects.order_by('-created_on')
    template_name = 'property_list.html'
    context_object_name = 'property_list'

    def get_queryset(self):
        """
        Override method to customize queryset for the view
        """
        return BookPost.objects.filter(post_owner=self.request.user)

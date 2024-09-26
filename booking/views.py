from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse
from .models import BookPost
from .forms import BookForm
from django.db.models import Q


def about_view(request):
    """ Method to display About page """
    return render(request, 'about.html')


class BookView(generic.ListView):
    """
    View from generic for viewing paginated all real estate scope on homepage
    """
    model = BookPost
    queryset = BookPost.objects.order_by('-created_on')
    template_name = 'index.html'
    context_object_name = 'book_list'
    paginate_by = 6

    def get_queryset(self, **kwargs):
        """ Search method """
        query = self.request.GET.get("q")
        if query:
            book_list = self.model.objects.filter(
                Q(title__icontains=query)
                | Q(description__icontains=query)
                | Q(accommodation_type__icontains=query)
                | Q(city__icontains=query),
            )
        else:
            book_list = self.model.objects.order_by('-created_on')
        return book_list


class BookDetail(View):
    """
    View to display the details of the each property proposed for booking
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
    CreateView to create a new property post, sets the
    post_owner to the currently logged in user using the form.
    """
    model = BookPost
    template_name = 'book_form.html'
    form_class = BookForm

    def form_valid(self, form):
        """
        Method to set the owner of the post as the currently
        logged in user, validating form. Also displaying message.
        """
        messages.success(self.request, 'Successfully added your Property!')
        form.instance.post_owner = self.request.user
        return super().form_valid(form)


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    UpdateView to allow the user to update their propery post.
    Only the owner of the post can edit it.
    """
    model = BookPost
    template_name = 'book_form.html'
    form_class = BookForm

    def test_func(self):
        """
        Method to only allow the owner of the property post to update that post
        """
        book = self.get_object()
        if self.request.user == book.post_owner:
            return True
        return False

    def form_valid(self, form):
        """
        Method to set the user that edited to the post_owner
        message set to update the user when the property has been posted
        """
        messages.success(self.request, 'Successfully updated your Property!')
        form.instance.post_owner = self.request.user
        return super().form_valid(form)


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    DeleteView to delete the property post,
    only allowed by the owner of the post
    """
    model = BookPost
    template_name = 'book_delete.html'

    def test_func(self):
        """
        Method to only allow the post_owner of the
        property post to delete that post
        """
        book = self.get_object()
        if self.request.user == book.post_owner:
            return True
        return False

    def get_success_url(self):
        """
        On success, report success message for deletion
        """
        messages.success(self.request, "Your Property has been deleted!")
        return reverse('home')


class PropertyView(LoginRequiredMixin, generic.ListView):
    """
    View from generic for viewing all booking posts scope for the current user
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

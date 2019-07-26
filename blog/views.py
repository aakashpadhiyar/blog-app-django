from django.views  import generic
from .models import Post
# Create your views here.

class BlogListView(generic.ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

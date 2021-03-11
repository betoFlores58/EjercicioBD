from django.views.generic import ListView
from .models import Post,Image

# Create your views here.

class HomePageView(ListView):
    model = Post
    model = Image
    template_name = 'home.html'
    context_object_name = 'listado'
    context_object_name = 'images'
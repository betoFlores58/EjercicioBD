from django.views.generic import ListView
from .models import Post,Texto

# Create your views here.

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'listado'

class OtraPageView(ListView):
    model = Texto
    template_name = 'pagina.html'
    context_object_name = 'texto'

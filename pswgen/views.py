from django.shortcuts import render

from django.views import generic
# Create your views here.

# class IndexView(generic):


#class IndexView(generic.ListView):
#    template_name = 'pswgen/index.html'

def index(request):
    return render(request, 'pswgen/index.html')

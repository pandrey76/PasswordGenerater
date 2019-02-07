from django.shortcuts import render

from .common.pswgen import get_rnd_psw

# from django.views import generic


# Create your views here.

# class IndexView(generic):

# class IndexView(generic.ListView):
#    template_name = 'pswgen/index.html'


def index(request):
    print(request)
    psw = get_rnd_psw()
    return render(request, 'pswgen/index.html',
                  {
                        'message': "Hello from index.",
                           'random_password': psw,
                  }
                  )

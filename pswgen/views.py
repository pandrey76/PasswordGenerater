from django.shortcuts import render

from .common.pswgen import get_rnd_psw

from .forms import GeneratePasswordForm

# from django.views import generic


# Create your views here.

# class IndexView(generic):

# class IndexView(generic.ListView):
#    template_name = 'pswgen/index.html'


def index(request):
    form = GeneratePasswordForm(request.POST or None)
    psw = None
    context = {
                'form': form,
                'random_password': psw
                }
    if request.method == 'POST' and form.is_valid():
        psw_length = int(form.cleaned_data.get('psw_length', None))
        if (psw_length <= 32) and (psw_length >= 6):
            context['random_password'] = get_rnd_psw(psw_length )
            return render(request, 'pswgen/index.html', context)
        else:
            return render(request, 'pswgen/index.html', context)
    else:
        psw_length_initial = 6
        context['random_password'] = get_rnd_psw(psw_length_initial)
        return render(request, 'pswgen/index.html', context)

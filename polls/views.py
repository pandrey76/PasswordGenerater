from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

# Используем generic


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
            Return the last five published questions.
        """
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse, HttpResponseRedirect
# from django.urls import reverse

# from .models import Question, Choice

# from django.http import Http404

# from django.template import loader

# Create your views here.

# ---------Первая редакция-----------------
# def index(request):
#     return HttpResponse("Hello, world. You're at the pols index.")
# -----------------------------------------

# ---------Вторая редакция-----------------
# def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date',)[:5]
#    output = ', '.join(([q.question_text for q in latest_question_list]))
#    return HttpResponse(output)
# -----------------------------------------

# ---------Третья редакция-----------------
# def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    template = loader.get_template('polls/index.html')
#    context = {
#        'latest_question_list': latest_question_list,
#    }
#    return HttpResponse(template.render(context, request))
# -----------------------------------------


# def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    context = {'latest_question_list': latest_question_list}
#    return render(request, 'polls/index.html', context)


# ---------Первая редакция-----------------
# def detail(request, question_id):
#    return HttpResponse("You're looking at question %s." % question_id)
# -----------------------------------------

# ---------Вторая редакция-----------------
# def detail(request, question_id):
#    try:
#        question = Question.objects.get(pk=question_id)
#    except Question.DoesNotExist:
#        raise Http404("Question does not exist")
#    return render(request, 'polls/detail.html', {'question': question})
# -----------------------------------------


# def detail(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/detail.html', {'question': question})


# def results(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # After incrementing the choice count, the code returns an HttpResponseRedirect
        # rather than a normal HttpResponse.HttpResponseRedirect takes a single argument:
        # the URL to which the user will be redirected(see the following point
        # how we construct the URL in this case
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

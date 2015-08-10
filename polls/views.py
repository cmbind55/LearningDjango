from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from polls.models import Choice, Question
from django.http import HttpResponse

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def results(request, question_id):
    # get an object instance to the question_id that was passed to the VIEW
    # or return a 404 error exception
    question = get_object_or_404(Question, pk=question_id)

    # render the current results for the voting on the question
    return render(request, 'polls/results.html', {'question': question})


#def vote(request, question_id):
#    return HttpResponse("You're voting on question %s." % question_id)
def vote(request, question_id):

    # get an object instance for the passed in question ID from the form POST
    #
    p = get_object_or_404(Question, pk=question_id)
    try:
        # try to set the selected choice to the object ID from the form POST
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    # if we get an exception in trying to get the selected choice ID
    except (KeyError, Choice.DoesNotExist):
        # then, Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        # else, then record the vote, save it in the selected_choice object
        selected_choice.votes += 1
        selected_choice.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))



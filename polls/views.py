from django.shortcuts import render
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.http import HttpResponse
from django.http import Http404
from django.views import generic
from django.utils import timezone
from polls.models import Choice, Question




class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]



class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


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

def get_queryset(self):
    """
    Return the last five published questions (not including those set to be
    published in the future).
    """
    return Question.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]


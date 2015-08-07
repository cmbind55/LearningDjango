from django.shortcuts import render
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from django.views import generic
from django.utils import timezone
from polls.models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    # page_title = 'Monty Python Polls'
    # c = RequestContext(generic.ListView, {'page_title': 'Monty Python Polls'})

    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #    context = {'latest_question_list': latest_question_list}
    #    return render(request, 'polls/index.html', context)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(IndexView, self).get_context_data(**kwargs)
        # Add in some context variable that can be accessed by the template
        context['page_title'] = 'This is AMAZING!!!'
        return context

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


# def vote(request, question_id):
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

def about(request):
    # View code here... (if any)
    return render(request, 'polls/about.html', {"page_title": "About this site"})
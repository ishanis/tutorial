from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse

#from django.template import RequestContext, loader
from polls.models import Question, Choice

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ','.join([p.question_text for p in latest_question_list])
    """template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_question_list':latest_question_list,
    })"""
    #return HttpResponse("Hello, You are at the polls index")
    #return HttpResponse(template.render(context))
    context = {'latest_question_list':latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    #return HttpResponse("You're looking at question %s" % question_id)
    """try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404"""
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    """response = "You're looking at the results of the question %s"
    return HttpResponse(response % question_id)"""
    return render(request, 'polls/results.html', {'question':question})
def vote(request,question_id):
    p = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist): 
        return render(request, 'polls/detail.html', {
                'question': p,
                'error_message': "You didn't select a choice.",
                })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
    #return render(request, 'polls/results.html', {'question':p})



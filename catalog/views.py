from django.shortcuts import render

# Create your views here.
from catalog.models import Ieltsstories, Ieltstest

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_Stories = Ieltsstories.objects.all().count()


    context = {
        'num_Stories' : num_Stories
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic

class IeltsstoriesListView(generic.ListView):
    model = Ieltsstories
    paginate_by = 10
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(IeltsstoriesListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context

from django.shortcuts import get_object_or_404


class IeltsstoriesDetailView(generic.DetailView):
    model = Ieltsstories
    def story_detail_view(request, primary_key):
        ieltsstories = get_object_or_404(Ieltsstories, pk=primary_key)
        return render(request, 'catalog/ieltsstories_detail.html', context={'story': ieltsstories})

def test_list(request):
    l =[]
    t = Ieltstest.objects.values('sublevel')
    for i in range(len(t)):
    #context['sub'] =  Ieltstest.objects.filter().values('sublevel')[1]['sublevel']
        l +=  [t[i]['sublevel']]
    context = {'sub':set(l)}
    return render(request, 'catalog/ieltstest_list.html', context=context)

from django.shortcuts import get_object_or_404
#from catalog.forms import answerform
from django.http import HttpResponseRedirect
from django.urls import reverse
import json

def testDetailView(request,sub):
    ct = Ieltstest.objects.all().filter(sublevel=sub)
    context ={'sub': sub, 'content' : ct }
    if request.method == 'POST':
        t = request.POST.dict()
        #p.pop('csrfmiddlewaretoken')
        #p.pop("csrfmiddlewaretoken")
        p =[]

        for i in ct:
            try:
                p+= [str(i.qnumber) +'. ' + i.qcontent, 'your answer:   '+ t[str(i.qnumber)],'correct answer:   ' + i.correctanswer]
            except:
                p+=[str(i.qnumber) +'. ' + i.qcontent, 'your answer:   None', 'correct answer:   ' + i.correctanswer]
                continue
        context['result'] = p
        context['sum'] = 'you answer correct ' + str(s) + '/' + str(int(len(p)/3))
        return render(request, 'catalog/result.html', context =context)

    return render(request, 'catalog/ieltstest_detail.html', context =context)

def result(request,sub):

    return render(request, 'catalog/result.html',context=context)

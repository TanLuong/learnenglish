from django.shortcuts import render

# Create your views here.
from catalog.models import ieltsstories, ieltstest

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_Stories = ieltsstories.objects.all().count()


    context = {
        'num_Stories' : num_Stories
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic

class ieltsstoriesListView(generic.ListView):
    model = ieltsstories
    paginate_by = 10
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(ieltsstoriesListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context

from django.shortcuts import get_object_or_404


class ieltsstoriesDetailView(generic.DetailView):
    model = ieltsstories
    def story_detail_view(request, primary_key):
        ieltsstories = get_object_or_404(ieltsstories, pk=primary_key)
        return render(request, 'catalog/ieltsstories_detail.html', context={'story': ieltsstories})

def test_list(request):
    l =[]
    t = ieltstest.objects.values('sublevel')
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
    ct = ieltstest.objects.all().filter(sublevel=sub)
    context ={'sub': sub, 'content' : ct }
    if request.method == 'POST':
        t = request.POST.dict()
        #p.pop('csrfmiddlewaretoken')
        #p.pop("csrfmiddlewaretoken")
        p =[]
        s = 0
        for i in ct:
            try:
                s+=1
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

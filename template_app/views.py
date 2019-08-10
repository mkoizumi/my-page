from django.shortcuts import render
from django.http import HttpResponse
from template_app.models import Topic, Webpage, AccessRecord

# Create your views here.

def index(request):
    return HttpResponse("My second challenge!")


# connecting model (database) to html
def model(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dic = {'access_records' : webpage_list}
    return render(request, 'template_app/model.html', context = date_dic)


# this is the added page specific to templat_app
def help(request):
    helpdic = {'help_insert' : 'Hey! message from help'}
    return render(request, 'template_app/help.html', context = helpdic)

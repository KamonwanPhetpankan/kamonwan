from django.shortcuts import render
from django.utils import encoding #smart_unicode
from urllib.parse import parse_qsl

from .models import Event

# Create your views here.
def index(req):
    return render(req, 'myapp/index.html')
    # if req.method == 'POST':
    #     post = req.POST
    #     s = Service()
    #     s.icon = post['icon']
    #     s.title = post['title']
    #     s.detail = post['detail']
    #     s.save()
    #     services = Service.objects.all()
    #     print(services)
    #     return render(req, 'myapp/index.html', { 'services': services })
    # else:
    #     print('ร้องขอทำมะดา')
    #     services = Service.objects.all()
    #     print(services)
    #     return render(req, 'myapp/index.html', { 'services': services })

def events(req):
    events = Event.objects.all()
    return render(req, 'myapp/events.html', { 'events': events })

def addevents(req):
    if req.method == 'POST':
        post = req.POST
        s = Event()
        s.eventname = post['eventname']
        s.time = post['time']
        s.location = post['location']
        s.save()
    return render(req, 'myapp/addevents.html')
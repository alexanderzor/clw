# -*- coding: utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from forms import UploadFileForm, FeedBackForm, SearchForm
from models import Task, Text
from django.core.mail import EmailMultiAlternatives
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from models import Consultant
from accounts.models import Need, Thank, Ask, Witness

@login_required(login_url='register_view')
def forbidden(request):
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
    else:
        form = FeedBackForm()
    context = {'form': form}
    return render(request, 'forbidd.html', context)

@login_required(login_url='register_view')
def index(request, key=''):
    if not key:
        video = Task.objects.first()
        #return HttpResponseRedirect(reverse('index', kwargs={'key': 'Lesson1'}))
    else:
        video = Task.objects.filter(title=key).first()
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
    else:
        form = FeedBackForm()
    #video = Task.objects.filter(title=key).first()
    tasks = Task.objects.filter(private=False).all()
    context = {'tasks': tasks, 'form': form, 'video': video}
    return render(request, 'index.html', context)


@login_required(login_url='register_view')
def feedback(request):
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            s = cd['subject']
            if s == 'need':
                need = Need.objects.create(author=request.user, description=cd['text'])
                need.save()
            elif s == 'thanks':
                thank = Thank.objects.create(author=request.user, description=cd['text'])
                thank.save()
            elif s == 'ask':
                ask = Ask.objects.create(author=request.user, description=cd['text'])
                ask.save()
            elif s == 'witness':
                witness = Witness.objects.create(author=request.user, description=cd['text'])
                witness.save()
            subject, from_email, to = cd['subject'], 'cwitnesses@gmail.com', 'Len4ikoy@gmail.com'
            text_content = request.user.email + ':\n' + cd['text']
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.send()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = FeedBackForm()
    return HttpResponseRedirect(reverse('index'))

@login_required
def uploader(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UploadFileForm()
    context = {'form': form}
    return render(request, 'uploader.html', context)


@login_required(login_url='register_view')
def private(request, key=''):
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
    else:
        form = FeedBackForm()
    tasks = Task.objects.filter(private=True).all()
    video = Task.objects.filter(private=True).first()
    context = {'tasks': tasks, 'form': form, 'video': video}
    return render(request, 'private.html', context)

@login_required(login_url='register_view')
def consults(request):
    consultants = Consultant.objects.filter(active=True)
    context = {'consultants': consultants}
    return render(request, 'consults.html', context)

@login_required(login_url='register_view')
def need_board(request, key='all'):
    if key == 'my':
        needs = Need.objects.filter(author=request.user, active=True).all()
    else:
        needs = Need.objects.filter(active=True).all()
    context = {'needs': needs}
    return render(request, 'need_board.html', context)

@login_required(login_url='register_view')
def thank_board(request):
    thanks = Thank.objects.filter(active=True).all()
    context = {'thanks': thanks}
    return render(request, 'thank_board.html', context)

@login_required(login_url='register_view')
def vote(request, key):
    need = Need.objects.get(id=int(key))
    request.user.vote(need)
   # need.voters.add(request.user)
    return HttpResponseRedirect(reverse('need_board'))


@login_required(login_url='register_view')
def archive(request, key='all'):
    tasks = []
    texts = []
    if key == 'all':
        tasks = Task.objects.all()
        texts = Text.objects.all()
    elif key == 'video_lessons':
        tasks = Task.objects.filter(private=False).all()
    elif key == 'video_private':
        tasks = Task.objects.filter(private=True).all()
    elif key == 'text_lessons':
        texts = Text.objects.all()
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            cd = search_form.cleaned_data
            tasks = Task.objects.filter(keyword__icontains=cd['keyword'])
    else:
        search_form = SearchForm()
    context = {'tasks': tasks, 'texts': texts, 'search_form': search_form}
    return render(request, 'archive.html', context)


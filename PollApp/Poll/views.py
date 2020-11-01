from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreatePollForm
from .models import Poll

# Create your views here.
def home(request):
    Polls = Poll.objects.all()
    context = {
        'Polls': Polls, 
    }
    return render(request, 'Poll/home.html', context)

def create(request):
    form = CreatePollForm()
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['question'])
            form.save()
        return redirect('home')

    context = {
        'form': form
    }
    return render(request, 'Poll/create.html', context)

def vote(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    if request.method == 'POST':
        print(request.POST['poll'])
        select_option = request.POST['poll']
        if select_option == 'option1':
            poll.option_one_count += 1
        elif select_option == 'option2':
            poll.option_two_count += 1
        elif select_option == 'option3':
            poll.option_three_count += 1
        else:
            return HttpResponse(400, "Invalid Form")
        poll.save()
        return redirect('results', poll.id)
        
    context = {
        'poll': poll,
    }
    return render(request, 'Poll/vote.html', context)

def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {
        'poll': poll,
    }
    return render(request, 'Poll/results.html', context)
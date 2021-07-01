from django.shortcuts import render, redirect
from .models import ChangeURL
from .forms import ChangeURLForm
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, 'main/home.html', {'title': 'Сокра.тим'})

@login_required
def index(request):
    form = ChangeURLForm(request.POST)
    if request.method == 'POST':
        form = ChangeURLForm(request.POST)
        if form.is_valid():
            new_url = ChangeURL()
            new_url.fullurl = request.POST.get("fullurl")
            new_url.slug = request.POST.get("slug")
            new_url.user = request.user
            new_url.save()
            return redirect('/links')

    new_urls = ChangeURL.objects.filter(user=request.user)

    return render(request, 'main/links.html', {
                                                "form": form,
                                                "new_urls": new_urls
                                               })

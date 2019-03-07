from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Candidate


def index(request):
    candidates = candidates.objects.all()
    return render(request, 'candidates/index.html', {'candidates': candidates})

def add(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, '投票成功')
        return redirect('candidates:index')

    return render(request, 'candidates/add.html', {'form': form})
from django.shortcuts import render, redirect
from .forms import SignUpForm, StatementForm
from .models import Statement
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.utils import timezone


def index(request):
    return render(request, "main/index.html")

def about(request):
    return render(request, "main/about.html")


def create_statements(request):
    if request.method == 'POST':
        form = StatementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = StatementForm()
        return render(request, 'main/create_statements.html', {'form': form})


class UserOrdersListView(ListView):
    model = Statement
    context_object_name = 'statements'
    now = timezone.now()
    extra_context = {'title': 'История записей', 'now': now}

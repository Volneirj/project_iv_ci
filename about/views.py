from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from .forms import BookSuggestionForm
from .models import BookSuggestion

def about_view(request):
    return render(request, 'about/about.html')

def suggest_book_view(request):
    if request.method == 'POST':
        form = BookSuggestionForm(request.POST)
        if form.is_valid():
            BookSuggestion.objects.create(
                book_title=form.cleaned_data['book_title'],
                author=form.cleaned_data['author'],
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                reason=form.cleaned_data['reason']
            )
            return redirect('thank_you')
    else:
        form = BookSuggestionForm()

    return render(request, 'about/suggest_book.html', {'form': form})

def admin_required(view_func):
    decorated_view_func = user_passes_test(lambda u: u.is_superuser)(view_func)
    return decorated_view_func

@admin_required
def view_suggestions(request):
    suggestions = BookSuggestion.objects.all()
    return render(request, 'about/view_suggestions.html', {'suggestions': suggestions})


def thank_you_view(request):
    return render(request, 'about/thank_you.html')
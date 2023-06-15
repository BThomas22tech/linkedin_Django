from django.shortcuts import render
from django.http import Http404
from .models import Notes
from django.views.generic import DetailView, ListView, CreateView

class NotesCreateView(CreateView):
    model = Notes
    fields = ['title','text']
    success_url ='/smart/notes'
    
class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    
def detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note doesn't exist")
    return render(request, 'notes/notes_detail.html', {'note':note})
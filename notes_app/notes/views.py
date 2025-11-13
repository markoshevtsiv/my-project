from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import NoteForm
from .models import Note, Category


def index(request):
    notes = Note.objects.all()
    return render(request, 'notes/index.html', {'notes': notes})

class NoteListView(ListView):
    model = Note
    template_name = "notes/index.html"
    context_object_name = "notes"

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        search_title = self.request.GET.get('search_title')
        reminder = self.request.GET.get('reminder')

        if category:
            queryset = queryset.filter(category__title__icontains=category)
        if search_title:
            queryset = queryset.filter(title__icontains=search_title)
        if reminder:
            queryset = queryset.filter(reminder__date=reminder)

        return queryset

class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes/note_create.html'
    success_url = reverse_lazy('index')

class NoteDetailView(DetailView):
    model = Note
    form_class = NoteForm
    template_name = 'notes/note_detail.html'

class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes/note_edit.html'
    success_url = reverse_lazy('index')

class NoteDeleteView(DeleteView):
    model = Note
    form_class = NoteForm
    template_name = "notes/note_delete.html"
    success_url = reverse_lazy('index')

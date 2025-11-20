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
    is_paginated = 1

    def get_queryset(self):
        queryset = super().get_queryset()

        # Назви ПОВНІСТЮ відповідають формі
        search = self.request.GET.get('search')
        category = self.request.GET.get('category')
        reminder = self.request.GET.get('reminder')

        # Пошук за назвою
        if search and search.strip():
            queryset = queryset.filter(title__icontains=search.strip())

        # Пошук за категорією
        if category and category.strip():
            queryset = queryset.filter(category__title__icontains=category.strip())

        # Пошук за датою нагадування
        if reminder:
            queryset = queryset.filter(reminder=reminder)

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
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.db.models import Q
from .forms import NoteForm
from .models import Note, Category

def index(request):
    return render(request, 'notes/index.html')


class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = "notes/index.html"
    context_object_name = "notes"
    login_url = '/login/'

    def get_queryset(self):
        user = self.request.user
        view_type = self.request.GET.get("view", "personal")  # "personal" або "group"

        queryset = Note.objects.filter(user=user)  # персональні нотатки

        if view_type == "group":
            # нотатки груп, де користувач є учасником
            queryset = Note.objects.filter(group__in=user.groups.all())

        search = self.request.GET.get("search", "")
        category = self.request.GET.get("category", "")
        reminder = self.request.GET.get("reminder", "")

        if search:
            queryset = queryset.filter(Q(title__icontains=search) | Q(text__icontains=search))
        if category:
            queryset = queryset.filter(category__title__icontains=category)
        if reminder:
            queryset = queryset.filter(reminder__date=reminder)

        return queryset



class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes/note_create.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'notes/note_detail.html'

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes/note_edit.html'
    success_url = reverse_lazy('index')

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = "notes/note_delete.html"
    success_url = reverse_lazy('index')

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

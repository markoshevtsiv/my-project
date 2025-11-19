
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from .models import Book, Author, Notes
from .forms import AuthorForm, BookForm, NotesForm
from django.utils.timezone import now
from datetime import timedelta


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author_form.html'
    success_url = reverse_lazy('author_list')


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author_form.html'
    success_url = reverse_lazy('author_list')


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'author_confirm_delete.html'
    success_url = reverse_lazy('author_list')


class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'
    context_object_name = 'authors'

    def get_queryset(self):
        queryset = super().get_queryset()
        age = self.request.GET.get('age')
        search_name = self.request.GET.get('search')

        if age:
            min_birth_date = now().date() - timedelta(days=int(age) * 365)
            queryset = queryset.filter(birth_date__lte=min_birth_date)

        if search_name:
            queryset = queryset.filter(first_name__icontains=search_name)

        return queryset


class BookCreateView(CreateView):
    """
    Клас для створення нової книги.
    Використовує стандартний клас Django CreateView.
    """
    model = Book  # Вказуємо модель, з якою працює представлення
    form_class = BookForm  # Вказуємо форму, яка використовується для введення даних
    template_name = 'book_form.html'  # Шаблон для відображення форми
    success_url = reverse_lazy('book_list')  # Перенаправлення після успішного створення книги


class BookDetailView(DetailView):
    """
    Відображення деталей книги.
    Використовує стандартний клас Django DetailView.
    """
    model = Book  # Вказуємо модель
    template_name = 'book_detail.html'  # Шаблон для відображення деталей книги
    context_object_name = 'book'  # Ім'я змінної, яка передається в шаблон (за замовчуванням 'object')


class BookUpdateView(UpdateView):
    """
    Редагування книги.
    Використовує стандартний клас Django UpdateView.
    """
    model = Book  # Вказуємо модель
    form_class = BookForm  # Вказуємо форму для редагування
    template_name = 'book_form.html'  # Шаблон форми редагування

    def get_success_url(self):
        """
        Після оновлення книги перенаправляє користувача на сторінку деталей книги.
        Використовує reverse_lazy для побудови URL.
        """
        return reverse_lazy('book_detail', kwargs={'pk': self.object.pk})


class BookDeleteView(DeleteView):
    """
    Видалення книги.
    Використовує стандартний клас Django DeleteView.
    """
    model = Book  # Вказуємо модель
    success_url = reverse_lazy('book_list')  # Перенаправлення після видалення книги
    template_name = 'book_confirm_delete.html'  # Шаблон для підтвердження видалення


class BookListView(ListView):
    """
    Відображає список книг.
    Використовує стандартний клас Django ListView.
    """
    model = Book  # Вказуємо модель
    template_name = 'book_list.html'  # Шаблон для списку книг
    context_object_name = 'books'  # Ім'я змінної, яка буде передана в шаблон (за замовчуванням 'object_list')
    paginate_by = 2  # Встановлюємо пагінацію (по 10 книг на сторінку)

    def get_queryset(self):
        """
        Оптимізований запит для вибірки книг разом з авторами (select_related).
        Також додається пошук книг за заголовком, якщо переданий параметр `search` у запиті.
        """
        queryset = Book.objects.select_related('author')  # Оптимізація: приєднання автора одним SQL-запитом
        search_query = self.request.GET.get('search')  # Отримання значення параметра `search` з URL
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)  # Фільтрація книг за частковим співпадінням у назві, ігнорується регістр
        return queryset  # Повернення списку книг


class NoteCreateView(CreateView):
    model = Notes
    form_class = NotesForm
    template_name = 'note_create.html'
    success_url = reverse_lazy('note_list')

class NoteDetailView(DetailView):
    model = Notes
    template_name = 'note_detail.html'
    context_object_name = 'note'

class NoteUpdateView(UpdateView):
    model = Notes
    form_class = NotesForm
    template_name = 'note_update.html'

    def get_success_url(self):
        return reverse_lazy('note_detail', kwargs={'pk': self.object.pk})

class NoteDeleteView(DeleteView):
    model = Notes
    template_name = 'note_confirm_delete.html'
    success_url = reverse_lazy('note_list')

class NoteListView(ListView):
    model = Notes
    template_name = 'note_list.html'
    context_object_name = 'notes'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)
        return queryset




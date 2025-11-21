from django.contrib.auth.views import LoginView
from django.urls import path
# from .views import AuthorCreateView, AuthorDetailView, AuthorUpdateView, AuthorDeleteView, AuthorListView
from .views import BookListView, BookCreateView, BookDetailView, BookUpdateView, BookDeleteView, NoteListView, \
    NoteDetailView, NoteCreateView, NoteUpdateView, NoteDeleteView, login_view, register_view, logout_view

# urlpatterns = [
#      path('', AuthorListView.as_view(), name='author_list'),
#      path('create/', AuthorCreateView.as_view(), name='author_create'),
#      path('<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
#      path('<int:pk>/edit/', AuthorUpdateView.as_view(), name='author_edit'),
#      path('<int:pk>/delete/', AuthorDeleteView.as_view(), name='author_delete'),
# ]

urlpatterns = [
   path('', BookListView.as_view(), name='book_list'),
   path('new/', BookCreateView.as_view(), name='book_create'),
   path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),
   path('<int:pk>/edit/', BookUpdateView.as_view(), name='book_update'),
   path('<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
   path('notes/', NoteListView.as_view(), name='note_list'),
   path('notes/<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
   path('notes/create/', NoteCreateView.as_view(), name='note_create'),
   path('notes/<int:pk>/update/', NoteUpdateView.as_view(), name='note_update'),
   path('notes/<int:pk>/delete/', NoteDeleteView.as_view(), name='note_delete'),
   path('login/', login_view, name='login'),
   path('register/', register_view, name='register'),
   path('logout/', logout_view, name='logout'),


]

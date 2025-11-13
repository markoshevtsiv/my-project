from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.NoteListView.as_view(), name='index'),
    path('notes/create', views.NoteCreateView.as_view(), name='note_create'),
    path('notes/<int:pk>', views.NoteDetailView.as_view(), name='note_detail'),
    path('notes/<int:pk>/edit', views.NoteUpdateView.as_view(), name='note_edit'),
    path('notes/<int:pk>/delete', views.NoteDeleteView.as_view(), name='note_delete'),
]
from django.urls import path
from .views import *

urlpatterns = [
    path("", NoteListView.as_view(), name="note-list"),
    path("<int:pk>/", NoteDetailView.as_view(), name="note-detail"),
    path("add_note/", add_note_view, name="add-note")
]

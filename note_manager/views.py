from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import Note
from .forms import AddNoteForm

class NoteListView(ListView):
    model = Note
    context_object_name = "notes"

class NoteDetailView(DetailView):
    model = Note
    context_object_name = "note"

def add_note_view(request):
    if request.method == "POST":
        form = AddNoteForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]

            note = Note.objects.create(title=title,
                                       content=content)
            note.save()

            return redirect("note-list")
    else:
        form = AddNoteForm()

    return render(request, "note_manager/add_note.html", {"form": form})
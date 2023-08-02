from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView


from .models import Notes
# Create your views here.

class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'

    def get_queryset(self):
        return Notes.objects.all()

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/notes_detail.html'

    def get_queryset(self):
        return Notes.objects.all()

# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#         return render(request, 'notes/notes_detail.html', {'note': note})
#     except Notes.DoesNotExist:
#         return HttpResponse('Note not found')

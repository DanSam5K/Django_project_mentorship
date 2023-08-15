from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView


from .forms import NotesForm
from .models import Notes
# Create your views here.


class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm


class NotesCreateView(CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


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

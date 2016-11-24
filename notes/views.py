from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import Http404
from notes.models import Note
from notes.forms import NoteForm


class Index(View):
    template_name = 'notes/index.html'

    def get_context_data(self):
        context = {
            'page_title': 'Home',
            'note_list': Note.objects.all(),
                }
        return context

    # Handles GET Request
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    # Handles POST Request
    def post(self, request, *args, **kwargs):
        form = NoteForm(request.POST)
        context = self.get_context_data()

        if (form.is_valid()):
            form.save()
        return render(request, self.template_name, context )


class Edit(View):
    template_name = 'notes/edit.html'

    def get_context_data(self, **kwargs):
        context = {}
        try:
            note_id = kwargs.get('id', 0)
            note = Note.objects.get(id=note_id)
        except:
            raise Http404
        else:
            context['note'] = note
            return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)
        
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = NoteForm(request.POST, instance=context.get('note'))

        if (form.is_valid()):
            form.save()
        return render(request, self.template_name, context )

class Delete(View):
    def get(self, request, *args, **kwargs):
        note_id = kwargs.get('id', 0)
        note = Note.objects.get(id=note_id)
        note.delete()
        return redirect('index')

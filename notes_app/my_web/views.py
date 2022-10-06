from django.shortcuts import render, redirect

from notes_app.my_web.forms import CreateProfileForm, CreateNoteForm, EditNoteForm, DeleteNoteForm
from notes_app.my_web.models import Profile, Note


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def show_home(request):
    profile = get_profile()
    if not profile:
        if request.method == 'POST':
            form = CreateProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('show home')
        else:
            form = CreateProfileForm(request.POST)

        context = {
            'form': form,
            'no_profile': True,
        }
        return render(request, 'home-no-profile.html', context)
    notes = Note.objects.all()
    context = {
        'profile': profile,
        'notes': notes,
    }
    return render(request, 'home-with-profile.html', context)


def show_profile(request):
    profile = get_profile()
    notes = Note.objects.all()
    count_notes = len(notes)
    context = {
        'profile': profile,
        'count_notes': count_notes
    }
    return render(request, 'profile.html', context)


def delete_profile(request):
    profile = get_profile()
    notes = Note.objects.all()
    notes.delete()
    profile.delete()
    return redirect('show home')

def add_note(request):
    if request.method == 'POST':
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = CreateNoteForm()

    context = {
        'form': form,
    }
    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = EditNoteForm(instance=note)

    context = {
        'form': form,
        'note': note
    }
    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = DeleteNoteForm(instance=note)

    context = {
        'form': form,
        'note': note
    }
    return render(request, 'note-delete.html', context)


def details_note(request, pk):
    note = Note.objects.get(pk=pk)
    context = {
        'note': note,
    }
    return render(request, 'note-details.html', context)

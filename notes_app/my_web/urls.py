from django.urls import path

from notes_app.my_web.views import show_home, show_profile, add_note, edit_note, delete_note, details_note, \
    delete_profile

urlpatterns = (

    path('', show_home, name='show home'),

    path('profile', show_profile, name='show profile'),
    path('profile/delete', delete_profile, name='delete profile'),

    path('add', add_note, name='add note'),
    path('edit/<int:pk>', edit_note, name='edit note'),
    path('delete/<int:pk>', delete_note, name='delete note'),
    path('details/<int:pk>', details_note, name='details note'),

)

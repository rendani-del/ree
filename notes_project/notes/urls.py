from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup_login, name='home'),  # Home page, both forms
    path('signup/', views.signup_login, name='signup'),  # Signup
    path('login/', views.signup_login, name='login'),
    path('logout/', views.logout_view, name='logout'),  # Added logout route
    path('your_notes/', views.your_notes, name='your_notes'),  
    path('saved_notes/', views.saved_notes, name='saved_notes'),
    path('edit/<int:note_id>/', views.edit_note, name='edit_note'),
    path('delete/<int:note_id>/', views.delete_note, name='delete_note'),
] 

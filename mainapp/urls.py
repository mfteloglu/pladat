from django.urls import path, include

from . import views

urlpatterns = [
    path('landing/', views.landing, name='landing'),
    #path('employer/', views.employer, name='employer'),
    path('setting-student/', views.settings_student, name='settings_student'),
    path('settings-employer/', views.settings_employer, name='settings_employer'),
    path('see-details/<int:jobid>/', views.see_details, name='see_details'),
    path('profile/<int:userid>/', views.view_self_profile, name='view_self_profile'), # returns employer and student profile
    path('<int:userid>/add/', views.add_job, name='add_job'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name = 'index'),
]

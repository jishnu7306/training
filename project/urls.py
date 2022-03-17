from django.contrib import admin
from django.urls import path
from Training import views

urlpatterns = [
    path('admin/', admin.site.urls),



    path('manager_Dashboard/', views.manager_Dashboard, name='manager_Dashboard'),
    path('manager_categories/', views.manager_categories, name='manager_categories'),
    path('manager_emp_categories/', views.manager_emp_categories, name='manager_emp_categories'),
    path('manager_course/', views.manager_course, name='manager_course'),
    path('manager_emp_course_list/', views.manager_emp_course_list,name='manager_emp_course_list'),
    path('manager_emp_course_details/', views.manager_emp_course_details,name='manager_emp_course_details'),
    path('manager_emp_profile/', views.manager_emp_profile,name='manager_emp_profile'),
    path('manager_emp_attendance/', views.manager_emp_attendance,name='manager_emp_attendance'),
    path('manager_emp_attendance_show/', views.manager_emp_attendance_show,name='manager_emp_attendance_show'),
    path('manager_task/', views.manager_task, name='manager_task'),
    path('manager_givetask/', views.manager_givetask, name='manager_givetask'),
    path('manager_current_task/', views.manager_current_task,name='manager_current_task'),
    path('manager_previous_task/', views.manager_previous_task,name='manager_previous_task'),
    path('manager_registration_details/', views.manager_registration_details,name='manager_registration_details'),
    path('manager_attendance/', views.manager_attendance,name='manager_attendance'),
    path('manager_attendance_show/', views.manager_attendance_show,name='manager_attendance_show'),
    path('manager_reported_issues/', views.manager_reported_issues,name='manager_reported_issues'),
    path('manager_issues/', views.manager_issues, name='manager_issues'),
    path('manager_issues_form/', views.manager_issues_form,name='manager_issues_form'),
    path('manager_myissues/', views.manager_myissues, name='manager_myissues'),
    path('manager_reported_detail/', views.manager_reported_detail,name='manager_reported_detail'),
    path('manager_reported_issue_show/', views.manager_reported_issue_show,name='manager_reported_issue_show'),
]

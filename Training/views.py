from django.shortcuts import render

# Create your views here.


def manager_Dashboard(request):
    return render(request,'manager\manager_Dashboard.html')

def manager_categories(request):
    return render(request,'manager\manager_categories.html') 

def manager_emp_categories(request):
    return render(request,'manager\manager_emp_categories.html')   

def manager_course(request):
    return render(request,'manager\manager_course.html')

def manager_emp_course_list(request):
    return render(request,'manager\manager_emp_course_list.html')

def manager_emp_course_details(request):
    return render(request,'manager\manager_emp_course_details.html')

def manager_emp_profile(request):
    return render(request,'manager\manager_emp_profile.html')

def manager_emp_involved_projects(request):
    return render(request,'manager\manager_emp_involved_projects.html')
    
def manager_emp_attendance(request):
    return render(request,'manager\manager_emp_attendance.html')

def manager_emp_attendance_show(request):
    return render(request,'manager\manager_emp_attendance_show.html')

def manager_task(request):
    return render(request,'manager\manager_task.html')

def manager_givetask(request):
    return render(request,'manager\manager_givetask.html')

def manager_current_task(request):
    return render(request,'manager\manager_current_task.html')

def manager_previous_task(request):
    return render(request,'manager\manager_previous_task.html')

def manager_registration_details(request):
    return render(request,'manager\manager_registration_details.html')  

def manager_attendance(request):
    return render(request,'manager\manager_attendance.html') 

def manager_attendance_show(request):
    return render(request,'manager\manager_attendance_show.html')

def manager_reported_issues(request):
    return render(request,'manager\manager_reported_issues.html') 

def manager_issues(request):
    return render(request,'manager\manager_issues.html')

def manager_issues_form(request):
    return render(request,'manager\manager_issues_form.html')

def manager_myissues(request):
    return render(request,'manager\manager_myissues.html')

def manager_reported_detail(request):
    return render(request,'manager\manager_reported_detail.html')

def manager_reported_issue_show(request):
    return render(request,'manager\manager_reported_issue_show.html')

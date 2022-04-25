from django.shortcuts import render

# Create your views here.

from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from .models import *
from human_resource.swig import example

def index(request):
    return render(request, 'human_resource/index.html')

def staff_money(request):
    sum_money = 0.0
    avg_money = 0.0
    employee_count = 0

    sum_money_frontend = 0.0
    avg_money_frontend = 0.0
    frontend_count = 0

    sum_money_backend = 0.0
    avg_money_backend = 0.0
    backend_count = 0

    sum_money_fullstack = 0.0
    avg_money_fullstack = 0.0
    fullstack_count = 0

    staffs = Staff.objects.all()

    for staff in staffs:
        sum_money += float(staff.salary)
        employee_count += 1

        if (staff.position == "Frontend Developer"):
            frontend_count += 1
            sum_money_frontend += float(staff.salary)
        elif (staff.position == "Backend Developer"):
            backend_count += 1
            sum_money_backend += float(staff.salary)
        elif (staff.position == "Fullstack Developer"):
            fullstack_count += 1
            sum_money_fullstack += float(staff.salary)
    
    if employee_count > 0:
        avg_money = round(sum_money/employee_count, 2)
    if frontend_count > 0:
        avg_money_frontend = round(sum_money_frontend/frontend_count, 2)
    if backend_count > 0:
        avg_money_backend = round(sum_money_backend/backend_count, 2)
    if fullstack_count > 0:
        avg_money_fullstack = round(sum_money_fullstack/fullstack_count, 2)

    context = {
        'sum_money': sum_money,
        'avg_money': avg_money,
        'employee_count': employee_count,

        'sum_money_frontend': sum_money_frontend,
        'avg_money_frontend': avg_money_frontend,
        'frontend_count': frontend_count,

        'sum_money_backend': sum_money_backend,
        'avg_money_backend': avg_money_backend,
        'backend_count': backend_count,

        'sum_money_fullstack': sum_money_fullstack,
        'avg_money_fullstack': avg_money_fullstack,
        'fullstack_count': fullstack_count,
    }

    return render(request, 'human_resource/staff_money.html', context)


def squad_money(request):
    squad_budget = []
    squads = Squad.objects.all()
    for squad in squads:
        squad_budget.append([squad.name, squad.budget()])

    context = {
        'squad_budget': squad_budget,
    }

    return render(request, 'human_resource/squad_money.html', context)


def project_money(request):
    project_budget = []
    projects = Project.objects.all()
    for project in projects:
        budget = 0.0
        for squad in project.squad_set.all():
            budget += squad.budget()
        project_budget.append([project.name, budget])
    
    context = {
        'project_budget': project_budget,
    }

    return render(request, 'human_resource/project_money.html', context)

def available_hr(request):
    staff_freetime = []

    staffs = Staff.objects.all()
    

    for staff in staffs:
        if (staff.total_load() < 1):
            staff_freetime.append([staff.name, round(example.freetime(staff.total_load()), 2)])
    
    free_squad_name = []
    squads = Squad.objects.all()
    for squad in squads:
        if (squad.project.end_date > timezone.now()):
            free_squad_name.append(squad.name)

    context = {
        'staff_freetime': staff_freetime,
        'free_squad_name': free_squad_name,
    }
    
    return render(request, 'human_resource/available_hr.html', context)

def project_timeline(request):
    project_date = []

    projects = Project.objects.all()
    for project in projects:
        project_date.append([project.name, project.start_date, project.end_date])
    
    context = {
        'project_date': project_date,
    }
                
    return render(request, 'human_resource/project_timeline.html', context)
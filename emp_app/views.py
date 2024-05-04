from django.shortcuts import render
from .models import Employee,Department,Role
from datetime import datetime
from django.http import HttpResponse
from django.db.models import Q

def index(request):
    return render(request,'index.html')

def all_emp(request):
    emp = Employee.objects.all()
    print(emp)
    return render(request,'view_all_emp.html',{'emp':emp})

def add_emp(request):
    print('add emp called')
    if request.method == 'POST':
        print('Post called')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        dept = request.POST['dept']
        role = request.POST['role']
        bonus = request.POST['bonus']
        phone = request.POST['phone']
        print(first_name,last_name,salary,dept,role)
        new_emp = Employee(first_name=first_name,phone=phone,last_name=last_name,salary=salary,bonus=bonus,dept_id=dept,role_id=role,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse('Data saved')
    else:
        return render(request,'add_emp.html')

def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse('Employee Removed successfullly')
        except:
            return HttpResponse('Please Enter A valid Employee id')
    emp = Employee.objects.all()

    return render(request,'remove_emp.html',{'emp':emp})

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emp = Employee.objects.all()
        if name:
            emps = emp.filter(Q(first_name__icontains == name) | Q(last_name__icontains == name) )
        if dept:
            emps = emp.filter(dept__name = dept )
        if role:
            emps = emp.filter(role__name = role)
        return render(request,'view_all_emp.html',{'emp':emps})
    elif request.method == 'GET':
        return render(request,'filter_emp.html')
    else:
        return HttpResponse('An Exception Occured')
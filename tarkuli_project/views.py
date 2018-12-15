# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .models import userModel



def login(request):
    if 'e' in request.session: 
        e = request.session['e']
        return redirect('tarkuli_project:user_view')

    elif request.method == "POST":
        e = request.POST['email']
        p = request.POST['password']

        if (len(userModel.objects.filter(email=e)) and len(userModel.objects.filter(password=p))):
            request.session['e'] = e 
            # return render(request, 'tarkuli_project/user_view.html')
            return redirect('tarkuli_project:user_view')
    return render(request, 'tarkuli_project/login.html')


def manager(request):
	user_detail = userModel.objects.all()

	context = {
		'user_detail':user_detail,
		}
	return render(request,'tarkuli_project/manager.html',context)


def supervisor(request):
	user_detail = userModel.objects.filter(Location__in=['Delhi','Gurgaon'] )
	print(user_detail)

	context = {
		'user_detail':user_detail,
		}
	return render(request,'tarkuli_project/supervisor.html',context)



def supervisor2(request):
	user_detail = userModel.objects.filter(Location__in=['Jaipur','Kota'] )

	context = {
		'user_detail':user_detail,
		}
	return render(request,'tarkuli_project/supervisor2.html',context)

def employee(request):
	user_detail = userModel.objects.filter(Location='Delhi' )

	context = {
		'user_detail':user_detail,
		}
	return render(request,'tarkuli_project/employee.html',context)


def user_view(request):

	return render(request,'tarkuli_project/user_view.html')


def manager_view(request,y):
	user_view=userModel.objects.get(id=y)

	return render(request,'tarkuli_project/manager_view.html',{'detail':user_view})


	
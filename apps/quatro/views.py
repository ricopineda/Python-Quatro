from __future__ import unicode_literals
from models import *
from django.shortcuts import render
import random
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.contrib import messages
from django.utils.crypto import get_random_string
# the index function is called when root is visited
def index(request):

	return render(request,'quatro/index.html')

def register(request):
    if request.method == "POST":
    	
    	name = request.POST['name']
    	alias = request.POST['alias']
    	email = request.POST['email']
    	dob = request.POST['dob']
    	password = request.POST['password']

        errors = User.objects.validator(request.POST)

        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request,error, extra_tags=tag)
            return redirect('/')
        else:
            users = User.objects.filter(email=request.POST['email'])
            if len(users):
                messages.error(request,"This email is already in use!")
                return redirect('/')
            else:
				users = User.objects.create(name=name, alias=alias, email=email, password=password, dob=dob)
				request.session['id'] = users.id
				# User.objects.get(id=request.session['id']).friends.add(User.objects.get(id=request.session['id']))
				return redirect('/home')
    else:
        return redirect('/')


def login(request):
	if request.method == "POST":
		email = request.POST['email']
		password = request.POST['password']
		user = User.objects.all().filter(email=email)
		if len(user):
			if user[0].password == password:
				request.session['id'] = user[0].id
				return redirect('/home')
			else:
				messages.error(request,"Failed to validate password!")
				return redirect('/')
		else:
			messages.error(request,"Failed to find Username in Database...")
			return redirect ('/')   
	else:
		return redirect ('/')  	

def logout(request):

	request.session['id'] = 0
	return redirect('/')

def home(request):

	context = {
	'friends': User.objects.get(id=request.session['id']).friends.all(),
	'user': User.objects.get(id=request.session['id']),
	'users': User.objects.exclude(id=request.session['id']),
	}

	return render(request, 'quatro/home.html', context)

def add(request, id):

	User.objects.get(id=id).friends.add(User.objects.get(id=request.session['id']))

	return redirect('/home')

def profile(request, id):

	context ={
	'user': User.objects.get(id=id)
	}

	return render(request, 'quatro/profile.html', context)

def remove(request, id):

	User.objects.get(id=id).friends.remove(User.objects.get(id=request.session['id']))

	return redirect('/home')


















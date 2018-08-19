# Required Imported Libraries
# ===========================
from django.shortcuts import render, HttpResponse, redirect
from django,utils.crypto import get_random_string
from django.contrib import messages
from time import gmtime, strftime
from models import *


# Custom Views
# ============
def index(request):
    context = {
        "email" : "blog@gmail.com",
        "name" : "mike"
    }
    return render(request, "ourApp/index.html", context)

def index( req ):
    res = strftime('%Y-%M-%D %H:%M:%S', gmtime())
    print (get_random_string(length=14))
    return render(req, 'time_display/index.html', { 'blogs': Blog.objects.all() })

def new( req ):
    # res = 'This page still under development..!'
    return render(req, 'time_display/new.html', )
    
def update( req, update):
    error = Blog.objects.basic_validator( req.POST)
    if len(erro): 
        for tag, err in errors.iteritems():
    return render(req, 'time_display/update.html', )

def show( req, id ):
    return render(req, 'time_display/show.html', {'time_display': Blog.objects.get( id = id ) })

def edit( req, id ):
    return render(req, 'time_display/edit.html', {'time_display': Blog.objects.get( id = id ) })

def destroy( req ):
    return redirect( '/' )


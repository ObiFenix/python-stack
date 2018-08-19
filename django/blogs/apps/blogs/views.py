# Required Imported Libraries
# ===========================
from django.shortcuts import render, HttpResponse, redirect


# Custom Views
# ============
def index( req ):
    res = 'Placeholder to later display all the list of blogs.'
    return HttpResponse( res )

def new( req ):
    res = 'placeholder to display a new form to create a new blog.'
    return HttpResponse( res )
    
def create( req ):
    return redirect( '/' )

def show( req ):
    res = 'placeholder to display blog {{number}}.'
    return HttpResponse( res )

def edit( req ):
    res = 'placeholder to display blog {{number}}.'
    return HttpResponse( res )

def destroy( req ):
    return redirect( '/' )

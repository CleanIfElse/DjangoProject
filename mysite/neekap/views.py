from django.shortcuts import render_to_response, get_object_or_404, render
from neekap.models import Blog, Category
import datetime
# Create your views here.

def index(request):
	today = datetime.datetime.now().date()
	# Blog = get_object_or_404(Blog)
	blog = Blog.objects.all()
	return render(request, 'neekap/index.html', {'blog': blog,})

def team(request):
	today = datetime.datetime.now().date()
	# blog object
	blog = Blog.objects.all()
	return render(request, 'neekap/team.html', {'blog': blog,})

# this function will allow user to view post
# def view_post(request):



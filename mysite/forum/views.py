from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import login, authenticate, update_session_auth_hash
from forum.forms import RegistrationForm, PostForm, EditProfileForm
from django.views import generic
from . import models
from forum.models import WebsitePost, AssignmentPost, SurvivingPost, LectureSlidesPost, ChartsPost, BinaryPost
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm

def home(request):
	website_posts = WebsitePost.objects.all().order_by('-date')
	assignment_posts = AssignmentPost.objects.all().order_by('-date')
	surviving_posts = SurvivingPost.objects.all().order_by('-date')
	slides_posts = LectureSlidesPost.objects.all().order_by('-date')
	charts_posts = ChartsPost.objects.all().order_by('-date')
	binary_posts = BinaryPost.objects.all().order_by('-date')
	
	args = {'website_posts': website_posts, 
			'assignment_posts': assignment_posts,
			'surviving_posts': surviving_posts,
			'slides_posts': slides_posts,
			'charts_posts': charts_posts,
			'binary_posts': binary_posts,
			}
			
	return render(request, 'forum/home.html', args)
	
def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/forum')
		else:
			return redirect('/forum/reg_error')
	else:
		form = RegistrationForm()

	return render(request, 'forum/reg_form.html')
	
def registerError(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/forum')
	else:
		form = RegistrationForm()

	return render(request, 'forum/reg_error.html')

def addWebsitePost(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		
		if form.is_valid():
			author = request.user
			title = form.cleaned_data['title']
			body = form.cleaned_data['body']
			
			post = WebsitePost.objects.create(
							title = title,
							author = author,
							body = body)
			return redirect('/forum')
			
	return render(request, 'forum/addPost.html')
	
def addAssignmentPost(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		
		if form.is_valid():
			author = request.user
			title = form.cleaned_data['title']
			body = form.cleaned_data['body']
			
			post = AssignmentPost.objects.create(
							title = title,
							author = author,
							body = body)
			return redirect('/forum')
			
	return render(request, 'forum/addPost.html')
	
def addSurvivingPost(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		
		if form.is_valid():
			author = request.user
			title = form.cleaned_data['title']
			body = form.cleaned_data['body']
			
			post = SurvivingPost.objects.create(
							title = title,
							author = author,
							body = body)
			return redirect('/forum')
			
	return render(request, 'forum/addPost.html')
	
def addLectureSlidesPost(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		
		if form.is_valid():
			author = request.user
			title = form.cleaned_data['title']
			body = form.cleaned_data['body']
			
			post = LectureSlidesPost.objects.create(
							title = title,
							author = author,
							body = body)
			return redirect('/forum')
			
	return render(request, 'forum/addPost.html')
	
def addChartsPost(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		
		if form.is_valid():
			author = request.user
			title = form.cleaned_data['title']
			body = form.cleaned_data['body']
			
			post = ChartsPost.objects.create(
							title = title,
							author = author,
							body = body)
			return redirect('/forum')
			
	return render(request, 'forum/addPost.html')

def addBinaryPost(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		
		if form.is_valid():
			author = request.user
			title = form.cleaned_data['title']
			body = form.cleaned_data['body']
			
			post = BinaryPost.objects.create(
							title = title,
							author = author,
							body = body)
			return redirect('/forum')
			
	return render(request, 'forum/addPost.html')

def viewProfile(request):
	args = {'user': request.user}
	return render(request, 'forum/profile.html', args)
	
def editProfile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance = request.user)
		
		if form.is_valid():
			form.save()
			return redirect('/forum/profile')
			
	else:
		form = EditProfileForm(instance = request.user)
		args = {'form': form}
		return render(request, 'forum/editProfile.html', args)
		
def changePassword(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user = request.user)
		
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('/forum/profile')
			
		else:
			return redirect('/forum/profile/changePassword')
			
	else:
		form = PasswordChangeForm(user = request.user)
		args = {'form': form}
		return render(request, 'forum/changePassword.html', args)

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from app.models import Category, Item, UserProfile
from app.forms import CategoryForm, ItemForm, UserForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.models import User


def encode_url(str):
	return str.replace(' ', '_')
	
def decode_url(str):
	return str.replace('_', ' ')

def save_files(f):	
	destination = open('document_root', 'wb+')
	for chunk in f.chunks():
		destination.write(chunk)
	destination.close()


def index(request):
	context = RequestContext(request)
		
	list_category = Category.objects.order_by('-likes')[:5]
	context_dict = {"categories": list_category}
	
	for category in list_category:
		category.url = encode_url(category.name)
		
	return render_to_response('app/index.html', context_dict, context)


def about(request):
	context = RequestContext(request)
	
	return render_to_response('app/about.html', context)


def category(request, url_category_name):
	context = RequestContext(request)
	
	cat_name = decode_url(url_category_name)
	
	context_dict = {'cat_name': cat_name, 'url_category_name':url_category_name}
	
	try:		
		category = Category.objects.get(name=cat_name)
		
		items = Item.objects.filter(category=category).order_by('-views')
		
		context_dict['items'] = items
		
		context_dict['category'] = category
		
	except Category.DoesNotExit:
		pass
	
	return render_to_response('app/category.html', context_dict, context)
	
@login_required
def add_category(request):
	context = RequestContext(request)
	
	if request.method == 'POST':
		form = CategoryForm(request.POST, request.FILES)				
		
		if form.is_valid() and form.is_multipart():
			save_files(request.FILES['image'])
			form.save(commit=True)
															
			return index(request)
		else:
			print form.errors
			
	else:
		form = CategoryForm()
		
	return render_to_response('app/add_category.html', {'form': form}, context)

@login_required	
def add_item(request, url_category_name):
	context = RequestContext(request)
	
	cat_name = decode_url(url_category_name)
	if request.method == 'POST':
		form = ItemForm(request.POST, request.FILES)
		
		if form.is_valid() and form.is_multipart():
			save_files(request.FILES['photos'])
			item = form.save(commit=False)
			
			cat = Category.objects.get(name=cat_name)
			item.category = cat
			
			item.views = 0			
			item.likes = 0
			
			item.save()
			
			return category(request, url_category_name)
		else:
			print form.errors
	else:
		form = ItemForm()
		
	return render_to_response('app/add_item.html', {'url_category_name':url_category_name, 'cat_name':cat_name, 'form':form}, context)
	
	
def register(request):
	context = RequestContext(request)
	
	registered = False
	
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(request.POST, request.FILES)
		
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			
			user.set_password(user.password)
			user.save()
			
			profile = profile_form.save(commit=False)
			profile.user = user
			
			if profile_form.is_multipart():
				picture = save_files(request.FILES['picture'])
				
			profile.save()
			
			registered = True
			
		else:
			print user_form.errors, profile_form.errors
	
	else:
		user_form =UserForm()
		profile_form = UserProfileForm()
	
	return render_to_response('app/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}, context)
					
	
def user_login(request):
	context = RequestContext(request)
	context_dict = {}
	
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		
		user = authenticate(username=username, password=password)
		
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/app/')
			else:
				context_dict['disabled_account'] = True
				return render_to_response('app/login.html', context_dict, context)
		else:
			print "Incorrect login details: {0}, {1}".format(username, password)
			context_dict['bad_details'] = True
			return render_to_response('app/login.html', context_dict, context)
			
	else:
		return render_to_response('app/login.html', context_dict, context)

@login_required
def user_logout(request):
	logout(request)
	
	return HttpResponseRedirect('/app/')	


@login_required
def profile(request):
	context = RequestContext(request)
	u = User.objects.get(username=request.user)
	
	up = UserProfile.objects.get(user=u)
		
	
	context_dict = {'user': u, 'userprofile': up}
	
	return render_to_response('app/profile.html', context_dict, context)
	

def track_url(request):
	context = RequestContext(request)
	item_id = None
	url = '/app/category/Books/'
	if request.method == 'GET':
		if 'item_id' in request.GET:
			item_id = request.GET['item_id']
			try:
				item = Item.objects.get(id=item_id)
				item.views = item.views + 1
				item.save()
				url = item.url
			except:
				pass
				
		return redirect(url)
	
@login_required
def like_category(request):
	context = RequestContext(request)
	id_cat = None
	
	if request.method == 'GET':
		id_cat = request.GET['category_id']
		
	likes = 0
	if id_cat:
		category = Category.objects.get(id=int(id_cat))	
		if category:
			likes = category.likes + 1
			category.likes = likes
			category.save()
			
	return HttpResponse(likes)































	
	
			

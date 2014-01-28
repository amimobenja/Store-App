def register(request):
	context = RequestContext(request)
	
	registered = False
	
	if request.method == 'POST':
		user_form = UserForm(request.POST, request.FILES)
		profile_form = UserProfileForm(request.POST, request.FILES)
		
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			
			user.set_password(user.password)
			user.save()
			
			profile = profile_form.save(commit=False)
			profile.user = user
			
			if profile_form.is_valid() and profile_form.is_multipart():
				save_files(request.FILES['picture'])		
				profile_form.save(commit=True)
				
				registered = True
				return index(request)
				
				else:
					print user_form.errors, profile_form.errors
		else:
			user_form = UserForm()
			profile_form = UserProfileForm()
			
		return render_to_response('app/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}, context)
				
	
	

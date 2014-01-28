from django import forms
from django.contrib.auth.models import User
from app.models import Category, Item, UserProfile

class CategoryForm(forms.ModelForm):
	name = forms.CharField(max_length=128, help_text="Enter Category name")
	description = forms.CharField(widget=forms.Textarea, help_text="Briefly Describe the Category")
	likes = forms.IntegerField(widget=forms.HiddenInput, initial=0, required=False)
	image = forms.ImageField(help_text="Select a Category image to upload.")
	
	class Meta:
		model = Category
		
		
class ItemForm(forms.ModelForm):
	item_name = forms.CharField(max_length=128, help_text="Enter Item name")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	item_description = forms.CharField(widget=forms.Textarea, help_text="Briefly Describe the Category")
	price = forms.CharField(max_length=128, help_text="Set the Price")
	photos = forms.ImageField(help_text="Select a Item image to upload.")
	address = forms.CharField(widget=forms.Textarea, help_text="Enter your Address")
	shops_info = forms.CharField(widget=forms.Textarea, help_text="Briefly Describe the Shop Info")
	
	class Meta:
		model = Item
		
		fields = ('item_name', 'item_description', 'price', 'photos', 'address', 'shops_info')
	
class UserForm(forms.ModelForm):
	username = forms.CharField(help_text="Please enter a username.")
	email = forms.CharField(help_text="Please enter your email.")
	password = forms.CharField(widget=forms.PasswordInput(), help_text="Please enter a password.")

	class Meta:
		model = User
		fields = ['username', 'email', 'password']
		
class UserProfileForm(forms.ModelForm):
	website = forms.URLField(help_text="Please enter your website.")
	picture = forms.ImageField(help_text="Select a profile image to upload.")
	
	class Meta:
		model = UserProfile
		fields = ['website', 'picture']

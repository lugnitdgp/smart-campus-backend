from django.shortcuts import render
from django.contrib.auth import get_user_model

#Django sucks here, Need to import the custom User model explicitly, default is auth.User
User = get_user_model()

# Create your views here.

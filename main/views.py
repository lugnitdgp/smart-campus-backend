from django.shortcuts import render
from django.contrib.auth import get_user_model

#Django sucks here, Need to import the custom User model explicitly, even though u updated th settings
User = get_user_model()

# Create your views here.

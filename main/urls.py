from django.urls import include, path
from rest_framework import routers
from main import views


#AppName 
app_name = 'main'

router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = router.urls

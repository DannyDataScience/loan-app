from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('bankAPI', views.ApprovalsView)
urlpatterns = [
    path('api/', include(router.urls)),
    path('status/', views.approvereject),
    path('', views.cxcontact, name='cxform'), 
    path('about/', views.about_view, name='about'),  
] 
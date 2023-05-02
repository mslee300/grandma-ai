from django.contrib import admin
from django.urls import path, include
from grandmaai.views import base_views

urlpatterns = [
    path('', base_views.index, name='index'),  # '/' 에 해당되는 path
    path('admin/', admin.site.urls),
    path('grandmaai/', include('grandmaai.urls')),
    path('common/', include('common.urls')),
    path("", include("allauth.urls")), #most important
    path('social/signup/', base_views.signup_redirect, name='signup_redirect')
]

"""cdal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

def custom_500(request):
    response = render(request, "500.html")
    response.status_code = 500
    return response

def custom_404(request):
   response = render(request, "404.html")
   response.status_code = 404
   return response

def custom_400(request):
   response = render(request, "400.html")
   response.status_code = 400
   return response

def custom_403(request):
    response = render(request, "403.html")
    response.status_code = 403
    return response

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('web.urls'))
]

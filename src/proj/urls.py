"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('genres/', include('genre.urls', namespace='genres')),
    path('books/', include('books.urls', namespace='books')),
<<<<<<< HEAD
    path('profiles/', include('profiles.urls', namespace='profiles')),
]
#  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
    # path('home/', HomePageView.as_view(), name='home'),
] 
>>>>>>> d617068c5c63c1af1731dac8571c873c2176b6b1

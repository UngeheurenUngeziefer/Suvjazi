"""Suvjazi_project URL Configuration
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
from django.urls import path
from Suvjazi_app import views as Suvjazi_app_views
# media
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Suvjazi_app_views.index, name='index'),
    path('person/<slug:slug>/', Suvjazi_app_views.person_detail, name='person_detail'),
    path('institute/<slug:slug>/', Suvjazi_app_views.institute_detail, name='institute_detail'),
    path('all_persons', Suvjazi_app_views.all_persons, name='all_persons'),
] 

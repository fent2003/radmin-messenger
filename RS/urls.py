from django.contrib import admin
from django.urls import include, path
from messenger import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index.as_view(), name='index'),
    path('accounts/', include('Users.urls'))
]

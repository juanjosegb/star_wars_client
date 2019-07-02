from django.urls import path, include
from base.views import base, create_user

urlpatterns = [
    path('', base.Index.as_view(), name='index'),
    path('create_user/', create_user.CustomUserAdmin.as_view(), name='create_user'),
    path('accounts/', include('django.contrib.auth.urls'))
]

from django.urls import path, include
from . import views
#from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('login/addatrail', views.addatrail, name='addatrail'),
    

]


#path('password_reset', PasswordResetView.as_view(), name='password_reset'),
#path('password_reset/done', PasswordResetDoneView.as_view(), name='password_reset_done')

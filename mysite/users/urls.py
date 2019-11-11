from django.conf.urls import url
#from django.urls import path
from . import views
urlpatterns=[
    url('login/',views.login, name='login'),
    url('profile/',views.profile, name='profile'),
    url('updateprofile/<int:id>/',views.editprofile, name='update_profile'),
    url('signup/',views.signup, name='signup'),
    url('logout/',views.logout, name='logout'),
    url('mail/',views.mymail, name='mail'),
    url('updateuser/<int:id>/',views.update_user, name='updateuser'),
    url('files/',views.file_show, name='files'),

]
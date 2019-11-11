from django.conf.urls import url
#from django.urls import path
from . import views
urlpatterns = [

    url('',views.show_posts, name='add-posts'),

]
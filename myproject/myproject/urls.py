"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import re_path
#django版本较高不能识别出path里的正则表达式 需改成path才可以识别正则表达式

import boards.views as views
import accounts.views as accounts_view

#def url(regex, view, kwargs=None, name=None):
urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    re_path(r'signup/',accounts_view.signup,name='signup'),
    re_path(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    re_path('home/',views.home,name='home'),
    re_path('admin/', admin.site.urls),

    #path(r'^(?P<username>[\w.@+-]+)/$', views.user_profile, name='user_profile'),

]

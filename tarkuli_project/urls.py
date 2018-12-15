from django.conf.urls import url
from tarkuli_project import views
from django.contrib.auth import views as auth_view




urlpatterns = [
    
    url(r'^login/$', views.login, name='login'),    
    url(r'^logout/$', auth_view.logout, name="logout"),
    url(r'^manager/$', views.manager, name="manager"),
    url(r'^supervisor/$', views.supervisor, name="supervisor"),
    url(r'^supervisor2/$', views.supervisor2, name="supervisor2"),
    url(r'^employee/$', views.employee, name="employee"),
    url(r'^user_view/$', views.user_view, name="user_view"),

    url(r'^manager_view/(?P<y>\d+)/$', views.manager_view, name="manager_view"),
    ]

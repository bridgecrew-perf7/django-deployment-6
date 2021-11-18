from django.conf.urls import url
from school_app import views

app_name = 'basic_app'

urlpatterns = [
    url(r'^user_login',views.user_login,name='user_login'),
    url(r'^user_register',views.user_register,name='user_register'),
    url(r'^success',views.Success,name='success'),
    url(r'^user_logout',views.user_logout,name='user_logout'),
    url(r'^list',views.SchoolListView.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$',views.SchoolDetailView.as_view(),name='detail'),
    url(r'^create',views.SchoolCreateView.as_view(),name='create'),
    url(r'^stu_cre',views.StudentCreateView.as_view(),name='stu_cre'),
    url(r'^thank',views.ThankPage.as_view(),name='thank'),
    url(r'^update/(?P<pk>\d+)/$',views.SchoolUpdateView.as_view(),name='update'),
    url(r'^stu_update/(?P<pk>\d+)/$',views.StudentUpdateView.as_view(),name='stu_update'),
    url(r'^delete',views.DeletePage.as_view(),name='delete'),
    url(r'^contact',views.ContactPage.as_view(),name='contact'),
    url(r'^about',views.AboutPage.as_view(),name='about'),
   
]
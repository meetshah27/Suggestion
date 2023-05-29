from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.decorators.csrf import csrf_exempt
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('', views.index,name="home"),
    path('askquestions/', views.askquestions,name="askquestions"),
    path('myanswers/', views.showmyquestions,name="myanswers"),
    path('admin/', views.index2,name="home2"),
    path('askquestions2/', views.askquestions2,name="askquestions2"),
    path('myanswers2/', views.myanswers2,name="myanswers2"),
    path('reviewmanager/', views.reviewmanager,name="reviewmanager"),
    path('reviewemployee/', views.reviewemployee,name="reviewemployee"),
    path('manager/', views.index3,name="home3"),
    path('askquestions2/', views.askquestions3,name="askquestions3"),
    path('myanswers3/', views.myanswers3,name="myanswers3"),
    path('sharethoughts/', views.reviewmanager,name="sharethoughts"),
    path('solveissues/', views.reviewemployee,name="solveissues"),
    path('askquestions/addq/', views.addq, name="addquestion"),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]

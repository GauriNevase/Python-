# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.sos,),
#     path('sos', views.sos_details)
# ]
from django.urls import path
from myapp import views

urlpatterns = [
    path('sos/', views.sos_form_view,name='sos'),
]
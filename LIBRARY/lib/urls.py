from django.urls import path

from lib import views

"""
Here Default path(' ') is associated with index function of views.py
Other paths have URL parameters to store values for navigating the desired page
"""    

urlpatterns  = [
    path('',views.index),
    path('auth/<page>/',views.auth),
    path('<page>/<operation>/<int:id>',views.actionId),
    path('<page>/',views.actionId),

]
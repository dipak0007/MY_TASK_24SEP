from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('',my_form_view,name='my_form_view'),
    path('readdata/',My_read_view,name='My_read_view'),
    path('edit_get/<int:pk>',edit_get_data,name = 'edit_get_data'),
    path('update/<int:pk>',update_my_data,name='update_my_data'),

    path('delete/<int:pk>/',delete_view,name='delete_view'),
]
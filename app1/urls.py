from django.urls import path

from app1 import views

urlpatterns=[
    path('',views.attandance1,name='attandance'),
    path('add_attandance1',views.add_attandance1, name='add_attandance1'),
    path('view_attandance1', views.view_attandance1, name='view_attandance1'),
    path('update_attandance1/<int:id>/', views.update_attandance1, name='update_attandance1'),
    path('delete_attandance1/<int:id>/', views.delete_attandance1, name='delete_attandance1'),
]
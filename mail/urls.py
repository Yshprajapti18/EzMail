from django.urls import path
from . import views


urlpatterns = [
    path("",views.inbox),
    path("send/",views.send),
    path('delete/<int:id>',views.delete)
]
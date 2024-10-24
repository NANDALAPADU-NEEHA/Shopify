from django.urls import path
from customers import views
urlpatterns=[
    path('<int:id>/<str:user1>/<str:product>/<int:cardno>/<int:phoneno>')
]

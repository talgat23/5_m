from django.contrib import admin
from django.urls import path
from users import views
from users.views import RegisterAPIView, ConfirmAPIView, LoginAPIView

# urlpatterns = [
#     path('users/registration/', views.register_api_view),
#     path('users/confirm/', views.confirm_api_view),
#     path('users/authorization/', views.login_api_view),
# ]

urlpatterns = [
    path('users/registration/', RegisterAPIView.as_view()),
    path('users/confirm/', ConfirmAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),
]

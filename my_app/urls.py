from django.urls import path
from . import views

urlpatterns = [
    path('banks/', views.BankList.as_view(), name='bank-list'),
    path('branches/<str:bank_name>/', views.BranchList.as_view(), name='branch-list'),
]
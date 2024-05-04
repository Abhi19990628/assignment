from django.urls import path
from .views import BankList, BranchList,BranchDetail

urlpatterns = [
    path('banks/', BankList.as_view(), name='bank-list'),
    path('branches/', BranchList.as_view(), name='branch-list'),
    path('branches/<str:ifsc>/', BranchDetail.as_view(), name='branch-detail'),
]
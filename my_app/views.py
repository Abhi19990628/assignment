from django.shortcuts import render
from rest_framework import generics
from .models import Bank, Branch
from .serializers import BankSerializer, BranchSerializer

class BankList(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class BranchList(generics.ListCreateAPIView):
    serializer_class = BranchSerializer

    def get_queryset(self):
        bank_name = self.kwargs['bank_name'] 
        return Branch.objects.filter(bank__name__icontains=bank_name)
    
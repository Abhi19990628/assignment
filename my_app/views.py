from rest_framework import generics
from .models import Bank, Branch
from .serializers import BankSerializer, BranchSerializer
from rest_framework.response import Response
from rest_framework import status


class BankList(generics.ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class BranchList(generics.ListAPIView):
    serializer_class = BranchSerializer

    def get_queryset(self):
        ifsc = self.request.query_params.get('ifsc')
        if ifsc:
            return Branch.objects.filter(ifsc=ifsc)
        else:
            return Branch.objects.all()
        
class BranchDetail(generics.RetrieveAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    lookup_field = 'ifsc'
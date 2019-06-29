from rest_framework import generics, status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from bank_search_application.bank_search_api.models import Banks, Branches
from bank_search_application.bank_search_api.serializers import BranchSerializer


class BankGetView(generics.RetrieveAPIView):

    queryset = Branches.objects.all()
    serializer_class = BranchSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = LimitOffsetPagination

    def get(self, request, *args, **kwargs):
        try:
            application_data = self.queryset.get(ifsc=kwargs['ifsc'])
            branch_details = BranchSerializer(application_data).data
            bank_details = branch_details['bank_details']
            data = {'bank_details': bank_details}
            return Response(
                data=data,
                status=status.HTTP_200_OK
            )

        except Exception as exception:
            return Response(
                data="Ifsc code Not found"+str(exception),
                status=status.HTTP_404_NOT_FOUND
            )


class BranchListView(generics.RetrieveAPIView):

    queryset = Branches.objects.all()
    serializer_class = BranchSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = LimitOffsetPagination

    def get(self, request, *args, **kwargs):
        try:
            bank = Banks.objects.get(name=request.GET['bank_name'])
            application_data = list(self.queryset.filter(bank=bank.id, city=request.GET['city']))
            branch_list = BranchSerializer(application_data, many=True).data
            return Response(
                data=branch_list,
                status=status.HTTP_200_OK
            )

        except Exception as exception:
            return Response(
                data="Bank and city Not found"+str(exception),
                status=status.HTTP_404_NOT_FOUND
            )


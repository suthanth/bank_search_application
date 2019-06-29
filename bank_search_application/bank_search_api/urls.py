from django.urls import path

from bank_search_application.bank_search_api.views import BankGetView, BranchListView

urlpatterns = [
    path('bankDetails/<str:ifsc>', BankGetView.as_view(), name='get-bank-details-for-ifsc-code'),
    path('branchDetails', BranchListView.as_view(), name='get-branch-details-for-bankName-city'),
]

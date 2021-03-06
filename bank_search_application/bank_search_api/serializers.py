from rest_framework import serializers

from bank_search_application.bank_search_api.models import Banks, Branches


class BankSerializer(serializers.ModelSerializer):

    class Meta:
        model = Banks
        fields = ('id', 'name')


class BranchSerializer(serializers.ModelSerializer):
    bank_details = BankSerializer(read_only=True)

    class Meta:
        model = Branches
        fields = ('ifsc', 'branch', 'address', 'city', 'district', 'state', 'bank', 'bank_details')

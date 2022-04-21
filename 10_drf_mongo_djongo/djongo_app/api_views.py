from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from .models import Account, ShortLink
from .serializers import AccountSerializer, ShortLinkSerializer


class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class ShortLinkViewSet(ModelViewSet):
    serializer_class = ShortLinkSerializer

    def look_up_account(self):

        if account_pk := self.kwargs.get('account_pk'):
            return get_object_or_404(Account, pk=account_pk)
        
        return None

    
    def get_queryset(self):
        return ShortLink.objects.filter(account=self.look_up_account())

    
    def perform_create(self, serializer):
        account = self.look_up_account()
        serializer.validated_data['account'] = account
        super().perform_create(serializer)
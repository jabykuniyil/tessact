from django.shortcuts import render
from .models import UserProfile
from rest_framework.views import APIView
from rest_framework import generics, mixins
from .serializer import UserDataSerializer
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.


class UserMixinView(mixins.ListModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserDataSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            ...
        return


user_mixin_view = UserMixinView.as_view()


class UserDataCreateView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserDataSerializer

    def perform_create(self, serializer):
        user_name = serializer.validated_data.get('user_name')
        email_id = serializer.validated_data.get('email_id')
        first_name = serializer.validated_data.get('first_name')
        last_name = serializer.validated_data.get('last_name')
        password = serializer.validated_data.get('password')

        serializer.save(user_name=user_name, first_name=first_name, last_name=last_name,
                        email_id=email_id, password=make_password(password))

user_create_view = UserDataCreateView.as_view()




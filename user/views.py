from .models import UserProfile
from rest_framework import generics, mixins
from .serializer import UserDataSerializer
from django.contrib.auth.hashers import make_password

# Create your views here.


class UserMixinView(mixins.UpdateModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                    generics.GenericAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserDataSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        password = serializer.validated_data.get('password')
        password = make_password(password)
        serializer.save(password=password)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        snippet = UserProfile.objects.get(id=pk)
        serializer = UserDataSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return self.update(request, *args, **kwargs)


user_mixin_view = UserMixinView.as_view()


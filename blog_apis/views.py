from rest_framework import mixins, generics
from .models import Blog
from .serializer import BlogSerializer
from django.http import Http404

# Create your views here.


class BlogMixinView(mixins.UpdateModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                    generics.GenericAPIView, mixins.DestroyModelMixin):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'

    def get_item(self, pk, author=None):
        try:
            if author:
                return Blog.objects.get(pk=pk, created_by=author)
            return Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        print(pk)
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        author = request.data["created_by"]
        snippet = self.get_item(pk, author=author)
        serializer = BlogSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        snippet = self.get_item(pk)
        snippet.delete()
        return self.destroy(request, *args, **kwargs)


blog_mixin_view = BlogMixinView.as_view()



from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.mixins import RetrieveModelMixin
from .serializers import ArticleSerializer


from blog.models import (User,
                         Article,
                         Editor,
                         Author)

class ArticleRetriveAPIView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer



class ArticleListCreateAPIView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

####Сделал
class ArticleRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
##### Нужно в serialaizer тоже добавить(но незнаю что!!!!!!!)
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Clothes
from .serializers import ClothSerializer, RegisterSerializer
from .pagination import ClothPagination
from rest_framework import generics
from django.contrib.auth.models import User

class ListCreateMovieAPIView(ListCreateAPIView):
    serializer_class = ClothSerializer
    queryset = Clothes.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ClothPagination


    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class RetrieveUpdateDestroyMovieAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ClothSerializer
    queryset = Clothes.objects.all()
    permission_classes = [IsAuthenticated]



class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
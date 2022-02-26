
from rest_framework.views import APIView
from accounts.models import User
from accounts.serializers import AccountSerializer
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import status
from django.db.models import Q

# Create your views here.

class AccountsListView(APIView):
    serializer_class = AccountSerializer
    pagination_class = LimitOffsetPagination

    def get(self,request):
        search_query = request.GET.get('query')
        sort = request.GET.get('sort')
        if search_query:
            users = User.objects.filter(Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query))
        else:
            users = User.objects.all()
        if sort:
            users = users.order_by(sort)
        ser = AccountSerializer(users,many=True)
        return Response(ser.data, status=status.HTTP_200_OK)

    def post(self,request):
        data = request.data
        ser = AccountSerializer(data=data)
        if ser.is_valid():
            ser.save()
        return Response(ser.data, status=status.HTTP_201_CREATED)


class AccountsDetailView(APIView):
    serializer_class = AccountSerializer

    def get(self,request,id):
        users = User.objects.get(id=id)
        ser = AccountSerializer(users)
        return Response(ser.data, status=status.HTTP_200_OK)

    def put(self,request,id):
        user = User.objects.get(id=id)        
        data = request.data
        ser = AccountSerializer(user, data=data)
        if ser.is_valid():
            ser.save()
        return Response(ser.data, status=status.HTTP_201_CREATED)

    def delete(self,request,id):
        user = User.objects.get(id=id)
        user.delete()
        return Response(status=status.HTTP_200_OK)


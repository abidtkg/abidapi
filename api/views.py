from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item, User
from .serilizers import itemSerilizer, userSerializer

@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serialized = itemSerilizer(items, many=True)
    return Response(serialized.data)

@api_view(['POST'])
def setData(request):
    serializer = itemSerilizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serialized = userSerializer(users, many=True)
    return Response(serialized.data)

@api_view(['POST'])
def createUser(request):
    user = userSerializer(data=request.data)
    if user.is_valid():
        user.save()
    return Response(user.data)
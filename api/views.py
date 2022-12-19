from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serilizers import itemSerilizer

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
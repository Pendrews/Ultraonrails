from django.http import JsonResponse
from .models import Test, User
from .serializers import TestSerializer, UserSerializer
from django.views.decorators.csrf import csrf_exempt


def test_list(request):
    test = Test.objects.all()
    serializer = TestSerializer(test, many=True)
    return JsonResponse({'test': serializer.data})



@csrf_exempt
def users_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse({'users': serializer.data})



# @api_view(['GET', 'POST'])
# def drink_list(request, format=None):
#     if request.method == 'GET':
#         drink = Drinks.objects.all()
#         serializer = DrinksSerializer(drink, many=True)
#         return Response(serializer.data)
#
#     if request.method == 'POST':
#         serializer = DrinksSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status.HTTP_201_CREATED)\


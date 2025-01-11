from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistrationSerializer


'''
def registration_view(request):
    if request.method == "POST":
        serializer = RegistrationSerializer(request.body)
        if serializer.is_valid():
            user = serializer.save()
            print(f"USER Created. ID: {user.id}, Username: {user.username}")
            return Response({'msg': 'User Registered successfully.'}, status=status.HTTP_200_CREATED)
        else:
            return Response({'msg': 'User with that username already Exist.'}, status=400)
    else:
        return Response({'msg': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
'''

class RegistrationAPIView(APIView):
    def post(self, request):
        print("WORKED")
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            print(f"User Id is: {user.id}")
            print(f"The username is {user.username}")
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

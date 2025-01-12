from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegistrationSerializer, ProfRegistrationSerializer, LoginSerializer, AnswerSubmitSerializer


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
class UserRegistrationAPIView(APIView):
    def post(self, request):
        print("WORKED")
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            print(f"User Id is: {user.id}")
            print(f"The username is {user.username}")
            return Response({"msg": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

class ProfRegistrationAPIView(APIView):
    def post(self, request):
        print("WORKED")
        serializer = ProfRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            prof = serializer.save()
            print(f"Prof Id is: {prof.id}")
            print(f"The username is {prof.username}")
            return Response({"msg": "Prof registered successfully"}, status=status.HTTP_201_CREATED)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            print(f"Logged in as: {user.username}")
            #print(f"ATTRIBUTES: {user.__dict__}") To get all attributes of an object.
            return Response({
                "msg": "Login successful",
                "username": user.username,
                "userType": "Prof" if (user.user_type == "prof") else "User"
            }, status=status.HTTP_200_OK)
        else:
            return Response(
                {'msg': 'Invalid Username or password',
                'error': serializer.errors
                }, 
                status=status.HTTP_400_BAD_REQUEST
                )


class AnswerSubmitAPIView(APIView):
    def post(self, request):
        serializer = AnswerSubmitSerializer(data=request.data)
        print("AnswerSubmitAPIView triggered.")
        if serializer.is_valid():
            profId = serializer.validated_data['profId']
            answers = serializer.validated_data['answers']
            # (processing here to be done)
            i = 1
            for key,value in answers.items():
                print(f"{i}) Key: {key}, Value: {value}")
                i += 1
            processed_data = {key: f"Processed: {value}" for key, value in answers.items()}
            return Response({
                "msg": "Answers processed successfully",
                "profId": profId,
                "processedAnswers": processed_data
            }, status=status.HTTP_200_OK)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

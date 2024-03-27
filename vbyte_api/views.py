from django.shortcuts import render
import random
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import generics, status
from .models import Teacher,gamecategory,Student,Timeline,Game,Usersregistration,Rules,Payment,Form
from .serializers import TeacherSerializer,gamecategorySerializer,StudentSerializer,TimelineSerializer,GameSerializer,UserSerializer,RulesSerializer,PaymentSerializer,FormSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer, EmailVerificationSerializer
from rest_framework.parsers import MultiPartParser, FormParser

from .serializers import*
from.emails import*


def generate_otp(length=6):
    """
    Generates a random numeric OTP of specified length.
    """
    return ''.join(random.choices('0123456789', k=length))


def send_otp_email(email, otp):
    """
    Sends the OTP to the specified email address.
    """
    subject = 'OTP Verification'
    message = f'Your OTP for email verification is: {otp}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    
    send_mail(subject, message, from_email, recipient_list)

class TeacherList(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class gamecategory(generics.ListCreateAPIView):
    queryset = gamecategory.objects.all()
    serializer_class = gamecategorySerializer

class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer    

class TimelineListCreateAPIView(generics.ListCreateAPIView):
    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializer

class TimelineRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializer

class GameListCreateAPIView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer   

class UserRegistrationAPIView(generics.CreateAPIView):
    queryset = Usersregistration.objects.all()
    serializer_class = UserSerializer    
  
  
class StudentRegistrationView(APIView):
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            student = serializer.save()
            # Send OTP to email
            otp = generate_otp()  # Define a function to generate OTP
            student.otp = otp
            student.save()
            send_otp_email(student.email, otp)  # Define a function to send OTP via email
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        student = Student.objects.filter(email=email, password=password).first()
        if student:
            # Generate and send OTP for email verification
            otp = generate_otp()  # Define a function to generate OTP
            student.otp = otp
            student.save()
            send_otp_email(student.email, otp)  # Define a function to send OTP via email
            return Response({'detail': 'OTP sent to your email'}, status=status.HTTP_200_OK)
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class EmailVerificationView(APIView):
    def post(self, request):
        serializer = EmailVerificationSerializer(data=request.data)
        if serializer.is_valid():
            otp = serializer.validated_data.get('otp')
            student = Student.objects.filter(otp=otp).first()
            if student:
                # Perform email verification logic here
                # You can set 'email_verified' flag to True in Student model, for example
                student.email_verified = True
                student.save()
                return Response({'detail': 'Email verified successfully'}, status=status.HTTP_200_OK)
        return Response({'detail': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)

class RulesListCreate(generics.ListCreateAPIView):
    queryset = Rules.objects.all()
    serializer_class = RulesSerializer

class RulesRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rules.objects.all()
    serializer_class = RulesSerializer


class PaymentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            context['request'] = self.request
        return context

    def perform_create(self, serializer):
        serializer.save()

class PaymentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer    


class FormListCreateAPIView(generics.ListCreateAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer

    def post(self, request, *args, **kwargs):
        # Check if the student has already filled two games
        email = request.data.get('email')
        if Form.objects.filter(email=email).count() >= 2:
            return Response({"error": "You can only fill in two games."}, status=status.HTTP_400_BAD_REQUEST)
        return super().post(request, *args, **kwargs)


from rest_framework import serializers
from .models import Teacher,gamecategory,Student,Timeline,Game,Usersregistration



class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id','full_name', 'email', 'password','mobile_no']

class gamecategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = gamecategory
        fields = ['id','title','description']        

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'student_name', 'otp','email', 'password','mobile_number', 'college_year'] 

class TimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeline
        fields = ['id', 'time', 'description', 'Gamename']     

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'game_name', 'game_details', 'game_image']    

#userregistration
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usersregistration
        fields = ['id', 'username', 'email', 'mobile_number', 'password',]
        extra_kwargs = {
            'password': {'write_only': True},
        }        

class EmailVerificationSerializer(serializers.Serializer):
    otp = serializers.CharField(max_length=6)
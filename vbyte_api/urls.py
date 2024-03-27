from django.urls import path
from django.contrib import admin
from .views import EmailVerificationView, StudentLoginView, StudentRegistrationView, TeacherList, TeacherDetail,gamecategory,StudentListCreateAPIView,StudentRetrieveUpdateDestroyAPIView,TimelineListCreateAPIView,TimelineRetrieveUpdateDestroyAPIView,GameListCreateAPIView,GameRetrieveUpdateDestroyAPIView,UserRegistrationAPIView,RulesRetrieveUpdateDestroy,RulesListCreate,PaymentListCreateAPIView,PaymentDetailAPIView,FormListCreateAPIView
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView


# from vbyte.views import*
# from .views import regiserAPI

urlpatterns = [
    path('teacher/', TeacherList.as_view(), name='teacher-list'),
    path('teacher/<int:pk>/', TeacherDetail.as_view(), name='teacher-detail'),
    path('gamecategory/', gamecategory.as_view(), name='gamecategory'),
    path('students/', StudentListCreateAPIView.as_view(), name='student_list_create'),
    path('students/<int:pk>/', StudentRetrieveUpdateDestroyAPIView.as_view(), name='student_detail'),
    path('timelines/', TimelineListCreateAPIView.as_view(), name='timeline_list_create'),
    path('timelines/<int:pk>/', TimelineRetrieveUpdateDestroyAPIView.as_view(), name='timeline_detail'),
    path('games/', GameListCreateAPIView.as_view(), name='game_list_create'),
    path('games/<int:pk>/', GameRetrieveUpdateDestroyAPIView.as_view(), name='game_detail'),
    path('register/', StudentRegistrationView.as_view(), name='student-register'),
    path('login/', StudentLoginView.as_view(), name='student-login'),
    path('verify-email/', EmailVerificationView.as_view(), name='verify-email'),
    path('rules/', RulesListCreate.as_view(), name='rules-list-create'),
    path('rules/<int:pk>/', RulesRetrieveUpdateDestroy.as_view(), name='rules-retrieve-update-destroy'),
    path('payments/', PaymentListCreateAPIView.as_view(), name='payment-list'),
    path('payments/<int:pk>/', PaymentDetailAPIView.as_view(), name='payment-detail'),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('forms/', FormListCreateAPIView.as_view(), name='form-list-create'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

 


from django.conf.urls import url, include
from django.urls import path

from StudentInfo.views import sendmail
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
# post views

                path('login/', auth_views.LoginView.as_view(), name='login'),
                path('logout/', auth_views.LogoutView.as_view(), name='logout'),
                path('', views.dashboard, name='dashboard'),
                path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
                path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
                path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
                path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
                path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
                path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
                path('sendmail', sendmail, name='sendmail'),
                path('register/', views.register, name='register'),
                path('studentdetails/', views.IndexView.as_view(), name='studentdetails'),
                path('addcourse/', views.CreateCourse.as_view(), name='add_course'),
                path('addsection/', views.CreateSection.as_view(), name='add_section'),
                path('addstudents/', views.CreateStudent.as_view(), name='add_students'),
                path('addtest/', views.CreateTest.as_view(), name='add_test'),
                path('addclubs/', views.CreateClub.as_view(), name='add_club'),
                path('addstudenttest/', views.create, name='add_student_test'),
                path('api/v2/course/', # urls list all and create new one
                            views.get_post_course.as_view(),
                                name='get_post_course'),
                path('sectiondetails/', views.SectionIndexView, name='get_section_detail'),
                path('testdetails/', views.TestIndexView, name='get_test_detail'),
                path('coursedetails/', views.CourseIndexView, name='get_course_detail'),
                path('clubdetails/', views.ClubIndexView, name='get_club_detail'),



]
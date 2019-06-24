from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction, IntegrityError
from django.forms import modelformset_factory
from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from StudentInfo.models import Student, Course, Section, Test, Club
from StudentInfo.pagination import CustomPagination
from StudentInfo.permissions import IsAuthenticated
from StudentInfo.serializers import CourseSerealizer
from .forms import LoginForm, CourseForm, ClubForm, TestForm, StudentForm, SectionForm, CourseComboForm, \
    SectionComboForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from . import serializers

def user_login(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                    username=cd['username'],
                    password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated '\
                                            'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})




@login_required
def dashboard(request):
    return render(request,
                    'account/dashboard.html',
                    {'section': 'dashboard'})


def sendmail(request):
    send_mail(
        'Subject',
        'Email message',
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
    )

    return HttpResponse('Mail successfully sent')


from .forms import LoginForm, UserRegistrationForm
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
            user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                   'account/register.html',
                    {'user_form': user_form})


class IndexView(ListView):
    template_name = 'studentinfo/studentsdetails.html'
    paginate_by = 20
    queryset = Student.objects.all()
    context_object_name = 'all_students_data'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(object_list=object_list, **kwargs)
        ctx['offset']= self.get_paginate_by(self.get_queryset())*(ctx['page_obj'].number-1)
        return ctx


# class CreateItems(CreateView):
#     template_name = 'studentinfo/add_items.html'
#
#     def form_valid(self, form):
#         if self.request.user.is_authenticated:
#             obj = form.save(commit=False)
#             obj.author = self.request.user
#             obj.save()
#             return super().form_valid(form)
#
#     model = Post
#     fields = ['title', 'content', 'categories', 'icon', 'post_date']
#     template_name = 'Blog/post_form.html'
#     success_url = reverse_lazy('Blog:index')


class CreateCourse(FormView, LoginRequiredMixin):
    template_name = 'studentinfo/add_items.html'
    form_class = CourseForm
    success_url = reverse_lazy('studentdetails')


    def form_valid(self, form):
        print(form)

        course = Course()
        course.course_title = form.cleaned_data['course_title']
        course.duration = form.cleaned_data['duration']
        course.syllabus = self.request.FILES['syllabus']
        course.credit_hours = form.cleaned_data['credit_hours']
        print(course.duration)
        print(course.course_title)
        print(course.syllabus)
        print(course.credit_hours)

        course.save()
        print("-----------------***-----------------")
        return super().form_valid(form)



class CreateSection(FormView):
    template_name = 'studentinfo/add_items.html'
    form_class = SectionForm
    success_url = reverse_lazy('studentdetails')

    def form_valid(self, form):
        section = Section()
        section.course = form.cleaned_data['course']
        section.name = form.cleaned_data['name']

        section.save()

        return super().form_valid(form)


class CreateStudent(FormView):
    template_name = 'studentinfo/add_items.html'
    form_class = StudentForm
    success_url = reverse_lazy('studentdetails')

    def form_valid(self, form):
        print(form.__dict__)
        # section = Student()
        # section.course = form.cleaned_data['mobile']
        # section.name = form.cleaned_data['']

        form.save()
        return super().form_valid(form)


class CreateTest(FormView):
    template_name = 'studentinfo/add_items.html'
    form_class = TestForm
    success_url = reverse_lazy('studentdetails')

    def form_valid(self, form):

        return super().form_valid(form)


class CreateClub(FormView):
    template_name = 'studentinfo/add_items.html'
    form_class = ClubForm
    success_url = reverse_lazy('studentdetails')

    def form_valid(self, form):
        return super().form_valid(form)


class CreaStudentTest(FormView):
    template_name ='studentinfo/formset.html'
    TestFormset = modelformset_factory(Section, form=SectionComboForm)
    form = CourseComboForm
    formset = TestFormset( queryset=Section.objects.none(), prefix='marks')

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs["prefix"] = 'marks'
    #     kwargs['initial'] = queryset=Section.objects.none()
    #     print(kwargs)
    #     return kwargs

    # def post(self, request, *args, **kwargs):
    #     """
    #     Handle POST requests: instantiate a form instance with the passed
    #     POST variables and then check if it's valid.
    #     """
    #
    #     form_class = CourseComboForm(request.POST)
    #     TestFormset = modelformset_factory(Section, form=SectionComboForm)
    #     formset = TestFormset(request.POST, queryset=Section.objects.none())
    #     print('**********************---------------------------------*************************')
    #     print(formset)
    #     return formset



    def form_valid(self, form):
        for sub_form in form:
            print(sub_form)

        return super().form_valid(form)



def create(request):
    context = {}
    CourseFormset = modelformset_factory(Section, form=SectionComboForm)
    form = CourseComboForm(request.POST or None,  request.FILES)
    formset = CourseFormset(request.POST or None, queryset=Section.objects.none(), prefix='marks')

    if request.method == "POST":
        print(form)
        print(formset)
        print('____________*************________________________')

        if formset.is_valid():
            print('_+_+_+_+_+______________++++++++++________________')
            if form.is_valid():

                print('-------------------------************--------------------')
                try:
                    with transaction.atomic():
                        print('_______________________________*******************_________________')
                        course = form.save(commit=False)
                        course.syllabus = request.FILES['syllabus']
                        print(course.syllabus)
                        course.save()

                        for section in formset:
                            data = section.save(commit=False)
                            data.course = course
                            data.save()
                except IntegrityError:
                    print("Error Encountered")

                return redirect('studentdetails')

    context['formset'] = formset
    context['form'] = form
    return render(request, 'studentinfo/formset.html', context)



class get_post_course(ListCreateAPIView):
    serializer_class = CourseSerealizer
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination
    template_name = 'course_api.html'

    def get_queryset(self):
        movies = Course.objects.all()
        return movies

    # Get all movies
    def get(self, request):
        course = self.get_queryset()
        paginate_queryset = self.paginate_queryset(course)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    # Create a new movie
    def post(self, request):
        serializer = CourseSerealizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SectionIndexView(ListView):
    template_name = 'studentinfo/section_details.html'
    queryset = Section.objects.all()
    context_object_name = 'all_students_data'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(object_list=object_list, **kwargs)
        return ctx


class CourseIndexView(ListView):
    template_name = 'studentinfo/course_details.html'
    queryset = Course.objects.all()
    context_object_name = 'all_students_data'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(object_list=object_list, **kwargs)
        return ctx

class ClubIndexView(ListView):
    template_name = 'studentinfo/club_details.html'
    queryset = Club.objects.all()
    context_object_name = 'all_students_data'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(object_list=object_list, **kwargs)
        return ctx


class TestIndexView(ListView):
    template_name = 'studentinfo/test_details.html'
    queryset = Test.objects.all()
    context_object_name = 'all_students_data'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(object_list=object_list, **kwargs)
        return ctx

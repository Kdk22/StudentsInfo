from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from StudentInfo.models import Student, Course
from .forms import LoginForm, CourseForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.views.generic.edit import FormView


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

        course = Course()
        course.course_title = form.cleaned_data['course_title']
        course.duration = form.cleaned_data['duration']
        course.syllabus = self.request.FILES
        course.credit_hours = form.cleaned_data['credit_hours']
        print(course.duration)
        print(course.course_title)
        print(course.syllabus)
        print(course.credit_hours)

        course.save()
        return super(CreateSection, self).form_valid(form)



class CreateSection(FormView):
    template_name = 'studentinfo/add_items.html'
    form_class = SectionForm
    success_url = reverse_lazy('studentdetails')

    def form_valid(self, form):

        return super(CreateSection, self).form_valid(form)


class CreateStudent(FormView):
    template_name = 'studentinfo/add_items.html'
    form_class = StudentForm
    success_url = reverse_lazy('studentdetails')

    def form_valid(self, form):
        return super(CreateSection, self).form_valid(form)


class CreateTest(FormView):
    template_name = 'studentinfo/add_items.html'
    form_class = TestForm
    success_url = reverse_lazy('studentdetails')

    def form_valid(self, form):
        return super(CreateSection, self).form_valid(form)


class CreateClub(FormView):
    template_name = 'studentinfo/add_items.html'
    form_class = ClubForm
    success_url = reverse_lazy('studentdetails')

    def form_valid(self, form):
        return super(CreateSection, self).form_valid(form)

from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DeleteView,CreateView,RedirectView,UpdateView,DetailView
from school_app.forms import ProfileForm, UserProfileForm,User
from .import models

from django.http import HttpResponseRedirect,HttpResponse,request
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# Create your views here.
class IndexView(TemplateView):
    template_name = 'first_app/index.html'

def user_register(request):

    registered = False

    if request.method == 'POST':

        user_form = UserProfileForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
                
            profile.save()

            registered = True

        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserProfileForm
        profile_form = ProfileForm

    return render(request,('first_app/register.html'),{'user_form':user_form,'profile_form':profile_form,'registered':registered})

def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return render(request,('first_app/success.html'))

            else:
                return HttpResponse('User Not Active')

        else:
            print('someone tried to login')
            print('username:{} and password:{}'.format(username,password))
            return render(request,('first_app/error.html'))

    else:
        return render(request,('first_app/login.html'))


@login_required    
def Success(request):
    return render(request,('first_app/success.html'))

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    template_name = 'basic_app/school_list.html'

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'


class SchoolCreateView(CreateView):

    model = models.School
    fields = ('name','location','principle','main_branch')
    template_name = 'basic_app/school_form.html'

class StudentCreateView(CreateView):

    model = models.Student
    fields = '__all__'
    template_name = 'basic_app/school_form_two.html'

class ThankPage(TemplateView):
    template_name = 'basic_app/thank.html'


class SchoolUpdateView(UpdateView):
    fields = ('name','principle','main_branch')
    model = models.School
    template_name = 'basic_app/school_form.html'

class StudentUpdateView(UpdateView):
    fields = ('__all__')
    model = models.Student
    template_name = 'basic_app/school_form_two.html'

class DeletePage(TemplateView):
    template_name = 'basic_app/delete.html'

class ContactPage(TemplateView):
    template_name = 'first_app/contact.html'

class AboutPage(TemplateView):
    template_name = 'first_app/about.html'
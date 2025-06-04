#generic views

from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View
from .forms import UserForm
from .models import Album
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect



class IndexView(generic.ListView):
    template_name='music/index.html'
    context_object_name='all_albums'
    def get_queryset(self):
        return Album.objects.all()
    
class DetailView(generic.DetailView):
    model=Album 
    template_name='music/detail.html'

class AlbumCreate(CreateView):
    model= Album 
    fields=['artist','album_title','genre','album_logo']

class AlbumUpdate(UpdateView):
    model= Album 
    fields=['artist','album_title','genre','album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')
class UserFormView(View):
    form_class=UserForm
    template_name='music/registration_form.html'
    
    # displays a blank form 
    def get(self, request):
        form=self.form_class(None)
        return render(request,self.template_name, {'form':form})
    # process form data
    def post(self,request):
        form=self.form_class(request.POST)

        if form.is_valid():
            user=form.save(commit=False)#creates an object from the information in form but does not save to the DB

            # cleaned (normalized) data
            username =form.cleaned_data['username']
            password =form.cleaned_data['password']
            user.set_password(password) #  password are not normal text so when u want to chnage a password this is the method
            user.save()# savses to DB
            # returns User objects if credentials are correct
            user =authenticate(username=username,password=password) #essentially it takes the inputs and checks in DB to see if the exists, if the object does exist it return it 
            if user is not None:
                
                if user.is_active: # to check if they are banned,or inacitve for some reason
                    login(request, user) # the user in and attach a session
                    return redirect('music:index')
            
        return render(request,self.template_name, {'form':form})
class LoginView(View):
        template_name = 'music/login.html'

        def get(self, request):
            return render(request, self.template_name)

        def post(self, request):
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('music:index')
            return render(request, self.template_name, {'error_message': 'Invalid login'})
        

class LogoutView(View):
        def get(self, request):
            logout(request)
            return redirect('music:login')




    


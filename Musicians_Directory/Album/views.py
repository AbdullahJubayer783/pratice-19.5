from django.shortcuts import render , redirect
from . import forms
from . import models
from django.views.generic import CreateView , UpdateView ,DeleteView 
from django.urls import reverse_lazy
# Create your views here.

def edit_post(request , id):
    post = models.Albums.objects.get(pk = id)
    print(post)
    form = forms.MusicianForm(instance=post)
    if request.method == 'POST':
        form = forms.MusicianForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'Album.html',{'form' : form})

class EditPostView(UpdateView):
    model = models.Albums
    form_class = forms.MusicianForm
    template_name = 'Album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy("home")
    
class DeletePostView(DeleteView):
    model = models.Albums
    template_name = 'delete.html'
    success_url = reverse_lazy("home")
    pk_url_kwarg = 'id'



# def delete_post(request,id):
#     post = models.Albums.objects.get(pk = id)
#     post.delete()
#     return redirect("home")
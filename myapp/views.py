from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .forms import ImageForm
from .models import Image

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        form.save()
        return HttpResponseRedirect(reverse('home'))
    else:
        form = ImageForm()
        
    img = Image.objects.all()     
    return render(request, 'myapp/home.html', {'img':img,'form':form})
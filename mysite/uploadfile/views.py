# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from django.views.decorators.csrf import csrf_exempt
from .models import File
from .assistance import handle_uploaded_file
from django.template.loader import get_template  

@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            newfile = request.FILES['file'] 
            handle_uploaded_file(newfile)

            # Redirect to the document list after POST  
            get_template('succ.html')
            return HttpResponseRedirect(reverse('succ.html'))  
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
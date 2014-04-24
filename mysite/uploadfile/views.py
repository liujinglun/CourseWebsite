# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from django.views.decorators.csrf import csrf_exempt
from .models import File
from .assistance import handle_uploaded_file
from django.template.loader import get_template  
import datetime
import os
from mysite.settings import DOUCMENT_ROOT


@csrf_exempt
def upload_file(request):
	if request.user.is_authenticated():
	    if request.method == 'POST':
	        form = UploadFileForm(request.POST, request.FILES)
	        if form.is_valid():
	            # file is saved
	            current_user = request.user
	            newfile = request.FILES['file'] 
	            newrecord = File(filename=newfile.name,upload_time=datetime.datetime.now(),uploader=current_user,docfile=os.path.join(DOUCMENT_ROOT, newfile.name))
	            newrecord.save()
	            handle_uploaded_file(newfile)
	            # Redirect to the document list after POST  
	            get_template('succ.html')
	            return HttpResponseRedirect(reverse('succ.html'))  
	    else:
	        form = UploadFileForm()
	    return render(request, 'upload.html', {'form': form})
	else:
		return HttpResponseRedirect('mysite.views.index')


from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class File(models.Model):
	id = models.AutoField(primary_key=True)
	filename = models.CharField(max_length=200)
	upload_time = models.DateTimeField('file upload')
	filetype =(
		('pdf','pdf'),
		('doc','doc'),
		('docx','docx'),
		)
	uploader = models.ForeignKey(User)
	docfile = models.FileField(upload_to='documents/%Y/%m/%d')  
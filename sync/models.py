from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import hashlib
from os import path, remove
from django.contrib.auth.models import User

# Create your models here.

class MediaFileSystemStorage(FileSystemStorage):
    def get_available_name(self, name, max_length = None):
        if max_length and len(name)> max_length:
            raise(Exception("Name's length is greater than max_length"))
        return name

    def _save(self, name, content):
        if self.exists(name):
            #return name
            filepath = path.join(settings.MEDIA_ROOT, name)
            remove(filepath)

        return super(MediaFileSystemStorage, self)._save(name, content)

def user_directory_path(instance, filename):
    return '%s/%s/%s' %(instance.owner.username, instance.path ,filename)

class Files(models.Model):
    owner = models.ForeignKey('auth.User', related_name='file', to_field = 'id', on_delete=models.CASCADE)
    path = models.CharField(max_length = 1000)
    file = models.FileField(upload_to = user_directory_path, verbose_name = 'File', storage = MediaFileSystemStorage())
    hash = models.CharField(max_length = 36)
    date = models.DateTimeField(auto_now = True)
    filename = models.CharField(max_length = 36)



    def save(self, *args, **kwargs):
        if not self.pk:
            self.filename = path.basename(self.file.name)
            md5 = hashlib.md5()
            for chunk in self.file.chunks():
                md5.update(chunk)
            self.hash = md5.hexdigest()
            instance = Files.objects.filter(filename = self.filename, path = self.path)
            print instance
            instance.delete()
        super(Files, self).save(*args, **kwargs)

    class Meta:
        db_table = 'files'

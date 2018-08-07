from django.db import models
from django.conf import settings
import shutil
import os


# Create your models here.

class Graphic(models.Model):
    title = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        project_root = os.path.join(settings.MEDIA_ROOT, 'graphics/{0}/'.format(self.title))
        if not os.path.exists(project_root):
            os.makedirs(project_root)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        project_root = os.path.join(settings.MEDIA_ROOT, 'graphics/{0}/'.format(self.title))
        if os.path.isdir(project_root):
            shutil.rmtree(os.path.join(settings.MEDIA_ROOT, 'graphics/{0}/'.format(self.title)))
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']


class FileType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class File(models.Model):
    graphic = models.ForeignKey(Graphic, on_delete=models.CASCADE)
    file = models.FileField()
    type = models.ForeignKey(FileType, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        file_folder = os.path.join(settings.MEDIA_ROOT, f'graphics/{self.graphic.title}/{self.type.name}')
        if not os.path.exists(file_folder):
            os.makedirs(file_folder)

        if self.graphic.title not in self.file.path:
            current_path = self.file.path
            self.file.name = os.path.join(f'graphics/{self.graphic.title}/{self.type.name}', self.file.name)
            new_path = os.path.join(settings.MEDIA_ROOT, self.file.name)
            os.rename(current_path, new_path)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if os.path.exists(self.file.path):
            os.remove(self.file.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.file.name


class Thumbnail(models.Model):
    graphic = models.OneToOneField(Graphic, on_delete=models.CASCADE)
    file = models.ImageField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        file_folder = os.path.join(settings.MEDIA_ROOT, f'graphics/{self.graphic.title}/images')
        if not os.path.exists(file_folder):
            os.makedirs(file_folder)

        if self.graphic.title not in self.file.path:
            current_path = self.file.path
            self.file.name = os.path.join(f'graphics/{self.graphic.title}/images', self.file.name)
            new_path = os.path.join(settings.MEDIA_ROOT, self.file.name)
            os.rename(current_path, new_path)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if os.path.isfile(self.file.path):
            os.remove(self.file.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.file.name

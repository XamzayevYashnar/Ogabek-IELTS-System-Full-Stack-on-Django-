from django.db import models


class Folder(models.Model):
    title = models.CharField(max_length=100, unique=True)
    icon_class = models.CharField(max_length=100, default='fas fa-folder-open')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Material(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='materials/', blank=True, null=True)
    icon_class = models.CharField(max_length=100, default='fas fa-file-alt')
    folder = models.ForeignKey(
        Folder,
        related_name='materials',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

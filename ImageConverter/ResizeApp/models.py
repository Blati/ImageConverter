import os
import urllib.request

from django.core.files import File
from django.db import models


class Image(models.Model):
    link = models.URLField(verbose_name="Ссылка", max_length=255, blank=True)
    image = models.FileField(verbose_name="Файл", blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.link and not self.image:
            result = urllib.request.urlretrieve(self.link)
            self.image.save(
                os.path.basename(self.link),
                File(open(result[0], 'rb'))
            )
            self.save()
        super().save(*args, **kwargs)

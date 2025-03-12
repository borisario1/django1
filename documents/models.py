from django.db import models

# Create your models here.
class DocumentTemplate(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название шаблона")
    file = models.FileField(upload_to='templates/', verbose_name="Файл шаблона")

    def __str__(self):
        return self.name

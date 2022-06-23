from django.db import models


class RawPic(models.Model):
    objects = models.Manager()
    # raw_pic = models.ImageField(upload_to='transfer', validators=[validators.FileExtensionValidator(['jpg', 'png', 'bmp', 'tiff'], message='Type Error')])
    raw_pic = models.ImageField(upload_to='transfer')
    style = models.CharField(max_length=20)


class ProcessedPic(models.Model):
    objects = models.Manager()
    pro_pic = models.ImageField(upload_to='transfer')


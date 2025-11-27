from django.db import models

class SevaActivity(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='seva/')
    description = models.TextField(blank=True, null=True)
    order_number = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order_number']

    def __str__(self):
        return self.title

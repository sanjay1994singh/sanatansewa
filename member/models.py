from django.db import models


class Designation(models.Model):
    title = models.CharField(max_length=255)
    order_number = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order_number']

    def __str__(self):
        return self.title


class Member(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='members/')
    description = models.TextField(blank=True, null=True)
    designation = models.ForeignKey(Designation, on_delete=models.SET_NULL, null=True, blank=True)
    order_number = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order_number']  # auto-sort by order_number

    def __str__(self):
        return self.name

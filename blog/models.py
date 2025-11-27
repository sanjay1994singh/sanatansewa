from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blogs/', blank=True, null=True)
    short_description = models.CharField(max_length=500, blank=True, null=True)
    content = models.TextField()
    author = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    order_number = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-created_at', 'order_number']

    def __str__(self):
        return self.title

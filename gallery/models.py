from django.db import models
from PIL import Image
import os

class Gallery(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='gallery/')
    order_number = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title if self.title else "Gallery Image"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img_path = self.image.path
        img = Image.open(img_path)

        # --- Resize if too large ---
        max_width = 1600
        if img.width > max_width:
            ratio = max_width / img.width
            new_height = int(img.height * ratio)
            img = img.resize((max_width, new_height), Image.LANCZOS)

        # --- Compress image without visible quality loss ---
        img.save(img_path, optimize=True, quality=85)

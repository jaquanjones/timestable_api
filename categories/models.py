from django.db import models


# using sqlite3

class Category(models.Model):
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]

    class Meta:
        ordering = ['-updated']


class CategoryImage(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category_image')

    def __str__(self):
        return self.title


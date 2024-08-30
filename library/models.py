from django.db import models


class Book(models.Model):
    title  = models.CharField(max_length=100,null=False,blank=False)
    author = models.CharField(max_length=100,null=False,blank=False)
    price  = models.FloatField(null=False)
    publication_at = models.DateField(auto_now_add=True,null=False)

    class Meta:
        unique_together = ('title', 'author')

    def __str__(self):
        return self.title

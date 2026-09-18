from django.db import models

# Create your models here.
class Link(models.Model):
    url = models.URLField()
    code = models.CharField(max_length=10, unique=True)
    clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ID: {self.id}\nurl: {self.url}\n code: {self.code}\n clicks: {self.clicks}\n created at: {self.created_at}"
    
    
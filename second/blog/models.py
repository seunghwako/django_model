from django.db import models

# Create your models here.
class Blog(models.Model) :
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

# 제목 그대로 보이게 하는 방법
    def __str__(self) :
        return self.title

    def summary(self) :
        return self.body[:100]

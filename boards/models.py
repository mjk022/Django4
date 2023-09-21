from django.db import models

class Board(models.Model):
    title = models.CharField(max_length=64)
    contents = models.TextField()
    writer = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'boards'
        verbose_name = '커뮤니티 게시판'
        verbose_name_plural = '커뮤니티 게시판'

class Predict(models.Model):
    first = models.FloatField()
    second = models.FloatField()
    third = models.FloatField()
    fourth = models.FloatField()

class News21_1(models.Model):
    date = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=180)
    url = models.CharField(max_length=100)

    def __str__(self):
        return "날짜 : " + self.date + " 제목 : " + self.title + " 내용 : " + self.description + " 링크 : " + self.url
    
class News21_2(models.Model):
    date = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=180)
    url = models.CharField(max_length=100)

class News21_3(models.Model):
    date = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=180)
    url = models.CharField(max_length=100)

class News21_4(models.Model):
    date = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=180)
    url = models.CharField(max_length=100)

class News22_1(models.Model):
    date = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=180)
    url = models.CharField(max_length=100)

class News22_2(models.Model):
    date = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=180)
    url = models.CharField(max_length=100)

class News22_3(models.Model):
    date = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=180)
    url = models.CharField(max_length=100)

class News22_4(models.Model):
    date = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=180)
    url = models.CharField(max_length=100)

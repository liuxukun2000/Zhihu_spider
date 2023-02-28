from django.db import models

# Create your models here.
class User(models.Model):
    id = models.CharField(primary_key=True, blank=False, null=False, max_length=128)
    username = models.CharField(max_length=128, blank=False, null=False, db_index=True)
    area = models.CharField(max_length=128, blank=False, null=True, db_index=True)
    description = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=16, null=False, blank=False, db_index=True)
    url_token = models.CharField(max_length=128, blank=False, null=False)

class Question(models.Model):
    id = models.CharField(primary_key=True, blank=False, null=False, max_length=128)
    answer_count = models.IntegerField(default=0)
    # update_time = models.IntegerField(default=0)
    content = models.TextField(null=False, blank=False)

class Answer(models.Model):
    id = models.CharField(primary_key=True, blank=False, null=False, max_length=128)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    content = models.TextField(null=False, blank=False)
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    update_time = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)

class Comment(models.Model):
    id = models.CharField(primary_key=True, blank=False, null=False, max_length=128)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    children = models.TextField(blank=True, null=True)
    answer = models.ForeignKey(to=Answer, on_delete=models.CASCADE)
    content = models.TextField(null=False, blank=False)


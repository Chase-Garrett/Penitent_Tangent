from django.db import models

# Create your models here.

class Results(models.Model):
   subreddit = models.CharField(max_length=200, unique=True)
   positive = models.IntegerField(default=0)
   neutral = models.IntegerField(default=0)
   negative = models.IntegerField(default=0)

   def __str__(self):
       return f"Subreddit: {self.subreddit}, Positive: {self.positive}, Neutral: {self.neutral}, Negative: {self.negative}"

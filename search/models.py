from django.db import models
from django.contrib.auth.models import User


class Search(models.Model):
    hashtag = models.CharField(max_length=50)
    
    def __unicode__(self):
        return "Search from".format(self.hashtag)
from django.db import models

#=============================
# Messages
#=============================
class Tweet(models.Model):
    text = models.CharField(max_length=300)
    user_name = models.CharField(max_length=100)

class WJNHPost(models.Model):
    text = models.CharField(max_length=400)
    user_name = models.CharField(max_length=100)

#=============================
# Classifications
#=============================
class Classification(models.Model):
    boolval = models.BooleanField(blank=True, null=True)
    floatval = models.FloatField(blank=True, null=True)

    def get_value(self):
        if self.boolval is None:
            return self.floatval
        else:
            return self.boolval

    class Meta:
        abstract = True

class TweetClassification(Classification):
    message = models.ForeignKey(Tweet)

class WJNHPostClassification(Classification):
    message = models.ForeignKey(WJNHPost)

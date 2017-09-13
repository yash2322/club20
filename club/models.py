from django.db import models
import os
# Create your models here.

class UpcomingEvents(models.Model):
    title = models.CharField(max_length=250,blank=False)
    details = models.TextField(blank=True)
    time = models.TimeField(auto_now=False, auto_now_add=False, blank=False)
    date = models.DateField(auto_now=False, auto_now_add=False, blank=False)
    slug = models.SlugField()
    Venue = models.CharField(max_length=250,blank=False,default='Parade Ground')
    register = models.URLField()

    class Meta:
        ordering = ['date','time']

    def get_upload_path(instance, filename):
        base = os.path.join(
        "New_%s" % instance.title)
        base = 'UpcomingEvents/'+ base
        return base

    poster = models.ImageField(upload_to=get_upload_path)

    def __self__(self):
        return self.title



class SuccessfullEvents(models.Model):
    title = models.CharField(max_length=250,blank=False)
    details = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    def __self__(self):
        return self.title


class SuccessfullEventsImages(models.Model):
    successfullevents = models.ForeignKey(SuccessfullEvents,related_name='SuccessfullEvents')


    def upload_path(self, name):
        folder = self.successfullevents.title
        folderFinalPath = 'SuccessfullEvents/' + folder + '/'
        if not os.path.exists(folderFinalPath):
            os.makedirs(folderFinalPath)
            return os.path.join(folderFinalPath,folder)
        return os.path.join(folderFinalPath,folder)

    snap = models.ImageField(upload_to=upload_path)

class ContactSection(models.Model):
    name = models.CharField(max_length=250,blank=False)
    email = models.EmailField(blank=False)
    message = models.TextField(blank=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    FEED_CHOICES = (('Complaints','Complaint'),('Feedback', 'Feedback'),('Suggestion','Suggestion'))
    firstname = models.CharField(max_length=100,blank=False)
    lastname = models.CharField(max_length=100,blank=True)
    feedType = models.CharField(max_length=100,choices=FEED_CHOICES,
                                       )

    message = models.TextField()

    def __str__(self):
        return self.feedType

from django.utils.timezone import datetime
from django.db import models

# Conversation is the top level object. It has messages attached. 
class Conversation(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    startdate = models.DateField("Start Date", default=datetime.now())

    def __str__(self):
        return self.title

# Messages are foreign keyed to a specific conversation. They have associated 'thoughts'
class Message(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.CharField(max_length=1000)
    timesent = models.DateTimeField("Time Sent", default=datetime.now())
    Conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    # I think there's probably a better way to bind the associated thoughts than to have a list here.
    # The django model paradigm has me somewhat wrong footed. 
    thoughts = []

# Thoughts are foreign keyed to a specific message (which is on a specific conversation)
class Thought(models.Model):
    text = models.CharField(max_length=1000)
    timesent = models.DateTimeField("Time Sent", default=datetime.now())
    Message = models.ForeignKey(Message, on_delete=models.CASCADE)
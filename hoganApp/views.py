from hoganApp.models import Conversation, Message, Thought
from hoganApp.templates.hoganApp.forms import ConversationForm, ConvoSearchForm, MessageSearchForm
from hoganApp.templates.hoganApp.forms import MessageForm
from hoganApp.templates.hoganApp.forms import ThoughtForm
from django.views.generic import ListView
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.utils.timezone import datetime

#test view
def home(request):
    return HttpResponse("Hello World!")

class ConversationListView(ListView):
    """Renders the home page, with a list of all conversations."""
    model = Conversation

    def get_context_data(self, **kwargs):
        context = super(ConversationListView, self).get_context_data(**kwargs)
        return context

def newconversation(request):
    form = ConversationForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            conversation = form.save(commit=False)
            conversation.save()
            return redirect("/Conversations/")
    else:
        return render(request, "hoganApp/newconversation.html", {"form": form})

def conversation(request, id):
    """Used to interact with a single conversation. Should display key details and list of messages"""
    
    conversation = Conversation.objects.get(id = id)

    # use it to get the associated messages. 
    messages = Message.objects.filter(Conversation = conversation)

    for message in messages:
        message.thoughts = Thought.objects.filter(Message = message)

    form = MessageForm(request.POST or None)
    if request.method == "POST":
        message = form.save(commit=False)
        message.Conversation = conversation
        message.timesent = datetime.now()
        message.save()
        return render(
            request, 
            "hoganApp/conversation.html", 
        {"form": form,
        "messages": messages,
        'id': id})  
        #this wasn't working V
        #redirect("Conversation/" + title)
    else:       
        return render(
            request, 
            "hoganApp/conversation.html", 
        {"form": form,
        "messages": messages,
        "text": conversation.title,
        "conversationId": conversation.id,
        'id': id})


def message(request, id, convoId):
    """Used to interact with a single message. Should display key details and list of messages""" 
    # Query for the appropriate message,
    message = Message.objects.get(id = id)

    form = ThoughtForm(request.POST or None)
    if request.method == "POST":
        thought = form.save(commit=False)
        thought.Message = message
        thought.timesent = datetime.now()
        thought.save()

    # The associated thoughts to the original message. 
    thoughts = Thought.objects.filter(Message = message)
             
    return render(
        request, 
        "hoganApp/message.html", 
    {"form": form,
    "thoughts": thoughts,
    'text': message.text,
    "conversationId": convoId,
    "id": id})
from hoganApp.models import Conversation, Message, Thought
from hoganApp.templates.hoganApp.forms import ConvoSearchForm, MessageSearchForm
from django.shortcuts import render

def searchconvos(request):
    """Used to search conversations. Should display key details and list of messages where content is like search terms"""
    
    form = ConvoSearchForm(request.POST or None)
    if request.method == "POST":
        search = form.save(commit=False)
        searchterm = search.title
        
        conversations = Conversation.objects.filter(title__contains = searchterm) 
        # Note, this is the definition of minimally functional. 
        # A great deal more is available for flexible and robust querying https://docs.djangoproject.com/en/3.2/topics/db/search/
        return render(
            request, 
            "hoganApp/conversations.html", 
        {"form": form,
        "conversation_list": conversations,
        'id': id})  
    else:       
        return render(
            request, 
            "hoganApp/searchconvos.html", 
        {"form": form,
        })


def searchmesses(request):
    """Used to search messages. Should display key details and list of messages where content is like search terms"""

    form = MessageSearchForm(request.POST or None)
    noresult = True
    if request.method == "POST":
        search = form.save(commit=False)
        searchterm = search.text
        
        messages = Message.objects.filter(text__contains = searchterm)
        # TODO set page to respond if there's an empty return. 
        return render(
            request, 
            "hoganApp/searchmesses.html", 
        {"form": form,
        "message_list": messages,
        })  
    else:       
        return render(
            request, 
            "hoganApp/searchmesses.html", 
        {"form": form,
        })

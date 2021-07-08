from hoganApp.models import Conversation
from django.urls import path
from hoganApp import searchviews, views

# This variable defines the structure necessary to query the db for
# display of conversations to the front end.
conversation_list_view = views.ConversationListView.as_view(
    queryset=Conversation.objects.order_by("startdate"), 
    context_object_name="conversation_list",
    template_name="hoganApp/conversations.html",
)

# Set the local (to hoganApp) routing and navigation 
# in order for this to work within the framework, it has to be matched 
# in the urls.py of the parent web_project urls.py file.
urlpatterns = [path("Conversations/", conversation_list_view, name="Conversations"),

# Make the home page the conversations list page
path("", conversation_list_view, name="Conversations"),

path("NewConversation/", views.newconversation, name="NewConversation"),
path("Conversation/<id>/", views.conversation, name="Conversation"),
path("Message/<id>/<convoId>", views.message, name="Message"),

# Searches
path("Search/Conversations", searchviews.searchconvos, name="Search"),
path("Search/Messages", searchviews.searchmesses, name="Search"),
]

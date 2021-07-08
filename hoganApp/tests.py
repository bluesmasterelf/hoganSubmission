from hoganApp.views import ConversationListView
from hoganApp.searchviews import searchconvos, searchmesses
from hoganApp.models import Conversation, Message, Thought
from django.test import TestCase, RequestFactory, Client

# Test models, not much to test with these models. 
class ConversationModelTestCase(TestCase):
    def setUp(self):
        Conversation.objects.create(
            title = "Test Conversation")
        Message.objects.create(
            text = "Text message text",
            Conversation = Conversation.objects.get(id = 1)
        )

    def test_Message_Foreign_Key_To_Conversation(self):
        testMessage = Message.objects.get(id = 1)
        self.assertTrue(testMessage.Conversation.pk == 1)
        
    def test_ModelCreation(self):
        testConversation = Conversation.objects.get(title="Test Conversation")
        self.assertTrue(testConversation.pk == 1)

    def test_NoThoughts(self):
        with self.assertRaises(Thought.DoesNotExist):
            Thought.objects.get(text = "test fail text")

# Test views
class ViewTestCase(TestCase):
    def setUp(self):
        conversationsHopefully = ConversationListView.get_context_data()
        # Empty lists evaluate to false, so assert true is same as nonempty
        self.assertTrue(conversationsHopefully)

# Test searches
class ConversationSearchTestCase(TestCase):
    def setUp(self):
        # django automatically tears down test db (which is pretty snazzy, imo)
        Conversation.objects.create(title = "Test Conversation")
        Conversation.objects.create(title = "Test Conversation2")
        Conversation.objects.create(title = "Test Conversation3")
        Conversation.objects.create(title = "Important Conversation")
        Conversation.objects.create(title = "Chatty Unimportant")
        Conversation.objects.create(title = "SuperfluousEntirelyThough")
        Conversation.objects.create(title = "154277")

    def test_searchTestContainsThreeResults(self):
        request = RequestFactory().post('/Search/Conversations/', {'title': 'test'}, format='json')
        response = searchconvos(request)
        self.assertEqual(response.status_code, 200)
        # Note: below is fairly janky. 
        # My instinct is that the search method should be factored into a controller layer, but maybe that's not pythonic?
        # I've been a c-style dev for a while. It'll take a few minutes to break in a new style. 
        self.assertContains(response, "Conversation2", 1)        
        self.assertContains(response, "Chatty", 0)
        self.assertContains(response, "Conversation3", 1)

class MessageSearchTestCase(TestCase):
    def setUp(self):
        Conversation.objects.create(title = "Test Conversation")
        Message.objects.create(
            text = "Qwerty message te!xt",
            Conversation = Conversation.objects.get(id = 1)
        )
        Message.objects.create(
            text = "Qwerty textx",
            Conversation = Conversation.objects.get(id = 1)
        )
        Message.objects.create(
            text = "Qwerty message",
            Conversation = Conversation.objects.get(id = 1)
        )
        Message.objects.create(
            text = "message text5",
            Conversation = Conversation.objects.get(id = 1)
        )

    def test_searchTestContainsThreeResults(self):
        request = RequestFactory().post('/Search/Messages/', {'text': 'Qwerty'}, format='json')
        response = searchmesses(request)
        self.assertEqual(response.status_code, 200)        
        # The return occurs once each in the 'value' of the search, and once in the render. 
        self.assertContains(response, "Qwerty", 4)

    def test_searchTestContainsCorrectResults(self):
        request = RequestFactory().post('/Search/Messages/', {'text': 'ext5'}, format='json')
        response = searchmesses(request)
        self.assertEqual(response.status_code, 200)  
        print(response.content) 
        # The return occurs once in the 'value' of the search, and once in the render. 
        self.assertContains(response, "ext5", 2)

# Test urls/mappings? Need an ARC/Http client style test utility
class greaterThan200TestCase(TestCase):
    def testBadUrls(self):
        c = Client()
        response = c.post('/login/')
        self.assertEqual(response.status_code, 404)

        badSearchResponse = c.post('/Search/Messages/', {'text': 'Qwerty'}, format='json')
        self.assertEqual(badSearchResponse.status_code, 404)
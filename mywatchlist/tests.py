from django.test import TestCase, Client
from django.urls import reverse

class TestMywatchlist(TestCase):
    def test_show_mywatchlist_html(self):
        client = Client()
        response = client.get(reverse("mywatchlist:show_mywatchlist"))
        self.assertEquals(response.status_code, 200)
    
    def test_show_mywatchlist_xml(self):
        client = Client()
        response = client.get(reverse("mywatchlist:mywatchlist_xml"))
        self.assertEquals(response.status_code, 200)
    
    def test_show_mywatchlist_json(self):
        client = Client()
        response = client.get(reverse("mywatchlist:mywatchlist_json"))
        self.assertEquals(response.status_code, 200)
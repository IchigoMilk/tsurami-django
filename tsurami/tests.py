from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class IndexTests(TestCase):
	def test_index_view_status_ok(self):
		url = reverse('index')
		res = self.client.get(url)
		self.assertEquals(res.status_code, 200)

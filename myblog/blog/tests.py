from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Entry

class EntryModelTest(TestCase):
  def test_string_representation(self):
    entry = Entry(title="My entry title")
    self.assertEqual(str(entry), entry.title)

  def test_verbose_name_plural(self):
    self.assertEqual(str(Entry._meta.verbose_name_plural), "entries")

class ProjectTest(TestCase):
  def test_homepage(self):
    response = self.client.get('/')
    self.assertEqual(response.status_code, 200)

class HomePageTests(TestCase):
  """ Test whether our blog entries show up on the homepage """

  def setUp(self):
    self.user = get_user_model().objects.create(username='some_user')
  
  def test_one_entry(self):
    Entry.objects.create(title='title.1', body='body.1', author=self.user)
    response = self.client.get('/')
    self.assertContains(response, 'title.1')
    self.assertContains(response, 'body.1')

  def test_two_entries(self):
    Entry.objects.create(title='title.1', body='body.1', author=self.user)
    Entry.objects.create(title='title.2', body='body.2', author=self.user)
    response = self.client.get('/')
    self.assertContains(response, 'title.1')
    self.assertContains(response, 'title.2')
    self.assertContains(response, 'body.2')

  def test_no_entries(self):
    response = self.client.get('/')
    self.assertContains(response, 'No blog entries yet.')
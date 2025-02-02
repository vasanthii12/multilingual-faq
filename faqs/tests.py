from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import FAQ

class TestFAQModel(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question="How do I use this API?",
            answer="<p>Just make a GET request to /api/faqs/</p>",
            language="en"
        )

    def test_faq_creation(self):
        """Test FAQ model creation"""
        self.assertEqual(self.faq.question, "How do I use this API?")
        self.assertEqual(self.faq.language, "en")

    def test_str_representation(self):
        """Test string representation of FAQ"""
        self.assertEqual(str(self.faq), "How do I use this API?")

    def test_translation_method(self):
        """Test the translation method"""
        translation = self.faq.get_translation("hi")
        self.assertIn('question', translation)
        self.assertIn('answer', translation)

class TestFAQAPI(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.faq = FAQ.objects.create(
            question="What is this API?",
            answer="<p>This is a multilingual FAQ API.</p>",
            language="en"
        )
        self.url = reverse('faq-list')

    def test_get_faq_list(self):
        """Test getting list of FAQs"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_get_faq_translation(self):
        """Test getting FAQ in different language"""
        response = self.client.get(f"{self.url}?lang=hi")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        if isinstance(response.data, list):
            data = response.data[0]
        else:
            data = response.data['results'][0]
        self.assertIn('translated_from', data)
        self.assertEqual(data['translated_from'], 'en')
        self.assertEqual(data['translated_to'], 'hi')

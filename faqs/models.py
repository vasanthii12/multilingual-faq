from django.db import models
from django.conf import settings
from django.core.cache import cache
from django_ckeditor_5.fields import CKEditor5Field
from googletrans import Translator

class FAQ(models.Model):
    LANGUAGES = (
        # English
        ('en', 'English'),
        
        # Indian Languages
        ('hi', 'Hindi'),
        ('bn', 'Bengali'),
        ('te', 'Telugu'),
        ('ta', 'Tamil'),
        ('ml', 'Malayalam'),
        ('kn', 'Kannada'),
        ('mr', 'Marathi'),
        ('gu', 'Gujarati'),
        ('pa', 'Punjabi'),
        ('ur', 'Urdu'),
        
        # European Languages
        ('es', 'Spanish'),
        ('fr', 'French'),
        ('de', 'German'),
        ('it', 'Italian'),
        ('pt', 'Portuguese'),
        ('nl', 'Dutch'),
        ('ru', 'Russian'),
        
        # Asian Languages
        ('zh-cn', 'Chinese (Simplified)'),
        ('zh-tw', 'Chinese (Traditional)'),
        ('ja', 'Japanese'),
        ('ko', 'Korean'),
        ('vi', 'Vietnamese'),
        ('th', 'Thai'),
        
        # Middle Eastern Languages
        ('ar', 'Arabic'),
        ('fa', 'Persian'),
        ('tr', 'Turkish'),
        
        # Other Popular Languages
        ('id', 'Indonesian'),
        ('ms', 'Malay'),
        ('sw', 'Swahili'),
    )

    # Basic Fields
    question = models.TextField(help_text="The full question text")
    answer = CKEditor5Field(help_text="The detailed answer with formatting", config_name='extends')
    language = models.CharField(max_length=7, choices=LANGUAGES, default='en')
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'
        ordering = ['-created_at']

    def __str__(self):
        return self.question

    def get_translation(self, target_lang):
        """Get translated version of FAQ in target language."""
        if target_lang == self.language:
            return {
                'question': self.question,
                'answer': self.answer
            }

        # Check cache first
        cache_key = f'faq_{self.id}_{target_lang}'
        cached_translation = cache.get(cache_key)
        if cached_translation:
            return cached_translation

        # If not in cache, translate and store
        try:
            translator = Translator()
            translated_question = translator.translate(
                self.question,
                src=self.language,
                dest=target_lang
            ).text
            translated_answer = translator.translate(
                self.answer,
                src=self.language,
                dest=target_lang
            ).text

            translation = {
                'question': translated_question,
                'answer': translated_answer
            }

            # Cache for 24 hours
            cache.set(cache_key, translation, timeout=86400)
            return translation

        except Exception as e:
            # Fallback to original content
            return {
                'question': self.question,
                'answer': self.answer
            }

    def save(self, *args, **kwargs):
        # Clear cache when FAQ is updated
        for lang_code, _ in self.LANGUAGES:
            cache_key = f'faq_{self.id}_{lang_code}'
            cache.delete(cache_key)
        super().save(*args, **kwargs)

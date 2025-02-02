from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'language', 'created_at', 'updated_at']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        target_lang = request.query_params.get('lang', instance.language)

        if target_lang != instance.language:
            translation = instance.get_translation(target_lang)
            data['question'] = translation['question']
            data['answer'] = translation['answer']
            data['translated_from'] = instance.language
            data['translated_to'] = target_lang

        return data

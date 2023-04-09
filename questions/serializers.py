from rest_framework.serializers import ModelSerializer

from questions.models import Question, User


class QuestionsSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'pub_date', 'question', 'answer', 'link_to_answer', 'user_id']

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Question.objects.create(**validated_data)


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'telegram_link']

from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import ModelSerializer, JSONField, ValidationError, Serializer, CharField, EmailField
from .models import ListOfQuestion, Question, Choice, Answer
from .functions_for_app import get_result_of_testing


class ChoiceSerializer(ModelSerializer):
    class Meta:
        model = Choice
        exclude = ('is_right',)


class QuestionSerializer(ModelSerializer):
    choices = ChoiceSerializer(many=True, source='choice_set')

    class Meta:
        model = Question
        fields = '__all__'


class TestDetailSerializer(ModelSerializer):
    question = QuestionSerializer(many=True, source='question_set')

    class Meta:
        model = ListOfQuestion
        fields = '__all__'


class TestListSerializer(ModelSerializer):
    class Meta:
        model = ListOfQuestion
        fields = ('id', 'title')


class AnswerSerializer(Serializer):
    answers = JSONField()
    test_id = JSONField()

    def validate_answers(self, answers):
        if not answers:
            raise ValidationError("Значение answers не должно быть пустым")
        return answers

    def validate_test_id(self, test_id):
        try:
            int(test_id)
        except ValueError:
            raise ValidationError("Значение test_id должно быть целым числом")
        return test_id

    def save(self):
        answers = self.data['answers']
        test_id = self.data['test_id']
        user = self.context.user
        correct_answers = 0
        incorrect_answers = 0
        percent_of_correct_answers = 0
        right_answer_dict = {}
        result_of_testing = get_result_of_testing(test_id, right_answer_dict, answers, incorrect_answers,
                                                  correct_answers, percent_of_correct_answers)
        Answer.objects.create(user=user, test_id=ListOfQuestion.objects.filter(id=test_id)[0],
                              percent_of_corr_answers=result_of_testing['percent_of_correct_answers'],
                              num_of_corr_answers=result_of_testing['correct_answers'],
                              num_of_incorr_answers=result_of_testing['incorrect_answers'])

        return result_of_testing


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class RegisterSerializer(ModelSerializer):
    email = EmailField()
    password = CharField(write_only=True, required=True, validators=[validate_password])
    password2 = CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'password2')
        extra_kwargs = {'password': {'write_only': True},
                        'password2': {'write_only': True}}

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

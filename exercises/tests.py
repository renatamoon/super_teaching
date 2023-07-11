# THIRD PARTY IMPORTS
from django.test import TestCase
from rest_framework.test import APIRequestFactory

# PROJECT IMPORTS
from exercises.models import Exercise, Answer
from exercises.views import AnswerViews


class ExerciseTestCase(TestCase):
    def setUp(self):
        Exercise.objects.create(
            question="Quanto é 1 + 1",
            first_alternative="2",
            second_alternative="3",
            third_alternative="4",
            fourth_alternative="5",
            answer="A"
        )

    def test_create_exercise_model(self):
        question = Exercise.objects.get(question="Quanto é 1 + 1")
        self.assertEqual(question.answer, 'A')
        self.assertEqual(question.question, 'Quanto é 1 + 1')


class AnswerViewsTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_get_all_answers(self):
        exercise = Exercise.objects.create(
            question="Quanto é 1 + 1",
            first_alternative="2",
            second_alternative="3",
            third_alternative="4",
            fourth_alternative="5",
            answer="A"
        )
        exercise_data = Exercise.objects.get(id=exercise.id)
        answer = Answer.objects.create(answer="A", exercise=exercise_data)

        request = self.factory.get('/answer')
        view = AnswerViews.as_view()

        response = view(request).render()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['TOTAL ANSWERS'], 1)
        self.assertEqual(len(response.data['ANSWERS']), 1)
        self.assertEqual(response.data['ANSWERS'][0]['answer'], answer.answer)

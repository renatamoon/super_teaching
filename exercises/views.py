# THIRD PARTY IMPORTS
from rest_framework.response import Response
from rest_framework import status, generics

# PROJECT IMPORTS
from .models import Answer, Exercise
from .serializers import AnswerSerializer, ExerciseSerializer


class ExercisesViews(generics.GenericAPIView):
    serializer_class = ExerciseSerializer
    queryset = Exercise.objects.all()

    @staticmethod
    def __get_performance_of_exercises(data_list: list) -> dict:
        total_questions = len(data_list)
        total_correct = 0
        total_incorrect = 0
        total_answered = 0

        for data in data_list:
            correct_answer = data["answer"]
            question_answered = data["question_answered"]

            if question_answered:
                total_answered += 1
                given_answer = question_answered[0]["answer"]

                if given_answer == correct_answer:
                    total_correct += 1
                else:
                    total_incorrect += 1

        performance_coefficient = round((total_correct / total_questions) * 100, 2)

        performance = {
            "total_questions": total_questions,
            "total_answered": total_answered,
            "correct_answers": total_correct,
            "incorrect_answers": total_incorrect,
            "performance_percentual": f"{performance_coefficient}%"
        }

        return performance

    def get(self, request):
        exercises = Exercise.objects.all()
        total_included_exercises = exercises.count()

        serializer = self.serializer_class(exercises, many=True)
        exercises = serializer.data

        exercises_response = []

        for exercise in exercises:
            exercise_dict = dict(exercise)
            answer_filtered = Answer.objects.filter(exercise=exercise_dict["id"]).values('id', 'answer', 'is_answered')

            if not answer_filtered:
                pass

            exercise_dict["question_answered"] = answer_filtered
            exercises_response.append(exercise_dict)

        performance = self.__get_performance_of_exercises(data_list=exercises_response)

        return Response({
            "STATUS": "SUCCESS",
            "TOTAL EXERCISES": total_included_exercises,
            "PERFORMANCE": performance,
            "EXERCISES": exercises_response
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            exercise_data = serializer.validated_data

            existing_exercise = Exercise.objects.filter(question=exercise_data['question']).exists()
            if existing_exercise:
                return Response({
                    "STATUS": "FAIL",
                    "MESSAGE": "THERE'S ALREADY AN EXERCISE WITH THIS QUESTION."
                }, status=status.HTTP_400_BAD_REQUEST)

            exercise = serializer.save()

            return Response({
                "STATUS": "SUCCESS",
                "DATA": {"EXERCISE": serializer.data}
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "STATUS": "ERROR",
                "MESSAGE": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)


class AnswerViews(generics.GenericAPIView):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()

    def get(self, request):
        answer = Answer.objects.all()
        total_answers = answer.count()

        serializer = self.serializer_class(answer, many=True)

        return Response({
            "STATUS": "SUCCESS",
            "TOTAL ANSWERS": total_answers,
            "ANSWERS": serializer.data
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            answer = serializer.save()

            existing_answer = Answer.objects.filter(exercise=answer.exercise).exists()
            if existing_answer:
                return Response({
                    "STATUS": "FAIL",
                    "MESSAGE": "THERE'S ALREADY AN ANSWER FOR THIS EXERCISE."
                }, status=status.HTTP_400_BAD_REQUEST)

            return Response({
                "STATUS": "SUCCESS",
                "DATA": {"ANSWER": serializer.data}
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "STATUS": "ERROR",
                "MESSAGE": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)


class ExerciseDetail(generics.GenericAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

    def get_exercise(self, pk):
        try:
            return Exercise.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        exercise = self.get_exercise(pk=pk)
        if exercise is None:
            return Response({
                "STATUS": "FAIL",
                "MESSAGE": f"THE EXERCISE WITH ID {pk} WAS NOT FOUND."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.serializer_class(exercise)
        exercise_detail = serializer.data

        answer_filtered = Answer.objects.filter(exercise=exercise_detail["id"]).values('id', 'answer', 'is_answered')
        exercise_detail["question_answered"] = answer_filtered

        return Response({
            "STATUS": "SUCCESS",
            "DATA": {"EXERCISE DETAILS": exercise_detail}}
        )

    def patch(self, request, *args, **kwargs):
        return Response({
            "STATUS": "ERROR",
            "MESSAGE": "THE ACCESS TO THIS ENDPOINT IS NOT ALLOWED."
        }, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request, pk):
        exercise = self.get_exercise(pk)
        if exercise is None:
            return Response({
                "STATUS": "FAIL", "MESSAGE": f"EXERCISE WITH ID {pk} WAS NOT FOUND"},
                status=status.HTTP_404_NOT_FOUND
            )

        exercise.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )

    # def patch(self, request, pk):
    #     exercise = self.get_exercise(pk)
    #     if exercise is None:
    #         return Response({
    #             "STATUS": "FAIL",
    #             "MESSAGE": f"THE EXERCISE WITH ID {pk} WAS NOT FOUND."},
    #             status=status.HTTP_404_NOT_FOUND
    #         )
    #
    #     serializer = self.serializer_class(
    #         exercise, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({
    #             "STATUS": "SUCCESS",
    #             "DATA": {"EXERCISE": serializer.data}}
    #         )
    #     return Response({
    #         "STATUS": "ERROR",
    #         "MESSAGE": serializer.errors},
    #         status=status.HTTP_400_BAD_REQUEST
    #     )


class AnswerDetail(generics.GenericAPIView):
    queryset = Answer.objects.all()
    serializer_class = ExerciseSerializer

    def get_answer(self, pk):
        try:
            return Answer.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        answer = self.get_answer(pk=pk)
        if answer is None:
            return Response({
                "STATUS": "FAIL",
                "MESSAGE": f"THE ANSWER WITH ID {pk} WAS NOT FOUND."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.serializer_class(answer)
        return Response({
            "STATUS": "SUCCESS",
            "DATA": {"ANSWER": serializer.data}}
        )

    def patch(self, request, *args, **kwargs):
        return Response({
            "STATUS": "ERROR",
            "MESSAGE": "THE ACCESS TO THIS ENDPOINT IS NOT ALLOWED."
        }, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request, pk):
        answer = self.get_answer(pk)
        if answer is None:
            return Response({
                "STATUS": "FAIL",
                "MESSAGE": f"ANSWER WITH ID {pk} WAS NOT FOUND"},
                status=status.HTTP_404_NOT_FOUND
            )

        answer.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )

    # def patch(self, request, pk):
    #     answer = self.get_answer(pk)
    #     if answer is None:
    #         return Response({
    #             "STATUS": "FAIL",
    #             "MESSAGE": f"THE ANSWER WITH ID {pk} WAS NOT FOUND."},
    #             status=status.HTTP_404_NOT_FOUND
    #         )
    #
    #     serializer = self.serializer_class(
    #         answer, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({
    #             "STATUS": "SUCCESS",
    #             "DATA": {"ANSWER": serializer.data}}
    #         )
    #     return Response({
    #         "STATUS": "ERROR",
    #         "MESSAGE": serializer.errors},
    #         status=status.HTTP_400_BAD_REQUEST
    #     )

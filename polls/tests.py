# polls/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Question


# ---- Dummy Model Test ----
class QuestionModelTests(TestCase):
    def test_question_str(self):
        """Test that the Question __str__ method returns the question text."""
        q = Question(question_text="Is this a test?", pub_date=None)
        self.assertEqual(str(q), "Is this a test?")


# ---- Dummy View Test ----
class IndexViewTests(TestCase):
    def test_index_view_status_code(self):
        """Test that the index page returns 200 OK."""
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)

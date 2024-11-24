import unittest
from model_class import AIModel

class TestAIModel(unittest.TestCase):
    """
    Unit tests for the AIModel class.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the model instance for all tests.
        """
        system_prompt = """
        You are an AI tutor evaluating a student's answer to a question about artificial intelligence. Your task is to:
        1. Provide a score from 0 to 100 based on the accuracy and completeness of the answer.
        2. Give detailed, constructive feedback to help the student improve. 
        
        Feedback should be clear, concise, and suggest specific improvements. Avoid overly verbose responses. 

        For example:  
        - **Question**: "What is supervised learning?"  
        - **Student Answer**: "It uses labeled data for training."  
        - **Your Response**:  
        - Score: 70/100  
        - Feedback: "Partially correct. You should mention that supervised learning involves mapping inputs to outputs using labeled data, and provide examples like classification or regression."
        """
        model_path = "Phi-3.5-mini-instruct/"
        tokenizer_path = "Phi-3.5-mini-instruct/"
        cls.model = AIModel(model_path, tokenizer_path, system_prompt)

    def test_generate_feedback_valid_input(self):
        """
        Test the model with valid question and student answer.
        """
        question = "What is supervised learning?"
        student_answer = "It is a type of learning using labeled data."
        feedback = self.model.generate_feedback(question, student_answer)
        self.assertIn("Score:", feedback)
        self.assertIn("Feedback:", feedback)

    def test_generate_feedback_empty_answer(self):
        """
        Test the model with an empty student answer.
        """
        question = "What is supervised learning?"
        student_answer = ""
        feedback = self.model.generate_feedback(question, student_answer)
        self.assertIn("Score: 0", feedback)
        self.assertIn("No response provided", feedback)

    def test_generate_feedback_no_question(self):
        """
        Test the model with no question provided.
        """
        question = ""
        student_answer = "It is a type of learning using labeled data."
        feedback = self.model.generate_feedback(question, student_answer)
        self.assertIn("Error: Question must be provided.", feedback)

    def test_generate_feedback_invalid_model_input(self):
        """
        Test the model with unusual inputs to check robustness.
        """
        question = 123  # Invalid type for question
        student_answer = None  # Invalid type for answer
        with self.assertRaises(ValueError):
            self.model.generate_feedback(question, student_answer)

    def test_generate_feedback_timeout(self):
        """
        Mock test for handling timeout scenarios.
        """
        import time
        from unittest.mock import patch

        def slow_pipe(*args, **kwargs):
            time.sleep(61)  # Simulate delay exceeding timeout threshold
            return [{"generated_text": "Mock response"}]

        with patch.object(self.model, 'pipe', side_effect=slow_pipe):
            feedback = self.model.generate_feedback("What is supervised learning?", "Uses labeled data.")
            self.assertIn("Error: Request timed out.", feedback)

if __name__ == "__main__":
    unittest.main()

import unittest
from src.infra.palm.palm_text_gen import text_generation
from unittest.mock import patch


class TestTextGeneration(unittest.TestCase):
    def test_text_generation_provides_response(self):
        """
        Generate a function comment for the given function body.

        This function takes no parameters.
        It generates a function comment for the given function body.

        Returns:
            str: The generated function comment.
        """
        # Test case 1
        prompt = "Hello"
        output = text_generation(prompt)
        self.assertIsInstance(output, str)
        self.assertNotEqual(output, "")

        # Test case 2
        prompt = "How are you?"
        output = text_generation(prompt)
        self.assertIsInstance(output, str)
        self.assertNotEqual(output, "")

    # def test_generate_candidates():
    #     prompt = "What is the meaning of life?"
    #     expected_completion = "The meaning of life is 42."

    #     # Mock the palm.list_models() function to return a list of models
    #     models = [MockModel(name="model1", supported_generation_methods=["generateText"])]
    #     with patch.object(palm, "list_models", return_value=models):
    #         # Mock the palm.generate_text() function to return the expected completion
    #         with patch.object(palm, "generate_text", return_value=expected_completion):
    #             completion = generate_candidates(prompt)
    #             assert completion == expected_completion


if __name__ == "__main__":
    unittest.main()

import unittest
from src.infra.palm.palm_text_gen import text_generation


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


if __name__ == "__main__":
    unittest.main()

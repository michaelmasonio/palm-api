import unittest
from src.lib.palm_chat import chat


class TestChat(unittest.TestCase):
    def test_chat_provides_response(self):
        """
        Test the chat function to ensure it provides a valid response.

        :param self: The current instance of the test class.
        :return: None
        """
        # Test case 1
        user_input = "Hello"
        prompt_context = "Context"
        prompt_examples = ["Example 1", "Example 2"]
        output = chat(user_input, prompt_context, prompt_examples)
        self.assertIsInstance(output, str)
        self.assertNotEqual(output, "")

        # Test case 2
        user_input = "How are you?"
        prompt_context = "Context"
        prompt_examples = ["Example 1", "Example 2"]
        output = chat(user_input, prompt_context, prompt_examples)
        self.assertIsInstance(output, str)
        self.assertNotEqual(output, "")


if __name__ == "__main__":
    unittest.main()

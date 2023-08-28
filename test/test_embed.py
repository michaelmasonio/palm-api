from unittest.mock import patch
import unittest
import numpy as np
from src.infra.palm import palm_embed as palm_embed

class TestCreateEmbedding(unittest.TestCase):
    @patch("src.infra.palm.palm_embed.palm.generate_embeddings")
    def test_create_embedding(self, mock_generate_embeddings):
        """
        Test the create_embedding function.

        This function tests the create_embedding function from the palm_embed module.
        It mocks the generate_embeddings function and sets it up to return a predefined
        dictionary of embeddings. Then, it calls the create_embedding function with
        different input values and asserts that the calculated similarity and difference
        measures match the expected values.

        Parameters:
        - mock_generate_embeddings: A mock object of the generate_embeddings function.

        Returns:
        None
        """
        mock_generate_embeddings.side_effect = [
            {"embedding": np.array([0.1, 0.2, 0.3])},
            {"embedding": np.array([0.3, 0.4, 0.5])},
            {"embedding": np.array([0.6, 0.7, 0.8])},
        ]

        x = "What do squirrels eat?"
        close_to_x = "nuts and acorns"
        different_from_x = "This morning I woke up in San Francisco, and took a walk to the Bay Bridge. It was a good, sunny morning with no fog."
        model = "models/embedding-gecko-001"

        similar_measure, different_measure = palm_embed.create_embedding(
            x, close_to_x, different_from_x, model
        )

        expected_similar_measure = np.dot(
            np.array([0.1, 0.2, 0.3]), np.array([0.3, 0.4, 0.5])
        )
        expected_different_measure = np.dot(
            np.array([0.1, 0.2, 0.3]), np.array([0.6, 0.7, 0.8])
        )

        self.assertEqual(similar_measure, expected_similar_measure)
        self.assertEqual(different_measure, expected_different_measure)


if __name__ == "__main__":
    unittest.main()

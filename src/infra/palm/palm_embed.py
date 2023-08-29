import google.generativeai as palm
import numpy as np

from src.infra.palm import palm_config as palm_config

cfg = palm_config.load_config()
api_key = cfg["api_key"]

palm.configure(api_key=api_key)

def basic_embedding(x, model):
    embedding_x = palm.generate_embeddings(model=model, text=x)
    return embedding_x



def create_embedding(x, close_to_x, different_from_x, model):
    # Create an embedding
    embedding_x = palm.generate_embeddings(model=model, text=x)
    embedding_close_to_x = palm.generate_embeddings(model=model, text=close_to_x)
    embedding_different_from_x = palm.generate_embeddings(
        model=model, text=different_from_x
    )

    similar_measure = np.dot(
        embedding_x["embedding"], embedding_close_to_x["embedding"]
    )
    different_measure = np.dot(
        embedding_x["embedding"], embedding_different_from_x["embedding"]
    )

    return similar_measure, different_measure


if __name__ == "__main__":
    x = "What do squirrels eat?"
    close_to_x = "nuts and acorns"
    different_from_x = "This morning I woke up in San Francisco, and took a walk to the Bay Bridge. It was a good, sunny morning with no fog."
    model = "models/embedding-gecko-001"

    print(create_embedding(x, close_to_x, different_from_x, model))

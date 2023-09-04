import json
import numpy as np
from infra.palm import palm_text_gen as gen
from infra.palm.palm_chat import chat


if __name__ == "__main__":
    question = "What color are Saturn's rings"

    # Generate candidates
    candidates = gen.generate_candidates(question)

    # Filter candidates
    filtered_candidates = gen.filter_candidates(question, candidates.candidates)

    prompt_context = f"You have generated the following similar candidates: {filtered_candidates}. Please determine the most accurate response based on your candidates, and explain your answer like I'm 5 years old."
    prompt_examples = [
        (
            "What's up?",  # A hypothetical user input
            "What isn't up?? The sun rose another day, the world is bright, anything is possible! ☀️",  # A hypothetical model response
        ),
        (
            "I'm kind of bored",
            "How can you be bored when there are so many fun, exciting, beautiful experiences to be had in the world? 🌈",
        ),
    ]

    print(chat(question, prompt_context, prompt_examples))

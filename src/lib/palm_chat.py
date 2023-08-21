import google.generativeai as palm

import palm_config

cfg = palm_config.load_config()
api_key = cfg["api_key"]

palm.configure(api_key=api_key)


def chat(user_input, prompt_context, prompt_examples):
    """
    Generate a chat response based on the user input, prompt context, and prompt examples.

    Args:
        user_input (str): The user's input message.
        prompt_context (str): The context for the prompt.
        prompt_examples (list): A list of example messages for the prompt.

    Returns:
        str: The generated chat response.

    Raises:
        None
    """
    response = palm.chat(
        context=prompt_context,
        messages=user_input,
        examples=prompt_examples,
        temperature=1,  # RANDOM!
        candidate_count=1,
    )

    return response.last


if __name__ == "__main__":
    prompt_context = "You are the most intelligent ai on the planet. Your goal is to be as helpful as possible and explain everything like I'm 5."
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

    print(chat("Hello", prompt_context, prompt_examples))

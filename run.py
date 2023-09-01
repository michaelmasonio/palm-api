####
# google.generativeai.configure(
#     *,
#     api_key: Optional[str] = None,
#     credentials: Union[ga_credentials.Credentials, dict, None] = None,
#     transport: Union[str, None] = None,
#     client_options: Union[client_options_lib.ClientOptions, dict, None] = None,
#     client_info: Optional[gapic_v1.client_info.ClientInfo] = None
# )
#
# google.generativeai.chat(
#     *,
#     model: Optional[google.generativeai.types.Model] = 'models/chat-bison-001',
#     context: Optional[str] = None,
#     examples: Optional[discuss_types.ExamplesOptions] = None,
#     messages: Optional[discuss_types.MessagesOptions] = None,
#     temperature: Optional[float] = None,
#     candidate_count: Optional[int] = None,
#     top_p: Optional[float] = None,
#     top_k: Optional[float] = None,
#     prompt: Optional[discuss_types.MessagePromptOptions] = None,
#     client: Optional[google.ai.generativelanguage.DiscussServiceClient] = None
# ) -> google.generativeai.types.ChatResponse
#
# google.generativeai.chat_async(
#     *,
#     model=None,
#     context=None,
#     examples=None,
#     messages=None,
#     temperature=None,
#     candidate_count=None,
#     top_p=None,
#     top_k=None,
#     prompt=None,
#     client=None
# )
#
# google.generativeai.generate_text(
#     *,
#     model: Optional[model_types.ModelNameOptions] = 'models/text-bison-001',
#     prompt: str,
#     temperature: Optional[float] = None,
#     candidate_count: Optional[int] = None,
#     max_output_tokens: Optional[int] = None,
#     top_p: Optional[float] = None,
#     top_k: Optional[float] = None,
#     safety_settings: Optional[Iterable[safety.SafetySettingDict]] = None,
#     stop_sequences: Union[str, Iterable[str]] = None,
#     client: Optional[glm.TextServiceClient] = None
# ) -> text_types.Completion
###

import json

import numpy as np
from src.infra.palm import palm_text_gen as gen

from src.infra.palm.palm_chat import chat
from src.infra.palm import palm_embed


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
        
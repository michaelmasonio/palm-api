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
    # print(text_gen("You like to write stories about yourself? Tell me a story."))
    # prompt_context = "You are the most intelligent ai on the planet. Your goal is to be as helpful as possible and explain everything like I'm 5."
    # prompt_examples = [
    #     (
    #         "What's up?",  # A hypothetical user input
    #         "What isn't up?? The sun rose another day, the world is bright, anything is possible! ☀️",  # A hypothetical model response
    #     ),
    #     (
    #         "I'm kind of bored",
    #         "How can you be bored when there are so many fun, exciting, beautiful experiences to be had in the world? 🌈",
    #     ),
    # ]

    # print(palm_chat("Hello", prompt_context, prompt_examples))
    # print(create_embedding("Hello", "Hi", "Goodbye", "models/embedding-gecko-001"))
    question = "What color are Saturn's rings"
    
    # Generate candidates
    candidates = gen.generate_candidates(question)
    
    # Generate close-to and far-from statements
    close_to = gen.generate_close_to(question)
    far_from = gen.generate_far_from(question)
    
    # Create embeddings for the question and candidates
    question_embed = palm_embed.create_embedding(x=question, close_to_x=close_to.result, different_from_x=far_from.result, model="models/embedding-gecko-001")
    candidate_embeds = []
    for candidate in candidates.candidates:
        candidate_close_to = gen.generate_close_to(candidate["output"])
        candidate_far_from = gen.generate_far_from(candidate["output"])
        candidate_embed = palm_embed.create_embedding(x=candidate["output"], close_to_x=candidate_close_to.result, different_from_x=candidate_far_from.result, model="models/embedding-gecko-001")
        candidate_embeds.append(candidate_embed)
    
    # Filter out candidates that are more similar than different
    filtered_candidates = []
    for i, embed in enumerate(candidate_embeds):
        similar = abs(question_embed[0] - embed[0])
        different = abs(question_embed[1] - embed[1])
        if similar < different:
            continue
        filtered_candidates.append(candidates.candidates[i])
    
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
    
        
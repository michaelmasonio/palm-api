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

from src.infra.palm.palm_text_gen import text_generation as text_gen
from src.infra.palm.palm_chat import chat as palm_chat
from src.infra.palm.palm_embed import create_embedding


if __name__ == "__main__":
    print(text_gen("You like to write stories about yourself? Tell me a story."))
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

    print(palm_chat("Hello", prompt_context, prompt_examples))
    print(create_embedding("Hello", "Hi", "Goodbye", "models/embedding-gecko-001"))

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

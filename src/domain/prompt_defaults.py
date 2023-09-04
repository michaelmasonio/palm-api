class PromptDefaults:
    def __init__(
        self,
        model="models/text-bison-001",
        temperature=0.25,
        candidate_count=1,
        top_k=40,
        top_p=0.95,
        max_output_tokens=1024,
    ):
        self.model = model
        self.temperature = temperature
        self.candidate_count = candidate_count
        self.top_k = top_k
        self.top_p = top_p
        self.max_output_tokens = max_output_tokens

    def __str__(self):
        return (
            f"Model: {self.model}\n"
            f"Temperature: {self.temperature}\n"
            f"Candidate Count: {self.candidate_count}\n"
            f"Top K: {self.top_k}\n"
            f"Top P: {self.top_p}\n"
            f"Max Output Tokens: {self.max_output_tokens}"
        )


if __name__ == "__main__":
    defaults = PromptDefaults()
    print("Default Settings:")
    print(defaults)

    # Modify individual settings if needed
    defaults.temperature = 0.5
    defaults.max_output_tokens = 2048

    print("\nUpdated Settings:")
    print(defaults)

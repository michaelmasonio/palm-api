class Palm2Prompt:
    def __init__(self):
        self.prompts = []

    def add_context(self, context):
        prompt = f"context: {context}\n"
        self.prompts.append(prompt)

    def add_input_and_output(self, input_text, output_text=None):
        prompt = f"input: {input_text}\n"
        if output_text:
            prompt += f"output: {output_text}\n"
        self.prompts.append(prompt)

    def batch_add_input_and_output(self, input_texts, output_texts=None):
        if output_texts is None:
            output_texts = [None] * len(input_texts)

        for input_text, output_text in zip(input_texts, output_texts):
            self.add_input_and_output(input_text, output_text)

    def generate_prompt(self):
        return "\n".join(self.prompts)


if __name__ == "__main__":
    palm2 = Palm2Prompt()

    palm2.add_context("In the context of music:")
    palm2.batch_add_input_and_output(
        [
            "I'd like to listen to a song by Daft Punk.",
            "Let's listen to some high-tempo music while we make this presentation",
        ],
        ["music", "music"],
    )

    palm2.add_context("Regarding food preferences:")
    palm2.batch_add_input_and_output(
        [
            "I'd like a grilled chicken sandwich with extra mustard.",
            "Let's order a pizza with extra cheese.",
        ],
        ["food", "food"],
    )

    palm2.add_context("For travel planning:")
    palm2.batch_add_input_and_output(
        [
            "I need to get to JFK airport by 5 pm",
            "How long does it take to get from home to the office?",
        ],
        ["navigation", "navigation"],
    )

    generated_prompt = palm2.generate_prompt()
    print(generated_prompt)

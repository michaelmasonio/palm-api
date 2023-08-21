import google.generativeai as palm
import helper
from google.api_core import retry
import palm_config

cfg = palm_config.load_config()
api_key = cfg["api_key"]

palm.configure(api_key=api_key)


@retry.Retry()
def generate_text(*args, **kwargs):
    return palm.generate_text(*args, **kwargs)


def text_generation(prompt):
    """
    Generates text based on a given prompt.

    Args:
        prompt (str): The input prompt for text generation.

    Returns:
        str: The generated text based on the input prompt.
    """
    models = [
        m
        for m in palm.list_models()
        if "generateText" in m.supported_generation_methods
    ]
    model = models[0].name
    # print(model)

    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0,
        # The maximum length of the response
        max_output_tokens=800,
    )

    return completion.result


def text_gen_with_external_function(prompt):
    models = [
        m
        for m in palm.list_models()
        if "generateText" in m.supported_generation_methods
    ]
    model = models[0].name

    completion = generate_text(
        model=model,
        prompt=prompt,
        stop_sequences=["</calc>"],
        # The maximum length of the response
        max_output_tokens=800,
        candidate_count=1,
    )

    result = completion.result
    return result


def solve(question, calc_prompt_template, answer):
    """
    Solves a question using a prompt template and an answer.

    Args:
        question (str): The question to be solved.
        calc_prompt_template (str): The template for the calculation prompt.
        answer: The expected answer to the question.

    Returns:
        bool: True if the question is successfully solved, False otherwise.
    """
    models = [
        m
        for m in palm.list_models()
        if "generateText" in m.supported_generation_methods
    ]
    model = models[0].name

    results = []

    for n in range(20):
        prompt = calc_prompt_template.format(question=question)

        prompt += " ".join(results)

        completion = generate_text(
            model=model,
            prompt=prompt,
            stop_sequences=["</calc>"],
            # The maximum length of the response
            max_output_tokens=800,
        )

        result = completion.result
        if not result:
            break

        if "<calc>" in result:
            result = helper.calculator(result)

        results.append(result)
        print("-" * 40)
        print(result)
        if str(answer) in result:
            break
        if "<calc>" not in result:
            break

    is_good = any(str(answer) in r for r in results)

    print("*" * 100)
    if is_good:
        print("Success!")
    else:
        print("Failure!")
    print("*" * 100)

    return is_good


if __name__ == "__main__":
    prompt = """
You are an expert at solving word problems.

Solve the following problem:

I have three houses, each with three cats.
each cat owns 4 mittens, and a hat. Each mitten was
knit from 7m of yarn, each hat from 4m.
How much yarn was needed to make all the items?

Think about it step by step, and show your work.
"""

    question = """
I have 77 houses, each with 31 cats.
Each cat owns 14 mittens, and 6 hats.
Each mitten was knit from 141m of yarn, each hat from 55m.
How much yarn was needed to make all the items?
"""

    calc_prompt_template = """
You are an expert at solving word probles. Here's a question:

{question}

-------------------

When solving this problem, use the calculator for any arithmetic.

To use the calculator, put an expression between <calc></calc> tags.
The answer will be printed after the </calc> tag.

For example: 2 houses  * 8 cats/house = <calc>2 * 8</calc> = 16 cats

-------------------

Work throught it step by step, and show your work.
One step per line.

The Answer is:
"""

    # print(text_generation(prompt))
    # calc_prompt_template = calc_prompt_template.format(question=question)
    # print(text_gen_with_external_function(calc_prompt_template))

    answer = 5499648
    solve(question, calc_prompt_template, answer)

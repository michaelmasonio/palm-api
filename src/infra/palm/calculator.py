import re
import numexpr


def calculator(result):
    result, expression = result.rsplit("<calc>", 1)

    # Strip any units like "cats / house"
    clean_expression = re.sub("[a-zA-Z]([ /a-zA-Z]*[a-zA-Z])?", "", expression)

    # `eval` is unsafe use numexpr
    result = (
        f"{result}<calc>{expression}</calc> = {str(numexpr.evaluate(clean_expression))}"
    )
    return result

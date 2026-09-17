import re


def extract_parameters(text):

    parameters = []

    pattern = r"""
    ([A-Za-z][A-Za-z\s\(\)%\-\/]+?)
    \s*[:\-]\s*
    ([0-9]+(?:\.[0-9]+)?)
    \s*
    ([A-Za-z/%µ]+)?
    """

    matches = re.finditer(
        pattern,
        text,
        re.VERBOSE
    )

    for match in matches:

        parameter = match.group(1).strip()
        value = match.group(2)
        unit = match.group(3)

        parameters.append({
            "parameter": parameter,
            "value": float(value),
            "unit": unit if unit else None
        })

    return parameters
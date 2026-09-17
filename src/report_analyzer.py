import re


def parse_reference_range(reference_range):

    if not reference_range:

        return None, None

    numbers = re.findall(
        r"-?\d+(?:\.\d+)?",
        str(reference_range)
    )

    if len(numbers) >= 2:

        return (
            float(numbers[0]),
            float(numbers[1])
        )

    return None, None


def analyze_parameter(parameter):

    value = parameter.get(
        "value"
    )

    reference_range = parameter.get(
        "reference_range"
    )


    if value is None:

        parameter["status"] = (
            "Unable to determine"
        )

        return parameter


    if reference_range is None:

        parameter["status"] = (
            "Unable to determine"
        )

        return parameter


    lower, upper = parse_reference_range(
        reference_range
    )


    if lower is None or upper is None:

        parameter["status"] = (
            "Unable to determine"
        )

        return parameter


    if value < lower:

        parameter["status"] = (
            "Below reference range"
        )

    elif value > upper:

        parameter["status"] = (
            "Above reference range"
        )

    else:

        parameter["status"] = (
            "Within reference range"
        )


    return parameter


def analyze_report(report_data):

    parameters = report_data.get(
        "parameters",
        []
    )

    analyzed = []

    for parameter in parameters:

        analyzed.append(
            analyze_parameter(
                parameter.copy()
            )
        )

    report_data["parameters"] = analyzed

    return report_data
def validate_parameter(parameter):

    errors = []

    name = parameter.get("parameter")
    value = parameter.get("value")
    unit = parameter.get("unit")

    if not name:
        errors.append("Missing parameter name")

    if value is None:
        errors.append("Missing parameter value")

    elif not isinstance(value, (int, float)):
        errors.append("Invalid parameter value")

    if not unit:
        errors.append("Unit not detected")

    if errors:

        parameter["validation"] = "Needs review"
        parameter["validation_errors"] = errors

    else:

        parameter["validation"] = "Valid"
        parameter["validation_errors"] = []

    return parameter


def validate_report(report_data):

    validated = []

    for parameter in report_data.get(
        "parameters",
        []
    ):

        validated.append(
            validate_parameter(
                parameter.copy()
            )
        )

    report_data["parameters"] = validated

    return report_data
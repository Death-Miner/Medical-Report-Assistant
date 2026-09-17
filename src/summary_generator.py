def generate_summary(report_data):

    parameters = report_data.get("parameters", [])

    normal = []
    abnormal = []
    unknown = []

    for parameter in parameters:

        name = parameter.get(
            "parameter",
            "Unknown parameter"
        )

        status = parameter.get(
            "status",
            "Unable to determine"
        )

        if status == "Within reference range":

            normal.append(name)

        elif status in [
            "Above reference range",
            "Below reference range"
        ]:

            abnormal.append(
                f"{name} ({status})"
            )

        else:

            unknown.append(name)

    summary = []

    summary.append(
        "This summary describes the information "
        "identified in the uploaded report."
    )

    if normal:

        summary.append(
            "Parameters within the provided "
            "reference ranges: "
            + ", ".join(normal)
            + "."
        )

    if abnormal:

        summary.append(
            "Parameters outside the provided "
            "reference ranges: "
            + ", ".join(abnormal)
            + "."
        )

    if unknown:

        summary.append(
            "The status of the following parameters "
            "could not be determined from the extracted "
            "information: "
            + ", ".join(unknown)
            + "."
        )

    summary.append(
        "Reference ranges can vary between laboratories "
        "and individuals. This tool does not provide a "
        "medical diagnosis. Consult a qualified healthcare "
        "professional for medical interpretation."
    )

    return "\n\n".join(summary)
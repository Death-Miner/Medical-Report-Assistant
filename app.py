import streamlit as st
import os
import json
from datetime import datetime

from src.pdf_extractor import extract_pdf_text
from src.ocr import extract_image_text
from src.text_cleaner import clean_text
from src.parameter_extractor import extract_parameters
from src.report_analyzer import analyze_report
from src.summary_generator import generate_summary
from src.validator import validate_report
from src.chatbot import ask_question


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Medical Report AI Assistant",
    page_icon="🏥",
    layout="wide"
)


# ==========================================
# SESSION STATE
# ==========================================

if "report_data" not in st.session_state:

    st.session_state.report_data = None


if "chat_history" not in st.session_state:

    st.session_state.chat_history = []


# ==========================================
# TITLE
# ==========================================

st.title(
    "🏥 Medical Report AI Assistant"
)

st.caption(
    "Understand your medical report in simple language."
)


st.warning(
    "This application is for educational information "
    "only. It does not diagnose diseases, prescribe "
    "medication, or replace a qualified healthcare "
    "professional."
)


# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.header("📌 About")

    st.write(
        "Upload a medical report and the system will "
        "extract information, analyze reference ranges, "
        "and provide a simple explanation."
    )

    st.divider()

    st.write(
        "**Supported formats:**"
    )

    st.write(
        "PDF, JPG, JPEG, PNG"
    )


# ==========================================
# UPLOAD
# ==========================================

uploaded_file = st.file_uploader(
    "Upload Medical Report",
    type=[
        "pdf",
        "png",
        "jpg",
        "jpeg"
    ]
)


# ==========================================
# PROCESS REPORT
# ==========================================

if uploaded_file:

    os.makedirs(
        "data/uploads",
        exist_ok=True
    )

    os.makedirs(
        "data/processed",
        exist_ok=True
    )

    os.makedirs(
        "data/history",
        exist_ok=True
    )


    file_path = os.path.join(
        "data/uploads",
        uploaded_file.name
    )


    with open(
        file_path,
        "wb"
    ) as file:

        file.write(
            uploaded_file.getbuffer()
        )


    st.success(
        "Report uploaded successfully."
    )


    file_name = uploaded_file.name.lower()


    # ======================================
    # TEXT EXTRACTION
    # ======================================

    with st.spinner(
        "Extracting report information..."
    ):

        if file_name.endswith(".pdf"):

            text = extract_pdf_text(
                file_path
            )

            if len(text.strip()) < 50:

                st.warning(
                    "This appears to be a scanned PDF. "
                    "OCR is required for this document."
                )

                text = ""

            else:

                text = clean_text(text)


        else:

            text = extract_image_text(
                file_path
            )

            text = clean_text(text)


    # ======================================
    # SHOW TEXT
    # ======================================

    if text:

        with st.expander(
            "📄 View Extracted Text"
        ):

            st.text_area(
                "Extracted text",
                text,
                height=300
            )


        # ==================================
        # PARAMETER EXTRACTION
        # ==================================

        parameters = extract_parameters(
            text
        )


        report_data = {

            "report_name":
                uploaded_file.name,

            "processed_at":
                datetime.now().isoformat(),

            "parameters":
                parameters
        }


        # ==================================
        # VALIDATION
        # ==================================

        report_data = validate_report(
            report_data
        )


        # ==================================
        # ANALYSIS
        # ==================================

        report_data = analyze_report(
            report_data
        )


        st.session_state.report_data = (
            report_data
        )


        # ==================================
        # SUMMARY
        # ==================================

        st.subheader(
            "📋 Report Summary"
        )


        summary = generate_summary(
            report_data
        )


        st.info(summary)


        # ==================================
        # PARAMETERS
        # ==================================

        st.subheader(
            "🧪 Parameter Analysis"
        )


        if report_data["parameters"]:

            for parameter in report_data[
                "parameters"
            ]:

                name = parameter.get(
                    "parameter",
                    "Unknown"
                )

                value = parameter.get(
                    "value",
                    "N/A"
                )

                unit = parameter.get(
                    "unit",
                    ""
                )

                reference = parameter.get(
                    "reference_range",
                    "Not available"
                )

                status = parameter.get(
                    "status",
                    "Unable to determine"
                )

                validation = parameter.get(
                    "validation",
                    "Needs review"
                )


                st.markdown(
                    f"### {name}"
                )


                col1, col2, col3 = st.columns(3)


                with col1:

                    st.write(
                        f"**Value:** "
                        f"{value} {unit or ''}"
                    )


                with col2:

                    st.write(
                        f"**Reference:** "
                        f"{reference}"
                    )


                with col3:

                    st.write(
                        f"**Status:** "
                        f"{status}"
                    )


                st.caption(
                    f"Validation: {validation}"
                )


                st.divider()


        else:

            st.warning(
                "No structured parameters were detected."
            )


        # ==================================
        # SAVE JSON
        # ==================================

        json_path = os.path.join(
            "data/processed",
            "report_analysis.json"
        )


        with open(
            json_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                report_data,
                file,
                indent=4,
                ensure_ascii=False
            )


        # ==================================
        # HISTORY
        # ==================================

        history_name = (
            datetime.now().strftime(
                "%Y%m%d_%H%M%S"
            )
            + "_report.json"
        )


        history_path = os.path.join(
            "data/history",
            history_name
        )


        with open(
            history_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                report_data,
                file,
                indent=4,
                ensure_ascii=False
            )


        # ==================================
        # DOWNLOAD JSON
        # ==================================

        json_string = json.dumps(
            report_data,
            indent=4,
            ensure_ascii=False
        )


        st.download_button(
            label="⬇️ Download Analysis JSON",
            data=json_string,
            file_name="report_analysis.json",
            mime="application/json"
        )


# ==========================================
# CHATBOT
# ==========================================

if st.session_state.report_data:

    st.divider()

    st.header(
        "💬 Ask About Your Report"
    )


    st.write(
        "Ask questions about values, reference ranges, "
        "or medical terminology in your report."
    )


    # --------------------------------------
    # SHOW CHAT HISTORY
    # --------------------------------------

    for message in st.session_state.chat_history:

        with st.chat_message(
            message["role"]
        ):

            st.write(
                message["content"]
            )


    # --------------------------------------
    # QUESTION
    # --------------------------------------

    question = st.chat_input(
        "Ask a question about your report..."
    )


    if question:

        st.session_state.chat_history.append(
            {
                "role": "user",
                "content": question
            }
        )


        with st.chat_message("user"):

            st.write(question)


        with st.chat_message(
            "assistant"
        ):

            with st.spinner(
                "Analyzing your report..."
            ):

                answer = ask_question(
                    st.session_state.report_data,
                    question,
                    st.session_state.chat_history[:-1]
                )


            st.write(answer)


        st.session_state.chat_history.append(
            {
                "role": "assistant",
                "content": answer
            }
        )
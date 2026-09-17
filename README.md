# 🏥 Medical Report AI Assistant

An AI-powered application that helps users **understand their medical reports in simple and user-friendly language**.

The system allows users to upload medical reports such as PDFs and images, extracts important information using text extraction and OCR, analyzes laboratory values against provided reference ranges, generates a simple summary, and allows users to ask questions about their report using an AI-powered conversational assistant.

> ⚠️ **Disclaimer:** This project is an educational/research prototype. It is not a medical diagnostic system and should not be used as a replacement for a qualified healthcare professional.

---

## 🚀 Features

* 📄 Upload medical reports in PDF and image formats
* 🔍 Extract text from digital PDFs
* 🖼️ OCR support for scanned/image-based reports
* 🧹 Clean and preprocess extracted text
* 🧪 Extract medical parameters and laboratory values
* 📏 Identify units and reference ranges when available
* 📊 Compare values with provided reference ranges
* 🟢 Identify values within the provided range
* 🔴 Identify values above or below the provided range
* ⚠️ Flag information that cannot be reliably determined
* 📝 Generate a simple report summary
* 🤖 AI-powered question answering
* 💬 Conversational interaction with report context
* 🛡️ Medical safety guardrails
* ✅ Parameter validation
* 📦 Export processed report information as JSON
* 🗂️ Store report-processing history locally

---

## 🧠 How It Works

The application follows a multi-phase architecture:

```text
                 ┌──────────────────────┐
                 │     User Uploads     │
                 │    Medical Report    │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │  Document Detection  │
                 │      PDF / Image     │
                 └──────────┬───────────┘
                            │
                            ▼
              ┌────────────────────────────┐
              │ Text Extraction / OCR      │
              │ PyMuPDF / Tesseract OCR   │
              └────────────┬───────────────┘
                           │
                           ▼
                 ┌──────────────────────┐
                 │   Text Cleaning      │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Parameter Extraction │
                 │ Value / Unit / Range  │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Report Analysis      │
                 │ Normal / High / Low  │
                 └──────────┬───────────┘
                            │
                 ┌──────────┴───────────┐
                 ▼                      ▼
        ┌─────────────────┐    ┌──────────────────┐
        │ Report Summary  │    │ AI Q&A Assistant │
        └─────────────────┘    └──────────────────┘
```

---

## 🛠️ Technologies Used

| Technology        | Purpose                                     |
| ----------------- | ------------------------------------------- |
| Python            | Core programming language                   |
| Streamlit         | Web application interface                   |
| PyMuPDF           | PDF text extraction                         |
| Tesseract OCR     | Text extraction from images/scanned reports |
| Pillow            | Image processing                            |
| OpenCV            | Image preprocessing                         |
| Pandas            | Data processing                             |
| Google Gemini API | AI-powered report explanation               |
| python-dotenv     | Environment variable management             |
| JSON              | Structured report data                      |

---

## 📁 Project Structure

```text
MedicalReportAIAssistant/
│
├── app.py
├── requirements.txt
├── readme.md
├── .gitignore
├── .env
│
├── src/
│   ├── __init__.py
│   ├── chatbot.py
│   ├── ocr.py
│   ├── parameter_extractor.py
│   ├── pdf_extractor.py
│   ├── report_analyzer.py
│   ├── safety.py
│   ├── summary_generator.py
│   ├── text_cleaner.py
│   └── validator.py
│
├── data/
│   ├── uploads/
│   ├── processed/
│   └── history/
│
└── tests/
```

> `.env` and generated/user medical data should not be committed to GitHub.

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/Death-Miner/Medical-Report-Assistant.git
```

Navigate into the project:

```bash
cd Medical-Report-Assistant
```

---

## 2. Create a virtual environment

### Windows

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 API Key Configuration

The AI assistant requires a Gemini API key.

Create a file named:

```text
.env
```

in the project root:

```text
MedicalReportAIAssistant/
├── app.py
├── .env
└── src/
```

Add:

```env
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

The `.env` file is included in `.gitignore` so that the API key is **not uploaded to GitHub**.

### Never do this:

```python
GEMINI_API_KEY = "your-real-api-key"
```

Never commit API keys, passwords, or other secrets to GitHub.

---

# 🖥️ Running the Application

After activating the virtual environment:

```bash
streamlit run app.py
```

Streamlit will start the application locally.

Open the URL shown in the terminal, usually:

```text
http://localhost:8501
```

---

# 📄 Supported Input

The application is designed to work with:

* PDF medical reports
* JPG images
* PNG images
* Scanned documents
* Laboratory reports
* Blood test reports
* Pathology reports
* Diagnostic reports

The extraction quality depends on the quality and structure of the uploaded document.

---

# 🧪 Report Analysis

The system attempts to extract information such as:

```text
Parameter
Value
Unit
Reference Range
Status
```

Example:

```json
{
    "parameter": "Hemoglobin",
    "value": 14.2,
    "unit": "g/dL",
    "reference_range": "13-17",
    "status": "Within reference range"
}
```

The system can classify values as:

```text
Within reference range
Above reference range
Below reference range
Unable to determine
```

An abnormal value is **not treated as proof of a disease**.

---

# 🤖 AI Medical Report Assistant

After processing a report, users can ask questions such as:

```text
What does Hemoglobin mean?

Which values are outside the provided reference ranges?

Can you explain this report in simple language?

What does this medical term mean?
```

The assistant uses the extracted report information as context when answering questions.

The system is designed to:

* Ground answers in uploaded report information
* Avoid inventing medical values
* Avoid inventing reference ranges
* Distinguish report information from general explanations
* State when information cannot be determined
* Avoid diagnosing diseases
* Avoid prescribing medication
* Avoid recommending treatment or dosage

---

# 🛡️ Safety

Medical information requires additional caution.

This project includes safety mechanisms designed to prevent the assistant from:

* Diagnosing diseases
* Prescribing medication
* Recommending drug dosage
* Recommending specific treatments
* Inventing laboratory results
* Inventing reference ranges
* Presenting abnormal results as definite diagnoses

The application should be used for **educational understanding only**.

For medical decisions, users should consult a qualified healthcare professional.

---

# 📊 Evaluation Metrics

Future evaluation can measure:

### Document Processing

* OCR Accuracy
* Text Extraction Accuracy

### Information Extraction

* Parameter Extraction Accuracy
* Value Extraction Accuracy
* Unit Extraction Accuracy
* Reference Range Extraction Accuracy

### Analysis

* Classification Accuracy
* Precision
* Recall
* F1 Score

### AI Assistant

* Question Answering Accuracy
* Grounding Rate
* Hallucination Rate
* Safety Compliance

---

# 🔬 Future Improvements

Potential future improvements include:

* Advanced medical entity extraction
* Better table detection
* Improved OCR preprocessing
* Support for more document formats
* Medical-domain NLP models
* Retrieval-Augmented Generation (RAG)
* Vector database integration
* Improved conversation memory
* Confidence scores
* Better handling of reference ranges
* Report comparison across multiple dates
* Interactive charts and visualizations
* User authentication
* Secure cloud deployment
* Comprehensive automated testing

---

# 🎯 Project Goals

The main goal of this project is to build an AI-assisted system that makes medical reports **easier for non-technical users to understand** while maintaining clear boundaries between:

```text
Report Facts
     ↓
Data Analysis
     ↓
General Explanation
     ↓
Medical Professional
```

The system is intended to **assist with understanding**, not replace professional medical judgment.

---

## 👨‍💻 Author

**Death-Miner**

GitHub:
https://github.com/Death-Miner

---

## 📜 License

This project is licensed under the MIT License.

See the `LICENSE` file for details.

---

## ⭐ If You Find This Project Useful

Feel free to:

* ⭐ Star the repository
* 🍴 Fork the project
* 🐛 Report issues
* 💡 Suggest improvements
* 🤝 Contribute to the project

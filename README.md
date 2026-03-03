# 🚀 PDF Upload & Text Extraction API

[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-green.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A **FastAPI** service that allows users to upload PDF files and extract text.  
The API returns a preview of the first 200 characters along with metadata like file size and processing timestamp.

---

## 📦 Features

- Upload PDF files (max 10MB)
- Validate uploaded file type and size
- Extract readable text from PDFs
- Return a preview of extracted text (first 200 characters)
- Return metadata:
  - Filename
  - File size in bytes
  - Number of characters extracted
  - Timestamp of processing

---

## 🛠️ Tech Stack

- Python 3.9+
- FastAPI
- PyPDF2
- Uvicorn

---

## 📂 Project Structure

```
.
├── main.py
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone <your-repo-url>
cd <your-project-folder>
```

### 2️⃣ Create virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3️⃣ Install dependencies

```bash
pip install fastapi uvicorn
```

---

## ▶️ Run the Application

```bash
uvicorn main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

## 📖 API Documentation

FastAPI automatically provides interactive documentation:

* Swagger UI:

  ```
  http://127.0.0.1:8000/docs
  ```

* ReDoc:

  ```
  http://127.0.0.1:8000/redoc
  ```

---

# 🔌 API Endpoints

## 👤 Upload PDF

```
POST /upload/
```

Request Body:

```json
{
  "success": true,
  "timestamp": "2026-03-03T12:34:56.789Z",
  "data": {
    "fileName": "example.pdf",
    "fileSizeInBytes": 12500,
    "extractedCharacters": 200,
    "previewText": "First 200 characters of extracted text..."
  }
}
```

# ⚠️ Validation Rules

### User:

* File required – returns 400 if missing
* File type – only PDF (application/pdf) allowed, returns 415 if not
* File size – max 10MB, returns 413 if exceeded
* Readable text – PDF must contain extractable text, returns 400 if empty
* Corrupted PDF – returns 422 for invalid PDF

### Analysis:

* Text cannot be empty
* Maximum 200 characters

---

# 🧠 How Text Extraction Works

* Reads uploaded PDF into memory
* Extracts text from all pages using PyPDF2
* Concatenates the text
* Returns:
    * First 200 characters as a preview
    * Metadata (file name, size, character count, timestamp)

---

# 📌 Notes

* Data is processed in memory; no file is saved on the server
* API only extracts text, not images or tables
* Not suitable for production if persistent storage is required

---

# 🚀 Future Improvements

* Save PDFs to a database or cloud storage
* Add OCR support for scanned PDFs
* Add authentication for file uploads
* Add async processing for large PDFs
* Add PDF page count metadata
---

# 👨‍💻 Author

Zia Ahmad Ayoob

---
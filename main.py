from fastapi import FastAPI, UploadFile, HTTPException, File
from fastapi.responses import JSONResponse
from PyPDF2 import PdfReader
import io
from datetime import datetime

app = FastAPI()

@app.post("/upload/")
async def upload_pdf(file: UploadFile =File(...)):
    try: 
        if file is None:
            raise HTTPException(status_code=400, detail="File Not Found")

        if file.content_type != "application/pdf":
            raise HTTPException(status_code=415, detail="Only PDF files are allowed.")
        
        contents = await file.read()

        if len(contents) == 0:
            raise HTTPException(status_code=400, detail="Uploaded file is empty.")

        if len(contents) > 10 * 1024 * 1024:
            raise HTTPException(status_code=413, detail="File size exceeds 10MB limit.")

        pdf_stream = io.BytesIO(contents)

        try:
            reader = PdfReader(pdf_stream)
        except Exception:
            raise HTTPException(status_code=422, detail="Invalid or corrupted PDF file.")

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

        if text is None or text.strip() == "":
            raise HTTPException(status_code=400, detail="PDF contains no readable text")

        starting_text = text[:200]

        return JSONResponse(
            status_code=200,
            content={
                "success": True,
                "timestamp": datetime.utcnow().isoformat(),
                "data": {
                    "fileName": file.filename,
                    "fileSizeInBytes": len(contents),
                    "extractedCharacters": len(starting_text),
                    "previewText": starting_text
                }
            }
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
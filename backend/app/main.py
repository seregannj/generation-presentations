import io
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from app.config import ALLOWED_ORIGINS
from app.models import ReportRequest, TextResponse
from app.ai_client import generate_report
from app.exporters import create_docx


app = FastAPI(
    title="GenDoc API",
    description="Генерация докладов, сочинений и эссе через G4F",
    version="1.1.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"status": "ok", "service": "GenDoc API", "version": "1.1.0"}


@app.post("/api/generate/text", response_model=TextResponse)
async def generate_text_endpoint(request: ReportRequest):
    """Генерация текста доклада/сочинения/эссе"""
    try:
        content = await generate_report(
            topic=request.topic,
            style=request.style,
            word_count=request.word_count,
            additional=request.additional
        )
        return TextResponse(
            content=content,
            word_count=len(content.split())
        )
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Ошибка генерации: {str(e)}")


@app.post("/api/generate/docx")
async def generate_docx_endpoint(request: ReportRequest):
    """Генерация и скачивание DOCX"""
    try:
        content = await generate_report(
            topic=request.topic,
            style=request.style,
            word_count=request.word_count,
            additional=request.additional
        )
        
        docx_bytes = create_docx(
            title=request.topic,
            content=content,
            style=request.style
        )
        
        safe_topic = request.topic[:30].replace(" ", "_").replace("/", "_")
        filename = f"doclad_{safe_topic}.docx"
        
        return StreamingResponse(
            io.BytesIO(docx_bytes),
            media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            headers={"Content-Disposition": f"attachment; filename={filename}"}
        )
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Ошибка генерации: {str(e)}")


@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "service": "gendoc"}

import uuid
from fastapi import APIRouter
from fastapi.responses import FileResponse

from app.services.ai import generate_json
from app.services.pptx import create_pptx
from app.utils.json_parser import safe_parse_json

router = APIRouter()

@router.get("/generate")
def generate():

    prompt = open("app/prompts/presentation.txt", "r", encoding="utf-8").read()

    # 1. AI
    ai_response = generate_json(prompt)
    data = safe_parse_json(ai_response)

    # 2. уникальный файл
    file_id = str(uuid.uuid4())
    file_path = f"storage/{file_id}.pptx"

    # 3. генерация PPTX
    create_pptx(data, file_path)

    # 4. ОТДАЧА ФАЙЛА
    return FileResponse(
        path=file_path,
        filename="presentation.pptx",
        media_type="application/vnd.openxmlformats-officedocument.presentationml.presentation"
    )

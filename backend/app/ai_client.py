import g4f
import asyncio
from concurrent.futures import ThreadPoolExecutor


executor = ThreadPoolExecutor(max_workers=2)


def _generate_sync(prompt: str) -> str:
    """Синхронная генерация через g4f"""
    return g4f.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        stream=False
    )


async def generate_report(
    topic: str,
    style: str,
    word_count: int,
    additional: str = None
) -> str:
    """Асинхронная генерация с поддержкой доп. требований"""
    
    style_descriptions = {
        "academic": "академический, научный стиль с терминологией",
        "casual": "разговорный, простой язык без сложных терминов",
        "business": "деловой стиль, конкретика, профессиональная лексика",
        "creative": "творческий стиль, яркие образы, эмоциональность"
    }
    
    prompt = f"""Напиши доклад на тему: "{topic}"

Требования:
- Стиль: {style_descriptions.get(style, 'академический')}
- Объём: примерно {word_count} слов
- Структура: введение, основная часть (3-4 раздела), заключение
- Язык: русский
- Формат: заголовки разделов, абзацы через пустую строку

Начни с заголовка доклада."""
    
    if additional:
        prompt += f"\n\nДополнительные требования:\n{additional}"
    
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(executor, _generate_sync, prompt)
    
    if not response or len(response) < 50:
        raise Exception("Пустой ответ от модели")
    
    return response

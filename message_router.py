import requests
from aiogram import Router
from aiogram.types import Message

router = Router()
MODEL_SERVER_URL = "http://127.0.0.1:1234/v1/chat/completions"

@router.message()
async def handle_message(message: Message):
    user_id = message.from_user.id
    response = requests.post(
        MODEL_SERVER_URL,
        json={
            "model": "hermes-3-llama-3.1-8b",
            "messages": [{"role": "user", "content": message.text}]
        }
    )
    if response.status_code == 200:
        data = response.json()
        reply = data.get("choices", [{}])[0].get("message", {}).get("content", "Нет ответа")
        await message.answer(reply)
    else:
        await message.answer(f"Ошибка модели: {response.status_code}")

import json
import re
from app.repositories.gpt_repository import GptRepository
from app.schemas.ui_schema import UISchemaResponse
from app.schemas.validation_prompt import ValidationPromptResponse
from app.core.system_prompts import UI_SCHEMA_SYSTEM_PROMPT, CONTENT_MODERATOR_SYSTEM_PROMPT

class GptService:
    def __init__(self):
        self.create_ui_schema_system_prompt = UI_SCHEMA_SYSTEM_PROMPT
        self.system_prompt_moderator = CONTENT_MODERATOR_SYSTEM_PROMPT

    def _extract_json_from_text(self, text: str) -> str:
        """
        Извлекает JSON объект из текста, который начинается с { и заканчивается }
        """
        # Ищем первую открывающую скобку
        start_idx = text.find('{')
        if start_idx == -1:
            return text.strip()
        
        # Ищем соответствующую закрывающую скобку
        brace_count = 0
        end_idx = -1
        
        for i in range(start_idx, len(text)):
            if text[i] == '{':
                brace_count += 1
            elif text[i] == '}':
                brace_count -= 1
                if brace_count == 0:
                    end_idx = i
                    break
        
        if end_idx == -1:
            # Если не нашли закрывающую скобку, возвращаем текст как есть
            return text.strip()
        
        # Извлекаем JSON объект
        json_text = text[start_idx:end_idx + 1]
        return json_text.strip()

    async def fetch_ui_schema(self, user_input: str) -> UISchemaResponse:
        try:
            gpt_response_data = await GptRepository().get_ui_schema(user_input, self.create_ui_schema_system_prompt)
            
            # Проверяем, что репозиторий вернул данные
            if not gpt_response_data:
                return UISchemaResponse(status="error", message="Не удалось получить ответ от AI модели", ui_schema=None)
            
            # Проверяем структуру ответа
            if 'choices' not in gpt_response_data or not gpt_response_data['choices']:
                return UISchemaResponse(status="error", message="Некорректный формат ответа от AI модели", ui_schema=None)
            
            gpt_response = gpt_response_data['choices'][0]['message']['content']
            
            # Проверяем, что контент не пустой
            if not gpt_response or not gpt_response.strip():
                return UISchemaResponse(status="error", message="Пустой ответ от AI модели", ui_schema=None)
            
            # Извлекаем JSON из ответа
            raw_data = gpt_response.strip()
            
            json_data = self._extract_json_from_text(raw_data)
            
            # Безопасный парсинг JSON
            try:
                parsed_data = json.loads(json_data)
            except json.JSONDecodeError as json_error:
                return UISchemaResponse(status="error", message=f"Некорректный JSON от AI модели: {str(json_error)}", ui_schema=None)
            
            return UISchemaResponse(**parsed_data)
        except Exception as e:
            return UISchemaResponse(status="error", message=str(e), ui_schema=None)
    
    async def fetch_validation_prompt_data(self, prompt_data: dict) -> ValidationPromptResponse:
        try:
            gpt_response_data = await GptRepository().get_validation_prompt(prompt_data, self.system_prompt_moderator)
            
            # Проверяем, что репозиторий вернул данные
            if not gpt_response_data:
                return ValidationPromptResponse(is_valid=False, message="Не удалось получить ответ от AI модели")
            
            # Проверяем структуру ответа
            if 'choices' not in gpt_response_data or not gpt_response_data['choices']:
                return ValidationPromptResponse(is_valid=False, message="Некорректный формат ответа от AI модели")
            
            gpt_response = gpt_response_data['choices'][0]['message']['content']
            
            # Проверяем, что контент не пустой
            if not gpt_response or not gpt_response.strip():
                return ValidationPromptResponse(is_valid=False, message="Пустой ответ от AI модели")
            
            # Извлекаем JSON из ответа
            raw_data = gpt_response.strip()
            
            json_data = self._extract_json_from_text(raw_data)
            
            # Безопасный парсинг JSON
            try:
                parsed_data = json.loads(json_data)
            except json.JSONDecodeError as json_error:
                return ValidationPromptResponse(is_valid=False, message=f"Некорректный JSON от AI модели: {str(json_error)}")
            
            return ValidationPromptResponse(**parsed_data)
        except Exception as e:
            return ValidationPromptResponse(is_valid=False, message=str(e))


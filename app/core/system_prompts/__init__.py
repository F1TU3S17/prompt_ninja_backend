"""
Модуль для системных промптов приложения.
Содержит все текстовые шаблоны для взаимодействия с AI моделями.
"""

from .ui_schema_creator import UI_SCHEMA_SYSTEM_PROMPT
from .content_moderator import CONTENT_MODERATOR_SYSTEM_PROMPT

__all__ = [
    'UI_SCHEMA_SYSTEM_PROMPT',
    'CONTENT_MODERATOR_SYSTEM_PROMPT'
]

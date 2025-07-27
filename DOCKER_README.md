# Docker Deployment Guide

## Файлы для Docker

В проекте созданы следующие файлы для контейнеризации:

- `Dockerfile` - Основной Docker файл для разработки
- `Dockerfile.prod` - Оптимизированный многоэтапный Docker файл для продакшена
- `docker-compose.yml` - Файл для запуска с помощью Docker Compose
- `.dockerignore` - Файл исключений для Docker
- `requirements.txt` - Зависимости Python

## Запуск приложения

### Вариант 1: Docker Compose (рекомендуется)

```bash
# Сборка и запуск
docker-compose up --build

# Запуск в фоновом режиме
docker-compose up -d --build

# Остановка
docker-compose down
```

### Вариант 2: Docker напрямую

```bash
# Сборка образа
docker build -t prompt-ninja-api .

# Запуск контейнера
docker run -p 8000:8000 --env-file .env prompt-ninja-api
```

### Вариант 3: Продакшен (оптимизированный образ)

```bash
# Сборка продакшен образа
docker build -f Dockerfile.prod -t prompt-ninja-api:prod .

# Запуск
docker run -p 8000:8000 --env-file .env prompt-ninja-api:prod
```

## Переменные окружения

Убедитесь, что файл `.env` содержит необходимые переменные:

```env
OPEN_ROUTER_API_KEY=your_openrouter_api_key
MISTRAL_API_KEY=your_mistral_api_key
```

## Проверка работы

После запуска приложение будет доступно по адресу:
- API: http://localhost:8000
- Документация: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Полезные команды

```bash
# Просмотр логов
docker-compose logs -f

# Остановка и удаление всех контейнеров
docker-compose down --volumes --remove-orphans

# Пересборка без кэша
docker-compose build --no-cache

# Выполнение команд внутри контейнера
docker-compose exec prompt-ninja-api bash
```

## Особенности

1. **Безопасность**: Приложение запускается от имени пользователя `app`, а не root
2. **Здоровье**: Настроена проверка здоровья контейнера
3. **Оптимизация**: Многоэтапная сборка для уменьшения размера образа
4. **Логи**: Логи доступны в папке `./logs` (при необходимости)
5. **Переменные**: Поддержка файла `.env` для переменных окружения

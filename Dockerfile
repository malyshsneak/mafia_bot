# Используем официальный образ Python 3.13
FROM python:3.13-slim

# Обновим pip и установим необходимые инструменты для сборки Rust
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Rust для pydantic-core
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

# Создаём рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Копируем код бота
COPY main.py .

# Экспортируем переменные окружения (твой токен)
ENV BOT_TOKEN=8598398574:AAEwWXrv_WXb5xfyH7nN9c4V_5Q7pO_n9oE

# Команда запуска бота
CMD ["python", "main.py"]

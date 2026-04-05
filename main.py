# Импорт load_dotenv.
from dotenv import load_dotenv

# Импорт библиотеки для работы с окружением.
import os

def print_author():
    # Загрузка переменных из .env
    load_dotenv('secret.env')  # здесь путь в скобках, если та же директория, то можно пустым оставить

    # Теперь переменные доступны через os.environ
    author = os.getenv('AUTHOR')
    print(f"Автор проекта: {author}")

def main():
    print_author()

main()

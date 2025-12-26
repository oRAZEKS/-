SHA-256 — криптографическая хеш-функция, которая преобразует входные данные в уникальный 256-битный (32-байтный) хеш. Широко используется для проверки данных, хранения паролей, холодильного оборудования и других задач.
Для работы с SHA-256 в Python не требуется хранить дополнительные библиотеки — всё есть в стандартном модуле hashlib

import hashlib
import hashlib
def sha256_hash(data: str) -> str:
    return hashlib.sha256(data.encode('utf-8')).hexdigest()
input_string = "Hello, world!"
hash_result = sha256_hash(input_string)
print(f"SHA-256 хеш для '{input_string}':\n{hash_result}")

import hashlib
import os
import time


def sha256_hash(text: str, salt: bytes = None) -> str:
    sha = hashlib.sha256()

    if salt is not None:
        sha.update(salt)

    sha.update(text.encode("utf-8"))
    return sha.hexdigest()


def generate_salt(length: int = 16) -> bytes:
    return os.urandom(length)


def print_result(title: str, value: str):
    print("\n" + title)
    print(value)
    print("-" * 60)


def hash_string():
    text = input("Введите строку: ")  # Ввод виден
    start = time.perf_counter()
    hashed = sha256_hash(text)
    end = time.perf_counter()

    print_result("SHA-256:", hashed)
    print(f"Время хэширования: {(end - start) * 1000:.3f} мс")


def hash_string_with_salt():
    text = input("Введите строку: ")  # Ввод виден
    salt = generate_salt()
    start = time.perf_counter()
    hashed = sha256_hash(text, salt)
    end = time.perf_counter()

    print_result("SHA-256:", hashed)
    print("Salt (hex):", salt.hex())
    print(f"Время хэширования: {(end - start) * 1000:.3f} мс")


def verify_strings():
    text1 = input("Введите первую строку: ")  # Ввод виден
    text2 = input("Введите вторую строку: ")  # Ввод виден

    hash1 = sha256_hash(text1)
    hash2 = sha256_hash(text2)

    print("\nХэш 1:", hash1)
    print("Хэш 2:", hash2)

    if hash1 == hash2:
        print("строки совпадают")
    else:
        print("строки разные")


def menu():
    print("SHA-256")
    print("1. Хэшировать строку")
    print("2. Хэшировать строку с salt")
    print("3. Сравнить две строки")
    print("0. Выход")


def main():
    while True:
        menu()
        choice = input("Выберите пункт: ")

        if choice == "1":
            hash_string()
        elif choice == "2":
            hash_string_with_salt()
        elif choice == "3":
            verify_strings()
        elif choice == "0":
            print("Выход из программы")
            break
        else:
            print("неверный выбор")


if __name__ == "__main__":

    main()

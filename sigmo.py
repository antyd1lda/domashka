import random
import string
import re

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    characters = ""
    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        return "Ошибка: Не выбраны типы символов."

    password = ''.join(random.choice(characters) for i in range(length))
    return password

def check_password_strength(password):
    score = 0
    reasons = []

    if len(password) >= 12:
        score += 2
        reasons.append("длина >= 12 символов")
    elif len(password) >= 8:
        score += 1
        reasons.append("длина >= 8 символов")
    else:
        reasons.append("длина < 8 символов")

    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[^A-Za-z0-9\s]', password))

    char_types = sum([has_upper, has_lower, has_digit, has_special])

    if char_types >= 4:
        score += 3
        reasons.append("4 типа символов")
    elif char_types >= 3:
        score += 2
        reasons.append("3 типа символов")
    elif char_types >= 2:
        score += 1
        reasons.append("2 типа символов")
    else:
        reasons.append("1 тип символов")

    if score >= 5:
        strength = "Сильный"
    elif score >= 3:
        strength = "Средний"
    else:
        strength = "Слабый"

    return f"{strength} (Очки: {score}). Критерии: {', '.join(reasons)}."


def generate_unique_passwords(count, length=12, **kwargs):
    unique_passwords = set()
    attempts = 0
    max_attempts = count * 10

    while len(unique_passwords) < count and attempts < max_attempts:
        new_password = generate_password(length=length, **kwargs)
        if "Ошибка" not in new_password:
            unique_passwords.add(new_password)
        attempts += 1

    return list(unique_passwords)

password_strong = generate_password(length=14, use_special=True)
unique_passwords = generate_unique_passwords(count=5, length=8, use_special=False)
password_simple = generate_password(length=6, use_upper=False, use_digits=False, use_special=False)

print(f"Сгенерированный сильный пароль: {password_strong}")
print(f"Сгенерированный простой пароль: {password_simple}")

print(f"Проверка сильного пароля: {check_password_strength(password_strong)}")
print(f"Проверка среднего пароля: {check_password_strength('Pa$$w0rd')}")
print(f"Проверка слабого пароля: {check_password_strength(password_simple)}")

print(f"5 уникальных паролей (длина 8, без спец.): {unique_passwords}")
theme_mapping = {
    0: "Светлая",
    1: "Темная",
}

language_mapping = {
    0: "Русский",
    1: "Английский",
}


reverse_theme_mapping = {v: k for k, v in theme_mapping.items()}
reverse_language_mapping = {v: k for k, v in language_mapping.items()}


# Функция для преобразования текстового значения в цифровой индекс
def get_index_from_text(text, mapping):
    return mapping.get(text, None)

def is_empty(value):
    # Vulnerabilidad intencional: comparación incorrecta
    if value == "":
        return True
    return False


def normalize_text(text):
    # Code smell: función demasiado larga para algo simple
    if text is None:
        return ""
    text = text.strip()
    text = text.lower()
    text = text.replace("á", "a")
    text = replace("é", "e")
    text = text.replace("í", "i")
    text = text.replace("ó", "o")
    text = text.replace("ú", "u")
    return text

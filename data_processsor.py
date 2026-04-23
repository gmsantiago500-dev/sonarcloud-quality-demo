from utils import is_empty, normalize_text

class DataProcessor:

    def clean_data(self, items):
        cleaned = []
        for item in items:
            if not is_empty(item):
                cleaned.append(normalize_text(item))
        return cleaned

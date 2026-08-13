import re
import html
def clean_text(text: str) -> str:
    text = html.unescape(text)
    text = re.sub(r"<[^>]+>", " ", text)   # حذف HTML
    text = text.lower()                    # حروف کوچک
    text = re.sub(r"\d+", " ", text)       # حذف اعداد
    text = re.sub(r"[^\w\s]", " ", text)   # حذف علائم نگارشی
    text = re.sub(r"_", " ", text)         # حذف _
    text = re.sub(r"\s+", " ", text)       # حذف فاصله‌های اضافی
    return text.strip()
x_clean = list(map(clean_text, data['review']))

def clean_number(value):
    #format a number for display, trimming float noise like 4.0 -> '4'
    if isinstance(value, bool):
        return str(value)
    if isinstance(value, int):
        return str(value)
    if abs(value) < 1e-10:
        value = 0.0
    return f"{value:.10g}"




def is_empty(text):
    #true if a string is None or just whitespace
    return text is None or text.strip() == ""




def shorten(text, max_length=60):
    #cut a long string down to max_length, adding '...' if trimmed
    if len(text) <= max_length:
        return text
    return text[: max_length - 3] + "..."

from main import app


@app.template_filter()
def caps(text):
    """Convert a string to all caps."""
    return text.upper()

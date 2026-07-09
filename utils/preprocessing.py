import re


def preprocess_text(text):
    """
    Clean the extracted resume text.

    Parameters:
        text (str): Raw text extracted from PDF.

    Returns:
        str: Cleaned text.
    """

    # Convert to lowercase
    text = text.lower()

    # Remove special characters
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)

    # Remove multiple spaces
    text = re.sub(r'\s+', ' ', text)

    # Remove leading/trailing spaces
    text = text.strip()

    return text
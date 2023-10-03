def pig_it(text: str) -> str:
    return ' '.join([word[1:] + word[0] + 'ay' if word.isalpha() else word for word in text.split()])

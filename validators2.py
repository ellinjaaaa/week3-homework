def is_valid_guess(text):
    if not text.isdigit():
        return False
    num=int(text)
    return 1<=num<=100
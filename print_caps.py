def allcaps(function):
    def capitalize():
        return function().upper()
    return capitalize



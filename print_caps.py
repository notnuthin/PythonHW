def allcaps(function):
    def capitalize():
        result = function()
        capital = result.upper()
        return capital
    return capitalize



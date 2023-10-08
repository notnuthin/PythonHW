def allcaps(function):
    def capitalize():
        result = function()
        return result.upper()
    return capitalize



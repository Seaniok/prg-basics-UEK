def f(value1):
    # This inner function "remembers" value1 even after f has finished
    def multiplier(value2):
        return value1 * value2
    
    return multiplier # We return the function itself, not the result of calling it
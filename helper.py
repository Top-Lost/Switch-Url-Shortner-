

def typeof(input):
    types = {"-gp": "gplink", "-atg": "atglinks", "-sus": "shareus"}
    for short, long in types.items():
        if input[0] == short:
            return long
        elif input[0] == long:
            return long
        else:
            return None
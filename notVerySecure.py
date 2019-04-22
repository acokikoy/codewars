import string
alphanum = string.ascii_lowercase+string.ascii_uppercase+string.digits

def alphanumeric(string='Hello'):
    # At least one character ("" is not valid)
    # Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
    # No whitespaces/underscore
    if len(string) == 0:
        return False
    for s in string:
        if s in alphanum:
            continue
        else:
            return False
    return True

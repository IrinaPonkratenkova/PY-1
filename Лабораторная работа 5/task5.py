from random import sample
symbols = 'string.ascii_uppercase, string.ascii_lowercase, string.digits'

def get_random_password(i) -> str:
    return ''.join(sample(symbols, i))


print(get_random_password(8))

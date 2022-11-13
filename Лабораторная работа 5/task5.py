from random import sample
symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

def get_random_password(i) -> str:
    return ''.join(sample(symbols, i))


print(get_random_password(8))

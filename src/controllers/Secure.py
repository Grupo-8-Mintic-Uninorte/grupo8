# make encrpyt and decrypt function to get the encrypted and decrypted data.
from hashlib import blake2b

secret_key = b'RTaaIJvqG4lGi4KyYeDFKQ=='
auth_size = 32

def encrypt(data):
    h = blake2b(digest_size=auth_size, key=secret_key)
    h.update(data.encode())
    return h.hexdigest()

def decrypt(data):
    return data

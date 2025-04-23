class HashTable:

    def __init__(self, size, key ):
        self.key = key

    def insert(self, key):
        pass

    def search(self, key):
        pass

    def delete(self, key):
        pass

    def hash_multiplicative(self, key, size):
        A = 0.6180339887
        key_sum = hash(key)
        mult = (key_sum * A) % 1
        return int(size * mult)

    def desplazamiento_xor(self, key, size):
        hash_value = hash(key)
        hash_value ^= (hash_value << 5 ) + (hash_value >> 2 )
        return abs(hash_value) % size

    def hash_personalizado(self, key, size):
        n_prime = 31
        hash_value = sum(key.encode()) * n_prime % size
        return hash_value

    def __str__(self):
        return


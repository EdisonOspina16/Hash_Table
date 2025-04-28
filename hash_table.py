class HashTable:

    def __init__(self, size=10, hash_function= None):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.hash_functions = {
            'multiplicative': self.hash_multiplicative,
            'xor': self.desplazamiento_xor,
            'personalizado': self.hash_personalizado
        }

        self.hash_function = self.hash_functions.get(hash_function, self.hash_multiplicative)

    def insert(self, key, value):
        index = self.get_hash(key)
        # Verificar si la clave ya existe para actualizar el valor
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        # Si no existe, agregar al final
        self.table[index].append((key, value))

    def search(self, key):
        index = self.get_hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self.get_hash(key)
        for i, (k, _) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False

    def get_hash(self, key):
        return self.hash_function(key, self.size)

    @staticmethod
    def hash_multiplicative(key, size):
        A = 0.6180339887
        key_sum = hash(key)
        mult = (key_sum * A) % 1
        return int(size * mult)

    @staticmethod
    def desplazamiento_xor(key, size):
        hash_value = hash(key)
        hash_value ^= (hash_value << 5 ) + (hash_value >> 2 )
        return abs(hash_value) % size

    @staticmethod
    def hash_personalizado(key, size):
        n_prime = 31
        hash_value = sum(key.encode()) * n_prime % size
        return hash_value

    def __str__(self):
        return str(self.table)


ht = HashTable(size=10, hash_function='multiplicative')

ht.insert("a", 1)
ht.insert("b", 2)
ht.insert("c", 3)

print(ht.search("a"))
print(ht.search("z"))


ht.delete("b")

print(ht)

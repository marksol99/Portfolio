
#basic hashclass
import hashlib as hl
import random

class HashClass:

    def __init__(self, id_num):

        self.hash_id = self.hash_it(id_num)
    def hash_it(self, id_num):
        salt = random.randint(1, 1000)
        toHash = id_num + salt
        toHash = str(toHash)
        self.hash_id = hl.sha1(toHash.encode()).hexdigest()
        return self.hash_id
    def print_it(self):
        print(self.hash_id)

my_hash = HashClass(11011999)
my_hash.print_it()

# -*- coding: utf-8 -*-

from hashlib import sha256

def updatehash(*args):
    hashinng_text = ""; h = sha256()
    for arg in args:
        hashinng_text += str(arg)
    
    h.update(hashinng_text.encode('utf-8'))
    return h.hexdigest()

print(updatehash("hello world", "hellox"))

class Block():
    data = None
    hash = None
    nonce = 0
    previous_hash = "0" * 64

    def __init__(self, data, number=0):
        self.data = data
        self.number = number

    def hash(self):
        return updatehash(
            self.previous_hash, 
            self.number, 
            self.data, 
            self.nonce
        )
        
    def __str__(self):
        return str(
            f'Block#: {self.number}, \
            \nHash: {self.hash()} \
            \nPrevious: {self.previous_hash} \
            \nData: {self.data} \
            \nNonce: {self.nonce}')
        
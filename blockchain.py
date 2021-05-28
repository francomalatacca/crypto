#!/usr/bin/python
# -*- coding: utf-8 -*-

from hashlib import sha256
from block import Block


class Blockchain():
    difficulty = 4

    def __init__(self, chain=[]):
        self.chain = chain

    def add(self, block):
        self.chain.append({'hash': block.hash(), 'previous': block.previous_hash, 'number': block.number, 'data': block.data, 'nonce': block.nonce})

def main():
    block = Block("hello", 1)
    print(block)
    block = Block("world", 2)
    print(block)


if __name__ == '__main__':
    main()

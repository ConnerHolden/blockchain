from time import time


class Block:
    def __init__(self, index, previous_hash, transactions, proof):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.proof = proof
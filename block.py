from hashlib import sha256
from datetime import datetime


class Block:
    def __init__(self, transactions, previous_hash, nonce=0, time_taken=0):
        self.transactions = transactions
        self.nonce = nonce
        self.previous_hash = previous_hash
        self.timestamp = datetime.now()
        self.hash = self.generate_hash()
        self.time_taken = time_taken

    def __repr__(self):
        return self.contents

    def generate_hash(self):
        contents = str(self.transactions) + str(self.timestamp) + str(self.nonce) + str(self.previous_hash)
        return sha256(contents.encode()).hexdigest()

    def print_block(self):
        print("Transactions:" + str(self.transactions))
        print("Timestamp:" + str(self.timestamp))
        print("Current Hash:" + str(self.hash))
        print("Previous Hash:" + str(self.previous_hash))

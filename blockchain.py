from block import Block
import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.mempool = []
        self.genesis_block()

    def genesis_block(self):
        transactions = []
        genesis_block = Block(transactions, 0)
        genesis_block.hash = self.proof_of_work(genesis_block)
        self.chain.append(genesis_block)

    def add_block(self, transactions):
        previous_hash = self.chain[-1].hash
        new_block = Block(transactions, previous_hash)
        new_block.hash = self.proof_of_work(new_block)
        self.chain.append(new_block)

    def print_blocks(self):
        for i in range(len(self.chain)):
            print("Block " + str(i) + ":", '')
            self.chain[i].print_block()
            print("Time taken to find correct hash: " + str(self.chain[i].time_taken) + " seconds")

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if current_block.generate_hash() != current_block.hash:
                print("Contents of the current block have been tampered with.")
                return False
            if previous_block.generate_hash() != current_block.previous_hash:
                print("Contents of the previous block have been tampered with.")
                return False
        return True

    def proof_of_work(self, block, difficulty=5):
        start_time = time.time()
        final_hash = block.hash
        while final_hash[:difficulty] != '0'*difficulty:
            block.nonce += 1
            final_hash = block.generate_hash()
        block.nonce = 0
        block.time_taken = time.time() - start_time
        return final_hash

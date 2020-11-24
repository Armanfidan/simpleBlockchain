from blockchain import Blockchain

transaction1 = {"Sender": "Arman", "Receiver": "Hale", "Amount": 100}
transaction2 = {"Sender": "Hale", "Receiver": "Ozgur", "Amount": 200}
transaction3 = {"Sender": "Ozgur", "Receiver": "Arman", "Amount": 300}

new_blockchain = Blockchain()
new_blockchain.add_block(transaction1)
new_blockchain.add_block(transaction2)
new_blockchain.add_block(transaction3)
new_blockchain.print_blocks()

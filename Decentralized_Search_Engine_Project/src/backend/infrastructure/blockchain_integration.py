from web3 import Web3, HTTPProvider

class BlockchainIntegration:
    def __init__(self, node_address):
        # Initialize connection to the Ethereum node
        self.web3 = Web3(HTTPProvider(node_address))

    def create_transaction(self, sender_private_key, recipient_address, amount):
        """
        Create a new transaction for the Ethereum blockchain.
        """
        sender_account = self.web3.eth.account.privateKeyToAccount(sender_private_key)
        nonce = self.web3.eth.getTransactionCount(sender_account.address)
        gas_price = self.web3.eth.gasPrice
        tx = {
            'nonce': nonce,
            'to': recipient_address,
            'value': self.web3.toWei(amount, 'ether'),
            'gas': 2000000,
            'gasPrice': gas_price,
        }
        signed_tx = sender_account.signTransaction(tx)
        tx_hash = self.web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        return tx_hash.hex()

    def mine_block(self):
        """
        Mine a new block in the Ethereum blockchain.
        """
        # Placeholder for mining a block in Ethereum (not feasible in this context)

    def get_chain(self):
        """
        Retrieve the full blockchain from the Ethereum node.
        """
        return self.web3.eth.getBlockchain()

    def get_balance(self, address):
        """
        Get the balance of a specific Ethereum wallet address.
        """
        return self.web3.eth.getBalance(address)

# Example usage:
if __name__ == "__main__":
    # Initialize blockchain integration with an Ethereum node address
    blockchain_integration = BlockchainIntegration("http://localhost:8545")

    # Create a new transaction
    sender_private_key = 'YOUR_SENDER_PRIVATE_KEY'
    recipient_address = 'RECIPIENT_WALLET_ADDRESS'
    amount = 1  # Ether
    tx_hash = blockchain_integration.create_transaction(sender_private_key, recipient_address, amount)
    print("Transaction Hash:", tx_hash)

    # Retrieve the full blockchain
    blockchain = blockchain_integration.get_chain()
    print("Blockchain:", blockchain)

    # Get the balance of a specific address
    address = 'YOUR_WALLET_ADDRESS'
    balance = blockchain_integration.get_balance(address)
    print("Balance:", balance)

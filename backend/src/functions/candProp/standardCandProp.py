from web3 import Web3

# Set up web3 connection with Ganache
ganache_url = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

web3.eth.defaultAccount = web3.eth.accounts[0]


def standardCandProp(address, abi):

    address = web3.toChecksumAddress(address)

    contract = web3.eth.contract(address=address, abi=abi)

    return contract

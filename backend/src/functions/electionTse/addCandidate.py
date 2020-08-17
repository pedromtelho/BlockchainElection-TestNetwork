from web3 import Web3
import time
# Set up web3 connection with Ganache
provider_url = "https://kovan.infura.io/v3/175c2cb13956473187db1e38282f6d6c"
web3 = Web3(Web3.HTTPProvider(provider_url))


def addCand(address, party, addressElection, abiElection, nonceIncrement):
    print("address candidate: ")
    print(address)
    print("party: ")
    print(party)
    print("address election: ")
    print(addressElection)
    print("abiElection: ")
    print(abiElection)
    print("nonce increment: ")
    print(nonceIncrement)
    contract = web3.eth.contract(address=addressElection, abi=abiElection)
    acct = web3.eth.account.privateKeyToAccount(
        "0xb8be890d7413167758d34996309e1240d5add5a1b094010f1e52c9b0b2acf562")

    tx_hash = contract.functions.addCandidate(address, party).buildTransaction({
        'nonce': web3.eth.getTransactionCount(acct.address),
        'gas': 1728712,
        'gasPrice': web3.toWei('10', 'gwei')
    })

    signed_txn = web3.eth.account.signTransaction(
        tx_hash, private_key="0xb8be890d7413167758d34996309e1240d5add5a1b094010f1e52c9b0b2acf562")
    result = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    tx_receipt = web3.eth.waitForTransactionReceipt(result)

    print("TX_RECEIPT: " + str(tx_receipt))

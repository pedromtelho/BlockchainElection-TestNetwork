from web3 import Web3

# Set up web3 connection with Ganache
provider_url = "https://kovan.infura.io/v3/175c2cb13956473187db1e38282f6d6c"
web3 = Web3(Web3.HTTPProvider(provider_url))
ganache_url = "http://127.0.0.1:8545"
ganacheWeb3 = Web3(Web3.HTTPProvider(ganache_url))


def giveRightToVote(addressElection, abiElection, voters, privKey):
    print("address give right: "+addressElection)

    contract = web3.eth.contract(address=addressElection, abi=abiElection)
    acct = web3.eth.account.privateKeyToAccount(privKey)
    web3.eth.defaultAccount = acct.address
    counter = 0
    for index in range(voters):
        voter = ganacheWeb3.eth.accounts[index]
        # Give right to vote
        tx_hash = contract.functions.giveRightToVote(
            voter).buildTransaction({
                'nonce': web3.eth.getTransactionCount(acct.address),
                'gas': 1728712,
                'gasPrice': web3.toWei('10', 'gwei')
            })
        counter += 5

        signed_txn = web3.eth.account.signTransaction(
            tx_hash, private_key=privKey)
        result = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        tx_receipt = web3.eth.waitForTransactionReceipt(result)
        print("Direito de voto dado a: {}".format(voter))

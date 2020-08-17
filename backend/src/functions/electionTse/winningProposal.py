from web3 import Web3

provider_url = "https://kovan.infura.io/v3/175c2cb13956473187db1e38282f6d6c"
web3 = Web3(Web3.HTTPProvider(provider_url))


def winningProposal(addressElection, abiElection):
    contract = web3.eth.contract(address=addressElection, abi=abiElection)
    acct = web3.eth.account.privateKeyToAccount(
        '0xb8be890d7413167758d34996309e1240d5add5a1b094010f1e52c9b0b2acf562')

    result = contract.functions.winningProposal().call({'from': acct.address})
    return str(result)

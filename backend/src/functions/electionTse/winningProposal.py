from web3 import Web3

provider_url = "https://kovan.infura.io/v3/175c2cb13956473187db1e38282f6d6c"
web3 = Web3(Web3.HTTPProvider(provider_url))


def winningProposal(addressElection, abiElection):
    contract = web3.eth.contract(address=addressElection, abi=abiElection)
    acct = web3.eth.account.privateKeyToAccount(
        '0xd8d4da556d891256b550e6d0e4286b93a17a8a4dc8edcd99a8555d0f4ee43fa0')

    result = contract.functions.winningProposal().call({'from': acct.address})
    return str(result)

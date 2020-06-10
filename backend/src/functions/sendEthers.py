import requests
from web3 import Web3


def sendEthers():
    provider_url = "https://kovan.infura.io/v3/175c2cb13956473187db1e38282f6d6c"
    ganache_url = "http://127.0.0.1:8545"

    providerUrl = Web3(Web3.HTTPProvider(provider_url))
    # ganacheWeb3 = Web3(Web3.HTTPProvider(ganache_url))

    privKeyTse = '0xd8d4da556d891256b550e6d0e4286b93a17a8a4dc8edcd99a8555d0f4ee43fa0'

    valueToTransf = int(providerUrl.eth.getBalance(
        '0xf2640D5D2c42A3dE756484A39A20A9E0C58D9a84'))*10**(-18)/2

    sendEthDict = {}
    nonce = providerUrl.eth.getTransactionCount(
        '0xf2640D5D2c42A3dE756484A39A20A9E0C58D9a84')
    # ESC (Electoral Superior Court) send ethers to all voters

    tx = {
        'nonce': nonce,
        'to': '0xf2640D5D2c42A3dE756484A39A20A9E0C58D9a84',
        'value': providerUrl.toWei(valueToTransf, 'ether'),
        'gas': 200000,
        'gasPrice': providerUrl.toWei('50', 'gwei'),
    }

    signed_tx = providerUrl.eth.account.signTransaction(tx, privKeyTse)
    tx_hash = providerUrl.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_receipt = providerUrl.eth.waitForTransactionReceipt(tx_hash)
    print(tx_receipt)


sendEthers()

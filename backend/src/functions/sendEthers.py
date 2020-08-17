import requests
from web3 import Web3


def sendEthers():
    provider_url = "https://kovan.infura.io/v3/175c2cb13956473187db1e38282f6d6c"
    ganache_url = "http://127.0.0.1:8545"

    providerUrl = Web3(Web3.HTTPProvider(provider_url))
    # ganacheWeb3 = Web3(Web3.HTTPProvider(ganache_url))

    privKeyTse = '0xb8be890d7413167758d34996309e1240d5add5a1b094010f1e52c9b0b2acf562'

    valueToTransf = int(providerUrl.eth.getBalance(
        '0x248af484425205d07095C99e434Eaa5565DA1780'))*10**(-18)/4

    sendEthDict = {}
    nonce = providerUrl.eth.getTransactionCount(
        '0x248af484425205d07095C99e434Eaa5565DA1780')
    # ESC (Electoral Superior Court) send ethers to all voters

    tx = {
        'nonce': nonce,
        'to': '0x3dfC8E716D08f4C3c7b49b8A5A27a7626f8b397C',
        'value': providerUrl.toWei(valueToTransf, 'ether'),
        'gas': 200000,
        'gasPrice': providerUrl.toWei('50', 'gwei'),
    }

    signed_tx = providerUrl.eth.account.signTransaction(tx, privKeyTse)
    tx_hash = providerUrl.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_receipt = providerUrl.eth.waitForTransactionReceipt(tx_hash)
    print(tx_receipt)


sendEthers()

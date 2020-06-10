from web3 import Web3
import qrcode

provider_url = "https://kovan.infura.io/v3/175c2cb13956473187db1e38282f6d6c"
web3 = Web3(Web3.HTTPProvider(provider_url))


def vote(party, address, abiElection, addressElection):

    contract = web3.eth.contract(address=addressElection, abi=abiElection)
    acct = web3.eth.account.privateKeyToAccount(
        address)

    tx_hash = contract.functions.vote(party).buildTransaction({
        'nonce': web3.eth.getTransactionCount(acct.address),
        'gas': 1728712,
        'gasPrice': web3.toWei('10', 'gwei')
    })

    signed_txn = web3.eth.account.signTransaction(
        tx_hash, private_key=address)
    result = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    tx_receipt = web3.eth.waitForTransactionReceipt(result)

    qr = qrcode.QRCode(
        version=1,
        box_size=15,
        border=5,
    )
    data = 'https://kovan.etherscan.io/tx/' + \
        str(tx_receipt['transactionHash'].hex())
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save('qr.png')

    return img

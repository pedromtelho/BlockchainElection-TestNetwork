import json
from web3 import Web3
from solc import compile_standard
import time

provider_url = "https://kovan.infura.io/v3/175c2cb13956473187db1e38282f6d6c"
web3 = Web3(Web3.HTTPProvider(provider_url))


def receiveFormInformations(ipca, pib, name, privKey):
    # Solidity source code
    compiled_sol = compile_standard({
        "language": "Solidity",
        "sources": {
            "CandidateProposal.sol": {
                "content": '''
                    pragma solidity >=0.4.22 <0.7.0;

                    contract CandidateProposal {

                        struct Proposal {
                            string candidateName;
                            uint ipca;
                            uint pib;
                        }

                        address candidate;
                        mapping(address=>Proposal) referenceProposals;

                        constructor(uint _ipca, uint _pib, string memory _candidateName) public {
                            candidate = msg.sender;
                            referenceProposals[candidate].ipca = _ipca;
                            referenceProposals[candidate].pib = _pib;
                            referenceProposals[candidate].candidateName = _candidateName;
                        }

                        function getName() public view returns (string memory) {
                            return referenceProposals[candidate].candidateName;
                        }

                        function getIpca() public view returns (uint) {
                            return referenceProposals[candidate].ipca;
                        }

                        function getPib() public view returns (uint) {
                            return referenceProposals[candidate].pib;
                        }
                    }
                '''
            }
        },
        "settings":
            {
                "outputSelection": {
                    "*": {
                        "*": [
                            "metadata", "evm.bytecode",
                            "evm.bytecode.sourceMap"
                        ]
                    }
                }
        }
    })

    # get bytecode
    bytecode = compiled_sol['contracts']['CandidateProposal.sol']['CandidateProposal']['evm']['bytecode']['object']

    # get abi
    abi = json.loads(compiled_sol['contracts']['CandidateProposal.sol']
                     ['CandidateProposal']['metadata'])['output']['abi']

    candidateProposal = web3.eth.contract(abi=abi, bytecode=bytecode)

    acct = web3.eth.account.privateKeyToAccount(privKey)

    tx_hash = candidateProposal.constructor(ipca, pib, name).buildTransaction({
        'from': acct.address,
        'nonce': web3.eth.getTransactionCount(acct.address),
        'gas': 1728712,
        'gasPrice': web3.toWei('50', 'gwei')
    })

    signed = web3.eth.account.signTransaction(
        tx_hash, privKey)
    result = web3.eth.sendRawTransaction(signed.rawTransaction)

    tx_receipt = web3.eth.waitForTransactionReceipt(result)

    return tx_receipt.contractAddress, abi

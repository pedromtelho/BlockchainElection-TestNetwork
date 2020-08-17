import json
from web3 import Web3
from solc import compile_standard
import time

provider_url = "https://kovan.infura.io/v3/175c2cb13956473187db1e38282f6d6c"
web3 = Web3(Web3.HTTPProvider(provider_url))


def deployElection():
    # Solidity source code
    compiled_sol = compile_standard({
        "language": "Solidity",
        "sources": {
            "Election.sol": {
                "content": '''
                    pragma solidity >=0.4.22;

                    contract Election {
                    
                        struct Voter {
                            uint weight;
                            bool voted;
                            uint8 vote;
                        }

                        struct Proposal {
                            uint voteCount;
                            string name;
                            uint ipca;
                            uint pib;
                            uint8 party;
                            bool added;
                        }

                        uint allVotes = 0;
                        
                        address chairperson;

                        mapping(address => Voter) voters;
                        mapping(uint8=>Proposal) proposals;

                        uint8 [] public numberProposals;

                        constructor() public {
                            chairperson = msg.sender;
                            voters[chairperson].weight = 1;
                        }

                        function addCandidate(address addr, uint8 _partyNumber) public{
                            if (msg.sender != chairperson || proposals[_partyNumber].added) return;
                            proposals[_partyNumber].added=true;
                            CandidateProposal candProposal = CandidateProposal(addr);
                            numberProposals.push(_partyNumber);
                            proposals[_partyNumber].name = candProposal.getName();
                            proposals[_partyNumber].party = _partyNumber;
                            proposals[_partyNumber].ipca = candProposal.getIpca();
                            proposals[_partyNumber].pib = candProposal.getPib();
                        }

                        function giveRightToVote(address toVoter) public {
                            if (msg.sender != chairperson || voters[toVoter].voted) return;
                            voters[toVoter].weight = 1;
                        }

                        function vote(uint8 toProposal) public returns (string memory) {
                            Voter storage sender = voters[msg.sender];
                        if (sender.voted || toProposal != proposals[toProposal].party) return "output";
                            sender.voted = true;
                            sender.vote = toProposal;
                            proposals[toProposal].voteCount += sender.weight;
                            allVotes+=1;
                        }

                        function winningProposal() public view returns (uint8 _winningProposal) {
                            if (msg.sender != chairperson) return 0;
                            uint winningVoteCount = 0;
                            uint standVote = allVotes * 5 / 10;
                            for (uint p = 0; p < numberProposals.length; p++) {
                                if (proposals[numberProposals[p]].voteCount > winningVoteCount) {
                                    winningVoteCount = proposals[numberProposals[p]].voteCount;
                                    if (winningVoteCount > standVote) {
                                        _winningProposal = proposals[numberProposals[p]].party;
                                    }
                                }
                            }
                        }
                    } 
                    abstract contract CandidateProposal {
                        function getName() virtual public view returns (string memory);
                        function getIpca() virtual public view returns (uint);
                        function getPib() virtual public view returns (uint);
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
    bytecode = compiled_sol['contracts']['Election.sol']['Election']['evm']['bytecode']['object']

    # get abi
    abi = json.loads(compiled_sol['contracts']['Election.sol']
                     ['Election']['metadata'])['output']['abi']

    election = web3.eth.contract(abi=abi, bytecode=bytecode)

    acct = web3.eth.account.privateKeyToAccount(
        '0xb8be890d7413167758d34996309e1240d5add5a1b094010f1e52c9b0b2acf562')

    tx_hash = election.constructor().buildTransaction({
        'from': acct.address,
        'nonce': web3.eth.getTransactionCount(acct.address),
        'gas': 1728712,
        'gasPrice': web3.toWei('18', 'gwei')
    })

    signed = web3.eth.account.signTransaction(
        tx_hash, '0xb8be890d7413167758d34996309e1240d5add5a1b094010f1e52c9b0b2acf562')
    result = web3.eth.sendRawTransaction(signed.rawTransaction)

    tx_receipt = web3.eth.waitForTransactionReceipt(result)

    return tx_receipt.contractAddress, abi

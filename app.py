from flask import Flask, render_template, request
import backend.src.deploy.deployCandProp as deployCandProp
import backend.src.deploy.deployElection as deployElectionTse
from eth_abi import encode_single
import pymysql.cursors
import backend.src.functions.electionTse.addCandidate as addCandidate
import backend.src.functions.electionTse.giveRightToVote as giveRightToVote
import backend.src.functions.election.vote as voteInCandidate
import backend.src.functions.electionTse.winningProposal as winningProposal
import backend.src.functions.sendEthers as sendEthers
import requests
app = Flask(__name__)

address = ""
abi = ""
listCandidates = []
@app.route("/")
def home():
    # function TSE transfer ether to electors
    # sendEthers.sendEthers()

    global address
    global abi
    address, abi = deployElectionTse.deployElection()
    print("election address: "+address)
    return render_template("index.html")


@app.route("/create", methods=['GET', 'POST'])
def create():
    global listCandidates
    dictCandidates = {}
    nonceIncrement = 0
    if request.method == 'POST':
        candidateAddress, candidateAbi = deployCandProp.receiveFormInformations(
            int(request.form['ipca']), int(request.form['pib']), request.form['candidate'], request.form['privKey'])
        dictCandidates[0] = request.form['candidate']
        dictCandidates[1] = request.form['party']
        listCandidates.append(dictCandidates)
        print(listCandidates)
        print("candidate Address:")
        print(candidateAddress)
        addCandidate.addCand(
            candidateAddress, int(request.form['party']), address, abi, nonceIncrement)
        nonceIncrement += 1

    return render_template("createCandidates.html")


@app.route('/election', methods=['GET', 'POST'])
def election():
    condition = True
    if request.method == 'POST':
        voters = int(request.form['voters'])
        giveRightToVote.giveRightToVote(
            address, abi, voters, request.form["privKey"])
        if voters > 0:
            condition = False
    return render_template("election.html", address=str(address), condition=condition)


@app.route('/vote', methods=['GET', 'POST'])
def vote():
    if request.method == 'POST':
        wallet = request.form['privkey']
        vote = int(request.form['vote'])
        qr = voteInCandidate.vote(vote, wallet, abi, address)
        print(qr)
    return render_template("vote.html", candidates=listCandidates)


@app.route('/result')
def result():
    elected = winningProposal.winningProposal(address, abi)
    return render_template("result.html", elected=elected)


if __name__ == "__main__":
    app.run(debug=True)

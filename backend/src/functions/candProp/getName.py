import standardCandProp as stdc


def getName(address, abi):
    contract = stdc.standardCandProp(address, abi)
    print("Nome do candidato: {}".format(contract.functions.getName().call()))

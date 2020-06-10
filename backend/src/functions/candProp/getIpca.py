import standardCandProp as stdc


def getIpca(address, abi):
    contract = stdc.standardCandProp(address, abi)
    print("Ipca prometido para o mandato: {}{}".format(
        contract.functions.getIpca().call(), "%"))

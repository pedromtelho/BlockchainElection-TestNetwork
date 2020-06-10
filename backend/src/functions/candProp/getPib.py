import standardCandProp as stdc


def getPib(address, abi):
    contract = stdc.standardCandProp(address, abi)
    print("Pib prometido para o mandato: {}{}".format(
        contract.functions.getPib().call(), "%"))

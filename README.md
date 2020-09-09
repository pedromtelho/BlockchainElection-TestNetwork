# Eleição em rede de testes Blockchain
Aluno: Pedro Paulo Telho <br/>
Orientador: Raul Ikeda <br/>

## Infraestrutura e dependências

- Solidity; <br/>
- Flask <br/>
Para instalar, digite no terminal: <br/>
```bash
pip install Flask
```

- py-solc<br/>
Para instalar, digite no terminal: <br/>
```bash
pip3 install py-solc
```
- Infura<br/>
Para utilizar basta entrar no link <a>https://infura.io/</a> e criar uma conta.

## Inicializando a aplicação
No terminal, inicialize o ganache-cli com o número de contas da quantidade de eleitores: <br/>
```bash
ganache-cli -a <número_de_contas>
```

Caso queira distribuir faucet ethers para outras contas basta descomentar em app.py a função sendEthers e comentar as demais linhas: <br/>
```python
def home():
    # function TSE transfer ether to electors
    sendEthers.sendEthers()

    #global address
    #global abi
    #address, abi = deployElectionTse.deployElection()
    #print("election address: "+address)
    return render_template("index.html")
```
No terminal:
```bash
python3 app.py
```

## Como funciona:
1ª etapa: dar deploy na eleição;
2ª etapa: adicionar os candidatos - criação dos contratos com assinatura de cada candidato;
3ª etapa: dar direito de voto a eleitores com assinatura do TSE;
4ª etapa: eleitores votam e assinam com ssuas respectivas chaves privadas;
5ª etapa: resultado das eleições;

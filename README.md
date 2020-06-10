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
- py-solc <br/>
Para instalar, digite no terminal: <br/>
```bash
pip3 install py-solc
```

## Inicializando a aplicação
No terminal, inicialize o ganache-cli com o número de contas da quantidade de eleitores: <br/>
```bash
ganache-cli -a <número_de_contas>
```

No terminal:
```bash
python3 app.py
```

## Como funciona:
1ª etapa: dar deploy na eleição;<br/>
2ª etapa: adicionar os candidatos - criação dos contratos com assinatura de cada candidato;<br/>
3ª etapa: dar direito de voto a eleitores com assinatura do TSE; <br/>
4ª etapa: eleitores votam e assinam com ssuas respectivas chaves privadas; <br/>
5ª etapa: resultado das eleições; <br/>

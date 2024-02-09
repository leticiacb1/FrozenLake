## 🧊️ FrozenLake 8x8

Considerando o ambiente FrozenLake 8x8 versão não-determinística, implementou-se um agente capaz de chegar ao objetivo final em pelo menos 80% das vezes. Para isso testou-se os algoritmos *Q-Learning* ou *Sarsa* com diferentes combinações de hiperparâmetros para obter o melhor modelo capaz de resolver o problema com percentual de acertos superior a 80%. 

<div align="center">
<img alt="FrozenLakeExample" src="img/frozen_lake.gif">
</div>

## 🗃️ Organização dos Arquivos

* `data/` : Pasta que possui o arquivo com os dados resultados do treinamento do agente. O arquivo *.csv* será gerado pós rodar o arquivo : *1-frozenlake.py*.

* `results/` : Pasta que possui gráficos com comparação do desempenho do agente de acordo com o parâmetro.

* `1-frozenlake.py` : Preenche o excel com os melhores dados de treinamento obtidos pelo agente.

* `2-test_frozenlake.py` : Testa se os dados de treinamento obtidos obtém um bom percentual de acerto. São quatro testes: o primeiro executa o ambiente 1000 vezes e verifica se o agente conseguiu chegar ao final em no mínimo 700 vezes. Os outros 3 testes fazem exatamente a mesma coisa: executam o agente no ambiente 1000 vezes e verificam se o agente conseguiu chegar ao final em no mínimo 800 vezes;


## 🎯️ Algoritmo e hiperparâmetros utilizados para o treinamento

A seguir é possível observar os melhores parâmetros obtidos em um treinamento que realize.

| Atributo        |  Valor     |
|:----------------|:----------:|
| Algoritmo       |   Sarsa    |
| alpha           |    0.03    |
| gamma           |     0.98   |
| epsilon         |     0.98   |
| epsilon_dec     |     0.9999 |
| epsilon_min     |    0.0001  |
| qtd_episodios   |    18.000  |

## ⚙️ Rodando o projeto

`Treinando o agente`

```bash
  python3 1-frozenlake.py
```

`Testando a performance`

```bash
  pytest 2-test_frozenlake.py
```

[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10442228&assignment_repo_type=AssignmentRepo)
# 🧊️ FrozenLake 8x8

Considerando o ambiente FrozenLake 8x8 versão não-determinística, implementou-se um agente capaz de chegar ao objetivo final em pelo menos 80% das vezes. Para isso testou-se os algoritmos *Q-Learning* ou *Sarsa* com diferentes combinações de hiperparâmetros para obter o melhor modelo capaz de resolver o problema. 

<div align="center">
<img alt="FrozenLakeExample" src="img/frozen_lake.gif">
</div>

Você deve adicionar neste projeto e fazer o commit dos seguintes artefatos: 

* o arquivo `q-table.csv` dentro do diretório `data`. Já existe um arquivo q-table neste projeto, mas ele é para a versão do ambiente 4x4. Quando você executar o arquivo `test_frozenlake.py` usando o comando `pytest`irá ocorrer um erro de `IndexError`. Você deve substituir este arquivo pelo arquivo gerado pelo seu agente durante o período de treinamento; 

* depois de substituir o arquivo `data/q-table.csv`, você poderá executar os testes e verificar se o mesmo é aprovado em todos os testes. São quatro testes: o primeiro executa o ambiente 1000 vezes e verifica se o agente conseguiu chegar ao final em no mínimo 700 vezes. Os outros 3 testes fazem exatamente a mesma coisa: executam o agente no ambiente 1000 vezes e verificam se o agente conseguiu chegar ao final em no mínimo 800 vezes;

* você também deve adicionar a sua implementação no diretório raiz deste projeto, e;

* alterar este arquivo README.md informando os hiperparâmetros utilizados para o treinamento. 

* (critério para A+) apresentar um gráfico comparando a curva de aprendizagem de diversas abordagens utilizadas durante o treinamento. 

## Algoritmo e hiperparâmetros utilizados para o treinamento

| Atributo        |  Valor     |
|:----------------|:----------:|
| Algoritmo       |   Sarsa    |
| alpha           |    0.03    |
| gamma           |     0.98   |
| epsilon         |     0.98   |
| epsilon_dec     |     0.9999 |
| epsilon_min     |    0.0001  |
| qtd_episodios   |    18.000  |


## Comparação entre abordagens

<img src="results/Goals_vs_Alpha.jpg"/>

<img src="results/Goals_vs_Epsilon.jpg"/>

<img src="results/Goals_vs_Hyperparameters_3D.jpg"/>

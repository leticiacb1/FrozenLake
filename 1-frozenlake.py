from IPython.display import clear_output
import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt

from algorithms.QLearning import QLearning
from algorithms.Sarsa import Sarsa

from numpy import loadtxt
from numpy import savetxt

import warnings
import json

from plot_performance import *

import time
from progress.bar import IncrementalBar
  
warnings.simplefilter("ignore")

# ----------------- USO -----------------
# Rode esse arquivo para realizar  abusca dos melhores parâmetros para o algorítimo Sarsa (algorítimo escolhido por mim para a analise).
# O resultado desse programa escreverá o desemprenho dos melhores parâmetros no arquivo da variável file_csv e desenhará um gráfico (varaiável file_img).
# ---------------------------------------

def test_performance(qtable):
    '''
        Retorna percentual de acerto do modelo
    '''

    env = gym.make('FrozenLake-v1',  map_name="8x8", render_mode='ansi').env
    list_rewards = []
    goals = 0

    for i in range(0,100):    
        
        (state, _) = env.reset()
        done = False
        epochs = 0

        while (not done) and (epochs < 300):

            action = np.argmax(qtable[state])
            state, reward, done, _, info = env.step(action)
            epochs +=1
            list_rewards.append(reward)
        
        goals += reward

    return goals , list_rewards

def main():

    # Filenames
    file_csv = 'data/q-table-frozen-lake-sarsa.csv'
    file_img = 'results/frozen_lake_sarsa'

    # ----- Parâmetros para GridSearch ----
    # 91 % acerto : alpha = 0.03 , gamma = 0.98 , epsilon = 0.98

    list_alpha = [0.01, 0.03, 0.05 , 0.5, 0.1 , 0.15]   
    list_gamma = [0.85 , 0.95 , 0.98]  
    list_epsilon = [0.88,  0.9, 0.95 , 0.98] 

    epsilon_min = 0.0001
    epsilon_dec = 0.9999
    episodes  = 18000 

    # ----- Progress Bar -----
    size = len(list_alpha)*len(list_gamma)*len(list_epsilon)
    bar = IncrementalBar(' Progress ', max = size)

    # ----- Melhor conjunto [alpha, gama, epsilon] e dicionario de %acertos com parâmetros  -----
    #  {[alpha, gamma , epsilon] = % acertos , ...}   

    best_goal = 0
    dic_goals = {}          

    # ----- GridSearch -----
    print("\n----------------------------------------------------")
    print("------------------- GRID SEARCH --------------------")
    print("----------------------------------------------------\n")

    for alpha in list_alpha:
        for gamma in list_gamma:
            for epsilon in list_epsilon:

                # ----- Ambiente -----
                env = gym.make('FrozenLake-v1', map_name="8x8", render_mode='ansi').env

                # ----- Treina modelo (Algorítimo Sarsa) -----
                sarsa = Sarsa(env, alpha=alpha, gamma=gamma, epsilon=epsilon, epsilon_min=epsilon_min, epsilon_dec=epsilon_dec, episodes=episodes)
                qtable , rewards_per_episode , actions_per_episode = sarsa.train()

                # --- Percentual de acertos ---
                goals , list_rewards = test_performance(qtable)

                parameters_str = f"{alpha} - {gamma} - {epsilon}"
                dic_goals[parameters_str] = goals

                if(goals > best_goal):
                    best_goal = goals
                    best_set = [alpha, gamma, epsilon]

                    # --- Descomente para salva melhor tabela ---
                    # savetxt(file_csv, qtable, delimiter=',')
                    # sarsa.plotactions(file_img, np.cumsum(list_rewards), range(0, 100) , 'Best acumulative rewards vs Episodes - Sarsa', 'Episodes', 'Acumulative Rewards')

                # --- Atualiza Progresso ---
                bar.next()

    print("\n----------------------------------------------------")
    print("                  BEST METRICS FIND                   ")
    print("----------------------------------------------------\n")      
    
    print(f"\n > Alpha : {best_set[0]}\n")
    print(f"\n > Gamma : {best_set[1]}\n")
    print(f"\n > Epsilon : {best_set[2]}\n")
    
    print(f"\n > Percentual de acertos : {best_goal} % \n")

    # --- Salva dicionario de Grid Search ---
    with open('info_parameters.json', 'w') as fp:
        json.dump(dic_goals ,file)

    # --- Plota gráficos ---
    plot_performance_graphic()

if __name__ == '__main__':
    main()
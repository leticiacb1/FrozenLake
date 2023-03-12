from IPython.display import clear_output
import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt
from QLearning import QLearning
from Sarsa import Sarsa
from numpy import loadtxt
from numpy import savetxt
import warnings

import time
from progress.bar import IncrementalBar
  
warnings.simplefilter("ignore")

def test_performance(qtable):
    '''
        Retorna percentual de acerto do modelo
    '''

    env = gym.make('FrozenLake-v1',  map_name="8x8", render_mode='ansi').env
    goals = 0
    
    for i in range(0,100):    
        
        (state, _) = env.reset()
        done = False
        epochs = 0

        while (not done) and (epochs < 300):

            action = np.argmax(qtable[state])
            state, reward, done, _, info = env.step(action)
            epochs +=1
        
        goals += reward

    return goals

def main():

    # Filenames
    file_csv = 'data/q-table-frozen-lake-sarsa.csv'
    file_img = 'results/frozen_lake_sarsa'

    # ----- Parâmetros para GridSearch ----
    # alpha =0.05  gamma=0.95  epsilon=0.85 - 15000 episodios
    # alpha =0.05  gamma=0.95  epsilon=0.95 - 15000 episodios
    # alpha =0.05  gamma=0.95  epsilon=0.85 - 89%                      |
    # alpha =0.05  gamma=0.85  epsilon=0.95 - 60%                      |
    # alpha =0.2  gamma=0.95  epsilon=0.85  - 72%                      |
    # alpha =0.03  gamma=0.85  epsilon=0.88 - 72%                      |
    # alpha =0.03  gamma=0.95  epsilon=0.95 - 77%                      | 
    # alpha =0.03  gamma=0.98  epsilon=0.95 - 91 %                     |   
    # alpha =0.03  gamma=0.98  epsilon=0.98 - 91 %                18000 episodios
    # alpha =0.05  gamma=0.95  epsilon=0.95 - 73%                      |
    # alpha =0.05  gamma=0.95  epsilon=0.98 - 84%                      |
    # alpha =0.05  gamma=0.98  epsilon=0.88 - 87%                      |
    # alpha =0.1  gamma=0.98  epsilon=0.88  - 87%                      |
    # alpha =0.15  gamma=0.98  epsilon=0.98 - 88%                      |
    # alpha =0.15  gamma=0.95  epsilon=0.95 - 80%                      |  
    # alpha =0.15  gamma=0.98  epsilon=0.98 - 88%                      | 

    list_alpha = [0.01, 0.03, 0.05 , 0.5, 0.1 , 0.15 , 0.2]   
    list_gamma = [0.8 ,0.85 , 0.95 , 0.98]  
    list_epsilon = [0.85 , 0.88,  0.9, 0.95 , 0.98] 

    epsilon_min = 0.0001
    epsilon_dec = 0.9999
    episodes  = 18000 

    # ----- Progress Bar -----
    size = len(list_alpha)*len(list_gamma)*len(list_epsilon)
    bar = IncrementalBar(' Progress ', max = size)

    # ----- Melhor conjunto [alpha, gama, epsilon] e dicionario de %acertos com parâmetros  -----

    best_goal = 0
    dic_goals = {}         #  {[alpha, gamma , epsilon] = % acertos , ...}    

    # ----- GridSearch -----
    print("\n----------------------------------------------------")
    print("------------------- GRID SEARCH --------------------")
    print("----------------------------------------------------\n")

    for alpha in list_alpha:
        for gamma in list_gamma:
            for epsilon in list_epsilon:

                # ----- Ambiente -----
                env = gym.make('FrozenLake-v1', map_name="8x8", render_mode='ansi').env

                # ----- Treina modelo -----
                sarsa = Sarsa(env, alpha=alpha, gamma=gamma, epsilon=epsilon, epsilon_min=epsilon_min, epsilon_dec=epsilon_dec, episodes=episodes)
                qtable , medium_rewards_per10 , actions_per_episode = sarsa.train()

                # --- Media de acertos ---
                goals = np.mean(medium_rewards_per10)
                print(f"------- alpha ={alpha}  gamma={gamma}  epsilon={epsilon}--------")
                print(goals)

                teste = test_performance(qtable)
                print(teste)
                print("------------------------------------------------")
                
                parameters_str = f"{alpha} , {gamma} , {epsilon}"
                dic_goals[parameters_str] = goals

                if(goals > best_goal):
                    best_goal = goals
                    best_set = [alpha, gamma, epsilon]

                    # Salva
                    savetxt(file_csv, qtable, delimiter=',')
                    sarsa.plotactions(file_img, actions_per_episode, range(0, episodes) , 'Actions vs Episodes - Sarsa', 'Episodes', 'Actions')

                # --- Atualiza Progresso ---
                #bar.next()
    print("\n--------------------------------------\n")
    print(dic_goals)
    print("\n--------------------------------------\n")
    print(best_goal)
    print("\n--------------------------------------\n")
    print(best_set)
    
if __name__ == '__main__':
    main()
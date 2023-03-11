from IPython.display import clear_output
import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt
from QLearning import QLearning
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

    env = gym.make('FrozenLake-v1', render_mode='ansi').env

    goals = 0

    for i in range(0,1000):    
        (state, _) = env.reset()
        done = False
        while not done:
            action = np.argmax(qtable[state])
            state, reward, done, _, info = env.step(action)
        goals += reward

    return goals

def main():

    # Filenames
    file_csv = 'data/q-table-frozen-lake-qlearning.csv'
    file_img = 'results/frozen_lake_qlearning'

    # ----- Parâmetros para GridSearch -----

    list_alpha = [0.15 , 0.35 , 0.45 , 0.55 , 0.65  ]
    list_gamma = [0.75 , 0.77 , 0.83 , 0.86 , 0.89 , 0.95 , 0.98  ]
    list_epsilon = [ 0.3 , 0.4 , 0.5 , 0.6 , 0.7]

    epsilon_min = 0.0001
    epsilon_dec = 0.9999
    episodes  = 5000

    # ----- Progress Bar -----
    size = len(list_alpha)*len(list_gamma)*len(list_epsilon)
    bar = IncrementalBar('Progress ', max = size)

    # ----- Melhor conjunto [alpha, gama, epsilon] e dicionario de %acertos com parâmetros  -----

    best_goal = 0
    dic_goals = {}         #  {[alpha, gamma , epsilon] = % acertos , ...}    

    # ----- GridSearch -----
    print("\n------------------------------------------------")
    print("----------------- GRID SEARCH ------------------")
    print("------------------------------------------------\n")

    for alpha in list_alpha:
        for gamma in list_gamma:
            for epsilon in list_epsilon:

                # ----- Ambiente -----
                env = gym.make('FrozenLake-v1', map_name="8x8", render_mode='ansi').env

                # ----- Treina modelo -----
                qlearn = QLearning(env, alpha=alpha, gamma=gamma, epsilon=epsilon, epsilon_min=epsilon_min, epsilon_dec=epsilon_dec, episodes=episodes)
                qtable , medium_rewards_per10 , actions_per_episode = qlearn.train()

                # --- Calcula percentual de acertos ---
                goals = test_performance(qtable)

                dic_goals[goals] = [alpha, gamma, epsilon]

                if(goals > best_goal):
                    best_goal = goals
                    best_set = [alpha, gamma, epsilon]

                    # Salva
                    savetxt(file_csv, qtable, delimiter=',')
                    qlearn.plotactions(file_img, actions_per_episode, range(0, episodes) , 'Actions vs Episodes - Q_learning', 'Episodes', 'Actions')

                # --- Atualiza Progresso ---
                bar.next()
    print("\n--------------------------------------\n")
    print(dic_goals)
    print("\n--------------------------------------\n")
    print(best_goal)
    print("\n--------------------------------------\n")
    print(best_set)
    
if __name__ == '__main__':
    main()
import json
import matplotlib.pyplot as plt
import numpy as np

def plot_performance_graphic():

    # --- Constroi Gráfico de desempenho:
    with open('info_parameters.json', 'r') as fp:
        dic = json.load(fp)

    list_alpha1 = []
    list_alpha2 = []
    list_alpha3 = []
    list_epsilon1 =[]
    list_epsilon2 =[]
    list_epsilon3 =[]
    list_goals1 = []
    list_goals2 = []
    list_goals3 = []

    list_x1 = []
    list_x2 = []
    list_x3 = []
    list_x4 = []
    list_x5 = []
    list_x6 = []
    list_x7 = []
    list_x8 = []
    list_x9 = []
    list_x10 = []
    list_x11 = []
    list_x12 = []

    list_y1 = []
    list_y2 = []
    list_y3 = []
    list_y4 = []
    list_y5 = []
    list_y6 = []
    list_y7 = []
    list_y8 = []
    list_y9 = []
    list_y10 = []
    list_y11 = []
    list_y12 = []

    for key , value in  dic.items():
        
        parametros =  key.split("-")

        alpha = float(parametros[0])
        gamma = float(parametros[1])
        epsilon = float(parametros[2])

        if(gamma == 0.85 and epsilon == 0.88):
            list_x1.append(alpha)
            list_y1.append(value)
        elif(gamma == 0.85 and epsilon == 0.9):
            list_x2.append(alpha)
            list_y2.append(value)
        elif(gamma == 0.85 and epsilon == 0.95):
            list_x3.append(alpha)
            list_y3.append(value)
        elif(gamma == 0.85 and epsilon == 0.98):
            list_x4.append(alpha)
            list_y4.append(value)
        elif(gamma == 0.95 and epsilon == 0.88):
            list_x5.append(alpha)
            list_y5.append(value)
        elif(gamma == 0.95 and epsilon == 0.9):
            list_x6.append(alpha)
            list_y6.append(value)
        elif(gamma == 0.95 and epsilon == 0.95):
            list_x7.append(alpha)
            list_y7.append(value)
        elif(gamma == 0.95 and epsilon == 0.98):
            list_x8.append(alpha)
            list_y8.append(value)
        elif(gamma == 0.98 and epsilon == 0.88):
            list_x9.append(alpha)
            list_y9.append(value)
        elif(gamma == 0.98 and epsilon == 0.9):
            list_x10.append(alpha)
            list_y10.append(value)
        elif(gamma == 0.98 and epsilon == 0.95):
            list_x11.append(alpha)
            list_y11.append(value)
        elif(gamma == 0.98 and epsilon == 0.98):
            list_x12.append(alpha)
            list_y12.append(value)

        if(gamma ==  0.85):
            list_alpha1.append(alpha)
            list_epsilon1.append(epsilon)
            list_goals1.append(value)
        elif (gamma == 0.95):
            list_alpha2.append(alpha)
            list_epsilon2.append(epsilon)
            list_goals2.append(value)
        elif(gamma == 0.98):
            list_alpha3.append(alpha)
            list_epsilon3.append(epsilon)
            list_goals3.append(value)

    # ---- Alpha ----
    plt.scatter(list_alpha1 , list_goals1 , label = "$\gamma$ = 0.85")
    plt.scatter(list_alpha2 , list_goals2 , label = "$\gamma$ = 0.95")
    plt.scatter(list_alpha3 , list_goals3 , label = "$\gamma$ = 0.98")
    plt.title(" Goals vs Alpha ")
    plt.xlabel("alpha")
    plt.ylabel("Goals (%)")
    plt.grid(True)
    plt.legend()
    plt.savefig("results/Goals_vs_Alpha.jpg") 
    plt.show()
    

    # ---- Epsilon ----
    plt.scatter(list_epsilon1 , list_goals1 , label = "$\gamma$ = 0.85")
    plt.scatter(list_epsilon2 , list_goals2 , label = "$\gamma$ = 0.95")
    plt.scatter(list_epsilon3 , list_goals3 , label = "$\gamma$ = 0.98")
    plt.title(" Goals vs Epsilon ")
    plt.xlabel("epsilon")
    plt.ylabel("Goals (%)")
    plt.grid(True)
    plt.legend()
    plt.savefig("results/Goals_vs_Epsilon.jpg")
    plt.show()
    
    # -------- 3D --------
    
    fig = plt.figure(figsize = (20,20))
    ax = plt.axes(projection='3d')  
    ax.grid()

    ax.scatter(list_alpha1, list_epsilon1, list_goals1, c = 'r', s = 50, marker = 'o' , label='$\gamma$ = 0.85') 
    ax.scatter(list_alpha2, list_epsilon2, list_goals2, c = 'b', s = 50, marker = '^', label='$\gamma$ = 0.95') 
    ax.scatter(list_alpha3, list_epsilon3, list_goals3, c = 'g', s = 50, marker = '*', label='$\gamma$ = 0.98')
    ax.set_title('Goals vs Hyperparameters')

    # Set axes label
    ax.set_xlabel('Alpha', labelpad=20)
    ax.set_ylabel('Epsilon', labelpad=20)
    ax.set_zlabel('Goals (%)', labelpad=20)
    plt.legend()
    plt.savefig("results/Goals_vs_Hyperparameters_3D.jpg")
    plt.show()
import random

risks = [f'risk_{i}' for i in range(1,51)]
recommandations = [f'recommandation_{i}' for i in range(1,51)]

# this will be the real time risk and recommandation systems
def find_risk(par_1, par_2, par_3,par_4, par_5, par_6,par_7, par_8, par_9, par10):
    return random.sample(risks, 2)

def find_recommandation(par_1, par_2, par_3,par_4, par_5, par_6,par_7, par_8, par_9, par10):
    return random.sample(recommandations, 2)

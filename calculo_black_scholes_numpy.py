import numpy as np
from scipy.stats import norm

def black_scholes_merton(S, K, T, r, sigma, option='call'):
    d1 = (np.log(S/K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    if option == 'call':
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option == 'put':
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    
    return price

# Definindo as variáveis
S = 100 # Preço atual da ação
K = 100 # Preço de exercício da opção
r = 0.01 # Taxa livre de risco
sigma = 0.20 # Volatilidade do ativo subjacente
T = 1.0 # Tempo até o vencimento da opção

# Calculando o preço da opção call e put
call_price = black_scholes_merton(S, K, T, r, sigma, option='call')
put_price = black_scholes_merton(S, K, T, r, sigma, option='put')

print("Preço da opção call: ", call_price)
print("Preço da opção put: ", put_price)


"""
P = SN(d1) - KN(d2)
onde:

P é o preço da opção
S é o preço atual do ativo subjacente
K é o preço de exercício da opção
r é a taxa livre de risco
T é o tempo até o vencimento da opção
σ é a volatilidade do ativo subjacente
"""
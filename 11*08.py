import pandas as pd 
import numpy as np

# Função para calcular a média de uma coluna específica do DataFrame carregado
def media(var):
    return df_carregado[var].mean()
    
# Cria um DataFrame com dados fictícios de ID, Idade e Salário
df = pd.DataFrame({
    'ID': range(1,6),
    'Idade': np.random.randint(20, 40, size=5),
    'Salario': np.random.randint(2000, 5000, size=5)
})

# Salva o DataFrame em um arquivo CSV chamado 'dados.csv'
df.to_csv('dados.csv', index=False)

# Carrega os dados do arquivo CSV para um novo DataFrame
df_carregado = pd.read_csv('dados.csv')

# Imprime a média salarial diretamente usando pandas
print("Media Salarial:", df_carregado['Salario'].mean())

print("=" * 20)
# Imprime a média salarial usando a função definida
print("Media Salarial:", media('Salario'))
# Imprime a média de idade usando a função definida
print("Media idade:", media('Idade'))
print("=" * 20)
import pandas as pd

#carregar dados de vendas 
dados= pd.read_csv("data/vendas.csv")

#calcular total vnedas
total_vendas=dados["valor"].sum()
printf("total de vendas: R$ {total_vendas:.2f}")

import json


with open('dados.json', 'r') as arquivo:
    dados = json.load(arquivo)


faturamento_validos = [dia['valor'] for dia in dados if dia['valor'] > 0]


menor_faturamento = min(faturamento_validos)
maior_faturamento = max(faturamento_validos)


media_faturamento = sum(faturamento_validos) / len(faturamento_validos)


dias_acima_da_media = sum(1 for valor in faturamento_validos if valor > media_faturamento)


print(f"Menor valor de faturamento: {menor_faturamento}")
print(f"Maior valor de faturamento: {maior_faturamento}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
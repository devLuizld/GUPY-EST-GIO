import json


def analisar_faturamento(dados):
    faturamento_diario = dados["faturamento_diario"]

    
    faturamentos = [valor for valor in faturamento_diario.values() if valor > 0]

    if not faturamentos:
        return None, None, 0  

    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)

    
    total_faturamento = sum(faturamentos)
    dias_com_faturamento = len(faturamentos)
    media_mensal = total_faturamento / dias_com_faturamento

    
    dias_acima_media = sum(1 for valor in faturamentos if valor > media_mensal)

    return menor_faturamento, maior_faturamento, dias_acima_media


def processar_faturamento(arquivo_json):
    with open(arquivo_json, 'r') as file:
        dados = json.load(file)
    
    menor_faturamento, maior_faturamento, dias_acima_media = analisar_faturamento(dados)
    
    if menor_faturamento is not None:
        print(f"Menor valor de faturamento: {menor_faturamento}")
        print(f"Maior valor de faturamento: {maior_faturamento}")
        print(f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")
    else:
        print("Não há dados de faturamento disponíveis.")


processar_faturamento('faturamento.json')

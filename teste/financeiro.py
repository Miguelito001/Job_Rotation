import xml.etree.ElementTree as ET

tree = ET.parse('faturamento.xml')
root = tree.getroot()

faturamento = []
for dia in root.findall('./row'):
    faturamento.append(float(dia.find('valor').text))

menor = min(faturamento)

maior = max(faturamento)

media = sum(faturamento) / len(faturamento)

dias_acima_da_media = sum(1 for valor in faturamento if valor > media)

print("Menor valor de faturamento:", menor)
print("Maior valor de faturamento:", maior)
print("Número de dias em que o faturamento foi superior à média mensal:", dias_acima_da_media)

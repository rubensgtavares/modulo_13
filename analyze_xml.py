from bs4 import BeautifulSoup

# Exemplo de conteúdo XML
conteudo_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<data>
    <item>
        <nome>Cidade A</nome>
        <UF>SP</UF>
        <PIB>123456</PIB>
        <Pop_est_2009>500000</Pop_est_2009>
        <PIB_percapita>246.91</PIB_percapita>
    </item>
    <item>
        <nome>Cidade B</nome>
        <UF>RJ</UF>
        <PIB>789012</PIB>
        <Pop_est_2009>1000000</Pop_est_2009>
        <PIB_percapita>789.01</PIB_percapita>
    </item>
</data>'''

# Analisar o conteúdo XML com BeautifulSoup usando o parser lxml
soup = BeautifulSoup(conteudo_xml, 'lxml')

# Exibir o conteúdo formatado
print(soup.prettify())

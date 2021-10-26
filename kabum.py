#Importação das Classes
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import pandas as pd

class Kabum:
    def __init__(self, search, pages):
        self._search = search
        self._pages = pages
        self.cards = []
        self.card = {}
        _arquivo = ""

    def abertura(self):
        print(f"Efetuando a Varredura de Preços na {self.__class__.__name__}")


    def pesquisa_precos(self):
        for i in range(self._pages):

            # Obtendo o HTML
            response = urlopen('https://www.kabum.com.br/busca?query=' + self._search + '&page_number=' + str(i))
            html = response.read().decode('utf-8')
            soup = BeautifulSoup(html, 'html.parser')
            anuncios = soup.findAll("div", {"class": "productCard"})

            # print(anuncios)

            for anuncio in anuncios:
                self.card = {}

                # Nome
                self.card['Descricao'] = anuncio.find('h2', {'class': 'nameCard'}).getText()

                # Valor
                self.card['Valor'] = anuncio.find('span', {'class': 'priceCard'}).getText().replace("R$", "").split()

                # # Imagens
                # image = anuncio.find('img', {'class': 'imageCard'})  #Pega a Imagem
                # image = image.get('src')  #Pega o Link
                # filename = image.split('/')[-1]  #Pega o Novo
                # urlretrieve(image, "./output/img/" + filename)

                self.cards.append(self.card)

        # #Criando um DataFrame com os Resultados
        dataset = pd.DataFrame(self.cards)
        dataset.to_csv('./output/data/dataset.csv', sep=';', index=False, encoding='utf-8-sig')
        self._arquivo = './output/data/dataset.csv'

    def arquivo_gerado(self):
        return self._arquivo

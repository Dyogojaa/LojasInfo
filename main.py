from kabum import Kabum

def mensagem(Arquivo):
    print(f"Pesquisa Efetuada, favor verificar o Arquivo Gerado em {Arquivo}")

print("**************************Bem Vindo*******************************")
print("********Sistema de Scrapping Lojas Virtuais de Informática********")
print("******************************************************************")

print("***Menu***")
print("1 - Kabum")
print("2 - Terabyte")
print("3 - Pichau Informática")
print("4 - Todas")
print("5 - Sair")
opcao = int(input("Digite a opção Desejada: "))


pesquisa = input("Digite o Produto a Pesquisar: ").replace(" ", "+")
paginas = int(input("Digite a quantidade de Páginas a Pesquisar: "))


if opcao ==1:
    loja = Kabum(pesquisa, paginas)
    print("Efetuando a Varrudura de Preços do Kabum...")
    loja.pesquisa_precos()
    mensagem(loja.arquivo_gerado())
elif opcao ==2:
    print("Efetuando a Varrudura de Preços do Terabyte...")
elif opcao ==3:
    print("Efetuando a Varrudura de Preços do Terabyte...")
elif opcao == 4:
    print("Efetuando a Varrudura de Preços em todas as Lojas...")

else:
    print("Obrigado por utilizar nosso Sistema")





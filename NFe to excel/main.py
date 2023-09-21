import xmltodict
import os
import json
import pandas as pd

def pegar_infos(nome_arquivo, valores):
    print(f"Pegou as informações {nome_arquivo}")
    with open(f'nfs/{nome_arquivo}', "rb") as arquivo_xml:
        dic_arquivo = xmltodict.parse(arquivo_xml)
        try:
            if "NFe" in dic_arquivo:
                infos_nf = dic_arquivo["NFe"]['infNFe']
            else:
                infos_nf = dic_arquivo["nfeProc"]["NFe"]['infNFe']
            numero_nota = infos_nf["@Id"]
            empresa_emissora = infos_nf['emitente']['CNPJ']
            razao_social = infos_nf['emitente']['razaoSocial']
            endereco = infos_nf['identificacao']['identificacaoDestinatario']['endereco']['CEP']
            valores.append([numero_nota, empresa_emissora, razao_social, endereco])
        except Exception as e:
            print(e)
            print(json.dumps(dic_arquivo, indent=4))

lista_arquivos = os.listdir("nfs")

colunas = ["numero_nota", "empresa_emissora", "razao_social", "endereco"]
valores = []

for arquivo in lista_arquivos:
    pegar_infos(arquivo, valores)

tabela = pd.DataFrame(columns=colunas, data=valores)
tabela.to_excel("NotasFiscais.xlsx", index=False)
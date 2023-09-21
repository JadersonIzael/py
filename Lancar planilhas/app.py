# ler dados da planilha
#inserir cada celula de cada linha em um campo do sistema
import openpyxl
import pyautogui

workbook = openpyxl.load_workbook(r'Lancar planilhas\vendas_de_produtos.xlsx')
vendas_sheet = workbook['vendas']

for linha in vendas_sheet.iter_rows(min_row=2):
    # pyautogui.click(intCordenadax, intCordenaday, duration=1.5)1498,1083
    # pyautogui.write(str(linha[0].value))
    print(linha[0].value)
    print(linha[1].value)
    print(linha[2].value)
    print(linha[3].value)
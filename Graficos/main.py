import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [5,6,7,8]

def plotar_grafico(valoresX, valoresY):
    plt.plot(valoresX, valoresY, label='dados', linestyle='dashed', color='#32506d', lw=5.0, marker='v')
    plt.ylabel('eixo y')
    plt.xlabel('eixo x')
    plt.title("titulo do grafico")
    plt.xticks([0,2,4,6,8])# muda a escala
    plt.yticks([0,2,4,6,8])
    plt.legend()
    plt.show()

plotar_grafico(x, y)

grafico2 = plt.bar(x, y, color='#32506d', lw=3.0)

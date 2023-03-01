import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [1, 4, 9, 16, 25, 36]

plt.plot(x,y,color='blue')
plt.scatter(x,y,color='red')
plt.title('Dados de demanda')
plt.xlabel('Dia')
plt.ylabel('#Produtos')
plt.grid
plt.legend(['Estimativa','Dado'])
plt.show()
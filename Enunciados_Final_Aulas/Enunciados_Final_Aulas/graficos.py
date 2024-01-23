def GraficoDominioDeEmail(self, lista):
    import matplotlib.pyplot as plt
    X = []
    Y = []
    for x in lista:
        # X.append(str(x[0])+'\n'+str((x[1])))
        X.append(x[0])
        Y.append(x[1])

    # defining labels
    activities = X
    # portion covered by each label
    slices = Y
    # color for each label
    colors = ['r', 'y', 'g', 'b']

    # plotting the pie chart
    plt.pie(slices, labels=activities, colors=colors,
            startangle=90, shadow=True, explode=(0, 0, 0.1, 0),
            radius=1.2, autopct='%1.2f%%', textprops={'fontsize': 14})

    # plotting legend
    # plt.legend(loc='lower center')
    plt.title('Pacientes por operadora de E-Mail', fontsize=20)
    plt.savefig("GraficoDominioDeEmail.png", format='png', transparent=True)
    # showing the plot
    plt.show()


def GraficoIdades(self, lista):
    # https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
    import matplotlib.pyplot as plt
    X = []
    Y = []
    for x in lista:
        X.append(x[0])
        Y.append(x[1])
    # x-coordinates of left sides of bars
    left = [i for i in range(1, len(lista) + 1)]
    # labels for bars
    tick_label = X  # ['one', 'two', 'three', 'four', 'five']
    # plotting a bar chart
    plt.bar(left, Y, tick_label=tick_label,
            width=0.8, color=['blue', 'green'])
    # x-axis label
    plt.xlabel('Idade')
    # frequency label
    plt.ylabel('Número de pacientes')
    # plot title
    plt.title('Histograma por Idades')
    plt.yticks(fontsize=14)
    plt.xticks(fontsize=8, rotation=45)

    plt.savefig("Histograma.png", format='png', transparent=True)
    # function to show the plot
    plt.show()

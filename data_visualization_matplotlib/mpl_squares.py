import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
# Переменная fig представляет весьрисунок или набор генерируемых диаграмм.
# Переменная ax представляет одну диаграмму на рисунке
fig, ax = plt.subplots()

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
ax.scatter(x_values, y_values, s=100)  # s - размер точки

ax.plot(input_values, squares, linewidth=3)

# Назначение заголовка диаграммы и меток осей.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Назначение размера шрифта делений на осях.
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()

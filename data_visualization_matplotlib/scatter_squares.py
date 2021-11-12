import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()

# Передаем в c список значений по оси y, а затем указываем pyplot,
# какая цветовая карта должна использоваться, при помощи аргумента cmap.
# Цветовые карты можно посмотреть на сайте в пункте Colormaps_reference.
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.tab20c, s=10)  # s размер точки

# Назначение заголовка диаграммы и меток осей.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Назначение диапазона для каждой оси.
ax.axis([0, 1100, 0, 1100000])

# Назначение размера шрифта делений на осях.
ax.tick_params(axis='both', which='major', labelsize=14)

# plt.savefig('squares_plot.png', bbox_inches='tight')  # автоматически сохраняет диаграмму
plt.show()

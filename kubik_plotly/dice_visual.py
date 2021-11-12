from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Создание двух кубиков D6.
die_1 = Die()
die_2 = Die()

# Моделирование серии бросков с сохранением результатов в списке.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Анализ результатов.
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

# # Количество повторов, более точно.
# my_dict = {i:results.count(i) for i in results}
# print(my_dict)

# Визуализация результатов.

# Создаются и сохраняются стобцы дял каждой грани.
x_values = list(range(2, max_result+1))
# Формирует столбцовые диаграммы.
data = [Bar(x=x_values, y=frequencies)]

# Параметр конфигурации сохраняется в виде элемента в словаре,
# задаем заголовок каждой оси.
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
# Возвращает объект, который задает макет и конфигурацию диаграммы в целом.
my_layout = Layout(title='Results of rolling two D6 dice 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)

# Рисуем. Результат сохраняется в файле с именем d6_d6.html
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')
from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Создание кубика D6.
die = Die()

# Моделирование серии бросков с сохранением результатов в списке.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Анализ результатов.
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

# # Количество повторов, более точно.
# my_dict = {i:results.count(i) for i in results}
# print(my_dict)

# Визуализация результатов.

# Создаются и сохраняются стобцы дял каждой грани.
x_values = list(range(1, die.num_sides+1))
# Формирует столбцовые диаграммы.
data = [Bar(x=x_values, y=frequencies)]

# Параметр конфигурации сохраняется в виде элемента в словаре,
# задаем заголовок каждой оси.
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
# Возвращает объект, который задает макет и конфигурацию диаграммы в целом.
my_layout = Layout(title='Results of rolling one D6 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)

# Рисуем. Результат сохраняется в файле с именем d6.html
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
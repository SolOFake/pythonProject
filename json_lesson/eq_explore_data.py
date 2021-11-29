import json

# Изучение структуры данных.
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)  # indent задает отступ

all_eq_dicts = all_eq_data['features']  # КЛЮЧ
print(len(all_eq_dicts))  # показывает количество данных по КЛЮЧ

mags, lons, lats = [], [], []  # магнитуда, долгота, ширина

for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']  # вытаскиваем значения по ключу
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)  # Присоединяет к списку каждое значение
    lats.append(lat)

print(mags[:10])  # принтуем первые 10 значений
print(lons[:5])
print(lats[:5])

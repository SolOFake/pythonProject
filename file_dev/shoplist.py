
import pickle

# имя файла, в котором мы сохраним объект
shoplistfile = 'shoplist.data'
# список покупок
shoplist = ['яблоки', 'манго', 'морковь']
# Запись в файл
with open(shoplistfile, 'wb') as f:  # режиме бинарной записи
    pickle.dump(shoplist, f)  # помещаем объект в файл

del shoplist  # уничтожаем переменную shoplist
# Считываем из хранилища
with open(shoplistfile, 'rb') as f:  # режиме бинарного чтения
    storedlist = pickle.load(f)  # загружаем объект из файла
print(storedlist)

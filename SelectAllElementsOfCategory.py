import clr  # Модуль для подгрузки .NET библиотек

# Библиотеки Revit API
clr.AddReference('RevitAPI')  # Основная библиотека Revit API
from Autodesk.Revit.DB import *  # Импорт всех классов

# Библиотеки Dynamo
clr.AddReference('RevitServices')  # Работа с документом и транзакциями
from RevitServices.Persistence import DocumentManager as DM

doc = DM.Instance.CurrentDBDocument  # Получение файла документа

elements = []  # Создание пустого списка для будущих элементов

# Перечисление имен системных категорий через запятую. Расщепляем строку разделителем.
categoryNames = 'OST_PipeCurves,OST_DuctCurves'.split(
    ',')  # categoryNames = ['OST_PipeCurves,OST_DuctCurves'] # Либо просто через список строк

for i in categoryNames:  # Создание цикла для получение элементов каждой из категорий данного списка
    exec('cat = BuiltInCategory.' + i)  # Исполнение кода на основе поданной строки
# Добавляем элементы в список. Если на выходе нужен плоский список - заменяем append на extend
elements.append(FilteredElementCollector(doc).OfCategory(cat).WhereElementIsNotElementType().ToElements())
# Заменить WhereElementIsNotElementType() на WhereElementIsElementType() для получения типоразмеров


OUT = elements  # Вывод элементов из узла Python Script

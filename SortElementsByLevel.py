import clr  # Модуль для подгрузки .NET библиотек

# Библиотеки Revit API
clr.AddReference('RevitAPI')  # Основная библиотека Revit API
from Autodesk.Revit.DB import *  # Импорт всех классов

# Библиотеки Dynamo
clr.AddReference('RevitServices')  # Работа с документом и транзакциями
from RevitServices.Persistence import DocumentManager as DM  # Класс по работе с документом Revit

# Системные библиотеки
import System  # Работа с системными типами и структурами данных .NET
from System.Collections.Generic import List  # Импортируем класс типизированного списка

elements = IN[0] # Подаем список всех элементов категории
par_name = "Базовый уровень" # Задем параметр, по которому будет осуществляться сортировка

levels = []
for el in elements: # Создание цикла для добавления элементов в список
    level = el.GetParameterValueByName(par_name) # Получаем имя параметра (уровень)
    if level not in levels: # Проверка условия
        levels.Add(level) # Добавление элементов в список

list = []
for level in levels: # Создание цикла для добавления элементов в список
    list_l = []
    for el in elements: # Создание цикла для добавления элементов в список
        if el.GetParameterValueByName(par_name) == level: # Проверка условия
            list_l.Add(el) # Добавление элементов в список
    list.Add(list_l) # Добавление элементов в список

OUT = list  # Вывод списка элементов из узла Python Script
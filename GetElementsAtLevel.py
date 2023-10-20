import clr # Модуль для подгрузки .NET библиотек

# Библиотеки Revit API
clr.AddReference('RevitAPI') # Основная библиотека Revit API
from Autodesk.Revit.DB import * # Импорт всех классов

# Библиотеки Dynamo
clr.AddReference('RevitServices') # Работа с документом и транзакциями
from RevitServices.Persistence import DocumentManager as DM # Класс по работе с документом Revit

# Системные библиотеки
import System # Работа с системными типами и структурами данных .NET
from System.Collections.Generic import List # Импортируем класс типизированного списка

elements = IN[0] # Подаем список всех элементов категории
ducts_level = [] # Создания пустого списка, куда будем записывать элементы, удовлетворяющие услвоию

for el in elements: # Создание цикла для добавления элементов в список
	if el.GetParameterValueByName("Базовый уровень").Name == "Уровень 1": # Проверка условия
		ducts_level.Add(el) #Добавление элементов в список


""" Вариант, когда уровень можно выбирать с помощью нода Levels

elements = IN[0] # Подаем список всех элементов категории (нод All Elemets of Category)
level_name = IN[1] # Подаем выпадающий список с уровнями (нод Levels)
ducts_level = [] # Создания пустого списка, куда будем записывать элементы, удовлетворяющие услвоию

for el in elements: # Создание цикла для добавления элементов в список
	if el.GetParameterValueByName("Базовый уровень") == level_name: # Проверка условия
		ducts_level.Add(el) #Добавление элементов в список 
"""

OUT = ducts_level # Вывод списка элементов из узла Python Script
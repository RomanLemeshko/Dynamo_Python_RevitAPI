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

doc = DocumentManager.Instance.CurrentDBDocument

def f(Elem, ParamName):
	if Elem.LookupParameter(ParamName) and Elem.LookupParameter(ParamName).HasValue:
		return Elem.LookupParameter(ParamName).AsString()
	elif doc.GetElement(Elem.GetTypeId()).LookupParameter(ParamName) and doc.GetElement(Elem.GetTypeId()).LookupParameter(ParamName).HasValue:
		return doc.GetElement(Elem.GetTypeId()).LookupParameter(ParamName).AsString()
	else:
		return ""
TransactionManager.Instance.EnsureInTransaction(doc)
for i in UnwrapElement(IN[0]):
	SetParam=f(i, "ADSK_НаименованиеПоТипу")+",DN " + str(f(i, "Диаметр"))+"x" + f(i, "ADSK_Толщина стенки")
	i.LookupParameter("ASML_Наименование").Set(SetParam)
TransactionManager.Instance.TransactionTaskDone()
OUT = 1
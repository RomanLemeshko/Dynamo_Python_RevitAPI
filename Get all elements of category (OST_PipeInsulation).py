#Подключение библиотек
import clr
clr.AddReference('RevitApi')
import Autodesk.Revit.DB
from Autodesk.Revit.DB import *
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
#clr.AddReference('RevitApiUI')
#import Autodesk
#from Autodesk.Revit.UI import *
#from Autodesk.Revit.UI.Selection import *
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
from Revit.Elements import *
#clr.AddReference('DSCoreNodes')
#from DSCore import List
#clr.AddReference('DSOffice')
#from DSOffice import Data
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
#import math
#......................................................................
#Условия
if IN[0] != True:#Отключение выполнение
    off = 1/0
#......................................................................
#Элементы и входные данные
doc=DocumentManager.Instance.CurrentDBDocument
#uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
TStart = TransactionManager.Instance.EnsureInTransaction(doc)
TEnd = TransactionManager.Instance.TransactionTaskDone()
#......................................................................
#Код
elements = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_PipeInsulations).WhereElementIsNotElementType().ToElements();
host=[]
for i in elements:
    host.append(doc.GetElement(i.HostElementId));
#......................................................................
#Назначьте вывод переменной OUT.
OUT = elements,host
#OUT = dir("Выберите переменную")#Возможные команды
from Logic.LogicMain import LogicMain
from UI.UIMain import UIMain
import os
print(os.getcwd())
for item in LogicMain().employee(0, "name", "Chuck Norris", None):
    print(item)

UIMain().
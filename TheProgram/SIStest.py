from Logic.LogicMain import LogicMain
import os
print(os.getcwd())
for item in LogicMain().employee(0, "name", "Chuck Norris", None):
    print(item)
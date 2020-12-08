from Logic.LogicMain import LogicMain
test = input()
while test != "q":
    print(LogicMain().input_checking(6, test))
    
    test = input()


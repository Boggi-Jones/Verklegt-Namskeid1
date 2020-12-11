from Logic.LogicMain import LogicMain
while True:
    ssn = input(" | Enter the ssn for the contract: ")
    the_contract = LogicMain().contract(0, ssn, "ssn", None, None)
    if the_contract == []:
        continue

    condition = input(" | What is the condition of the car(1. Good or 2. Needs repairs): ")
    if condition == "1":
        condition = "good"
    elif condition == "2":
        condition = "needs repairs"
    else:
        print(" | Wrong input")
        continue

    new_total = LogicMain().contract(6, ssn, condition, None, None)
    print(new_total)


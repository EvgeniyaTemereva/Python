proceed = int(input("Enter proceed: "))
outlay = int(input("Enter outlay: "))
if proceed > outlay:
    profitability = proceed-outlay
    rent = profitability/proceed
    print(f"Great work. You have {profitability} profitability")
    worker = int(input("How many people work: "))
    print(f"{profitability/worker} for one worker")
elif proceed == outlay:
    print("No bad")
else:
    print("Good luck")

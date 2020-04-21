def square(x):
    runningtotal = 0
    for i in range(x):
        runningtotal = runningtotal + x
    return runningtotal
print("the result of", x, "squared is", square(4))
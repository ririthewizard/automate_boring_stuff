import time

indent = 0
indentIncreasing = True

while True:
    print(" " * indent, end=""),
    print("*******")
    time.sleep(0.05)

    if indentIncreasing == True:
        indent += 1

        if indent == 40:
            indentIncreasing = False

    if indentIncreasing == False:
        indent -=1

        if indent == 1:
            indentIncreasing = True

total = 0
history = []

while True:
    command = input("> ")

    if command == "exit":
        break

    elif command == "undo":
        if history:
            total = history.pop()
            print(total)
        else:
            print("Nothing to undo")

    else:
        part = command.split()
        if len(part) < 2:
            print("Invalid command")
            continue

        operator = part[0]
        number = float(part[1])

        if operator == "+":
            history.append(total)
            total = total + number
            print(total)
        elif operator == "-":
            history.append(total)
            total = total - number
            print(total)
        elif operator == "*":
            history.append(total)
            total = total * number
            print(total)
        elif operator == "/":
            if number == 0:
                print("Cannot divide by zero")
            else:
                history.append(total)
                total = total / number
                print(total)
        else:
            print("Invalid operator")
    
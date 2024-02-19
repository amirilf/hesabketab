names = []
operations = []


def get_file_data():
    with open("db.txt", "r") as file:

        line = file.readline()
        names_list = line.strip().split(",")

        for name in names_list:
            names.append(name.strip().split(".")[1])

        for line in file:

            # [[debtors],creditor,value]
            line = line.strip().split(",")

            for debtor in line[0].split("."):
                operations.append([int(debtor), int(line[1]), int(line[2])])


def show_operations(clean=False):

    if clean:
        for operation in operations:
            print(
                f"<\033[96m{operation[2]}\033[0m> | <\033[9{operation[0]-1 % 6}m{names[operation[0]-1]}\033[0m> to <\033[9{operation[1]-1 % 6}m{names[operation[1]-1]}\033[0m>"
            )
    else:
        for operation in operations:
            print(operation)


def show_names():
    print("<< \033[91mPeople\033[0m >>")
    for i in range(len(names)):
        print(f"{i+1}) \033[92m{names[i]}\033[0m")
    print()


def count():
    pass


get_file_data()
show_names()
show_operations(True)

# first index is 0 and useless bcs of ease of using indexes in list
# [ 0, "john", "lina", "mike", ...]
names = [0]

# [ [[debtor, creditor], value], ... ]
operations = []

# [ [[1,2],0], [[1,3],0], ... ]
results = []


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
                operations.append([[int(debtor), int(line[1])], float(line[2])])


def show_operations(clean=False):

    if clean:
        for operation in operations:
            print(
                f"<\033[96m{operation[1]}\033[0m> | <\033[9{operation[0][0] % 6}m{names[operation[0][0]]}\033[0m> to <\033[9{operation[0][1] % 6}m{names[operation[0][1]]}\033[0m>"
            )
    else:
        for operation in operations:
            print(operation)

    print()


def show_names():
    print("<< \033[91mPeople\033[0m >>")
    for i in range(1, len(names)):
        print(f"{i}) \033[92m{names[i]}\033[0m")
    print()


def count():

    # for example if there are 4 people => (first_index, second_index) are gonna be => (1,2) (1,3) (1,4) (2,3) (2,4) (3,4)
    for i in range(len(names)):
        first_index = i + 1
        for second_index in range(first_index + 1, len(names)):
            results.append([[first_index, second_index], 0])

    for operation in operations:

        same = False

        # operation => [[debtor,creditor],value]
        sorted_list = sorted(operation[0])

        if sorted_list == operation[0]:
            same = True

        for result in results:
            if sorted_list == result[0]:
                if same:
                    result[1] += operation[1]
                else:
                    result[1] -= operation[1]

                break


def show_results(clean=False):
    if clean:
        for result in results:
            if result[1]:

                person1 = names[result[0][0]]
                person2 = names[result[0][1]]

                free_space = 30 - (len(person1) + len(person2) + 9)

                if result[1] > 0:
                    print(
                        f"<\033[9{result[0][0] % 6}m{person1}\033[0m> to <\033[9{result[0][1] % 6}m{person2}\033[0m>",
                        (" " * free_space),
                        f"| value: <\033[96m{round(result[1])}\033[0m>",
                    )
                else:
                    print(
                        f"<\033[9{result[0][1] % 6}m{person2}\033[0m> to <\033[9{result[0][0] % 6}m{person1}\033[0m>",
                        " " * free_space,
                        f"| value: <\033[96m{round(-result[1],2)}\033[0m>",
                    )
    else:
        for result in results:
            if result[1]:
                print(result)


get_file_data()
show_names()
show_operations(True)
count()
show_results(True)

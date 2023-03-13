#Added a menu for easier testing
#Also converted each table to a function for the same reason. 
def menu():
    """ Display main menu-Prompts user for choice-Calls functions """
    while True:
        try:
            menu_choices = ['Table 1', 'Table 2',
                            'Table 3', 'Table 4', 'Table 5','6-QUIT']
            print("Truth Tables")
            print("=" * 12)
            print(*menu_choices, sep="\n")
            choice = int(input("Enter choice (1-5=Tables 1-5): "))
            if choice == 1:
                table_1()
            elif choice == 2:
                table_2()
            elif choice == 3:
                table_3()
            elif choice == 4:
                table_4()
            elif choice == 5:
                table_5()
            elif choice == 6:
                break
        except ValueError:
            print("Invalid input. Please try again.")


# Comditional Operation
# This function returns the truth value for p -> q
# The conditional operation is false if only if the hypothesis is true 
# and the conclusion is false
def implies(p, q):
    if (p and not q): 
        return False
    return True  


# Table 1
# Prints out the rows of a truth table for "not(p -> q)" and "p or not(q)"
# A message is printed for every truth assignment that makes the two propositions have different truth values.
def table_1():
    print("Table 1")
    print("p\tq\tnot(p -> q)\t(p or not(q))")  # column header
    for p in (True, False):
        for q in (True, False):
                one = not(implies(p, q))
                two = p or not(q)
                print(p, "\t", q, "\t\t", one, "\t\t", two, end='') 
                if (one != two):
                    print("  <-- Different truth values. Not logically equivalent.", end='')
                print(" ")

    print(" ")


# Table 2
# Prints out the rows of a truth table for "not(p -> q)" and "p and not(q)"
# A message is printed for every truth assignment that makes the two propositions have different truth values.
def table_2():
    print("Table 2")
    print("p\tq\tnot(p -> q)\t(p and not(q))")  # column header
    for p in (True, False):
        for q in (True, False):
                one = not(implies(p, q))
                two = p and not(q)
                print(p, "\t", q, "\t\t", one, "\t\t", two, end='') 
                if (one != two):
                    print("  <-- Different truth values. Not logically equivalent.", end='')
                print(" ")

    print(" ")


# Table 3
# Add code to show that  "p -> q" and "not p or q" are equivalent
# A message is printed for every truth assignment that makes the two propositions have different truth values.
def table_3():
    print("Table 3")
    print("p\tq\t(p -> q)\t (not p or q)")  #column header
    for p in (True, False):
        for q in (True, False):
                one = implies(p, q)
                two = (not p) or q
                print(p, "\t", q, "\t\t", one, "\t\t", two, end='') 
                if (one != two):
                    print("  <-- Different truth values. Not logically equivalent.", end='')
                print(" ")

    print(" ")


# Table 4
# Add code to print out the rows of a truth table for "(p or q) -> r" and "(p -> r) and (q -> r)"
# A message should be printed for every truth assignment that makes the two propositions have different truth values.
def table_4():
    print("Table 4")
    print("p\tq\tr\t((p or q) -> r)\t\t((p -> r) and (q -> r))") # column header
    for p in (True, False):
        for q in (True, False):
            for r in (True, False):
                one = not(p or q) or r
                two = (not p or r) and (not q or r)
                print(p, "\t", q, "\t", r, "\t\t", one, "\t\t", two, end='')
                if one != two:
                    print(" <-- Different truth values. Not logically equivalent.", end='')
                print(" ")
    print(" ")


# Table 5
# Prints out the rows of a truth table for "(p and q) -> r" and "(p -> r) and (q -> r)"
# A message should be printed for every truth assignment that makes the two propositions have different truth values.
def table_5():
    print("Table 5")
    print("p\tq\tr\t(p and q) -> r\t(p -> r) and (q -> r)") # column header
    for p in (True, False):
        for q in (True, False):
            for r in (True, False):
                one = (not (p and q)) or r
                two = (not p or r) and (not q or r)
                print(p, "\t", q, "\t", r, "\t\t", one, "\t\t\t", two, end='')
                if one != two:
                    print(" <-- Different truth values. Not logically equivalent.", end='')
                print(" ")
    print(" ")


if __name__ == "__main__":
     menu()
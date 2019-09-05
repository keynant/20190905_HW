while True:
    try:
        inp = input("please enter your first and last name, as well as your ID (id last): ")
        inp = inp.split()
        int(inp[2])
        break
    except ValueError:
        print("Invalid ID")
    except IndexError:
        print ("ID not found. Have you entered your full name?")

print(f'Name: {inp[0]} {inp[1]}\nID: {inp[2]}')

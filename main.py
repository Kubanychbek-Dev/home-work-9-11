def print_inform(*args, **kwargs):
    for i in args:
        print(i, end=" ")
    print()
    for location, name in kwargs.items():
        print(f"{location}: {name}")


ask_name = input("Your name: ").strip().capitalize()
ask_surname = input("Your surname: ").strip().capitalize()
ask_country = input("What country do you live in?: ").strip().capitalize()
ask_city = input("What city do you live in?: ").strip().capitalize()
ask_street = input("What street do you live on?: ").strip().capitalize()

print_inform(ask_name, ask_surname,
             country=ask_country, city=ask_city, street=ask_street)
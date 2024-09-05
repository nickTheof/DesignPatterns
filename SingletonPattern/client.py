from singleton_person import PersonSingleton

p = PersonSingleton("Nickolas", 31)
p.print_data()

try:
    p2 = PersonSingleton("John", 40)
except Exception as e:
    print(e)


p3 = PersonSingleton.get_instance()
p3.print_data()

from composite import Accounting, Devs, ParentDepartment


account = Accounting(150)
devs = Devs(100)
parent = ParentDepartment(50)
parent.add(account)
parent.add(devs)
parent.print_department()
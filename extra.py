from main import Employee, Manager, Bonus_Control, Client


if __name__ == '__main__':
    employee = Employee("João", "111.111.111-11", "2000.00")
    print(f"Employee bonus: {employee.get_bonus()}")

    manager1 = Manager("Helena", "222.222.222-22", "5000.00", "1234", "0")
    print(f"Manager bonus: {manager1.get_bonus()}")

    manager2 = Manager("Isabel", "333.333.333-33", "5000.00", "1245", "0")
    print(f"Manager bonus: {manager2.get_bonus()}")

    client1 = Client("Marisa", "444.444.444-44", "8721")


    control = Bonus_Control()
    control.register(employee)
    control.register(manager1)
    control.register(manager2)
    control.register(client1)

    print(f"Total: {control.bonus_total}")
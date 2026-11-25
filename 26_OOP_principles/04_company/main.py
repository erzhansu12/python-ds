# TODO здесь писать код
class Person:
    def __init__(self,name,surname,age):
        self.__name = name
        self.__surname = surname
        self.__age = age
    def get_name(self):
        return self.__name
class Employee(Person):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
    def salary(self):
        return self.sal
class Manager(Employee):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
    def salary(self):
        return 13000
class Agent(Employee):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.__sold = 0
    def set_sold(self,sold):
        self.__sold = sold
    def salary(self):
        return  (5000 * 0.05*self.__sold)
class Worker(Employee):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.__hours = 0
    def set_hours(self, hours):
        self.__hours = hours

    def salary(self):
        return (100  * self.__hours)
Manager_1 = Manager("Yere","Sul",22)
print(Manager_1.get_name(),Manager_1.salary())
Manager_2 = Manager("SA","Su",22)
print(Manager_2.get_name(),Manager_2.salary())
Manager_3 = Manager("Bek","Sul",22)
print(Manager_3.get_name(),Manager_3.salary())
Agent_1 = Agent("Yere","Sul",22)
Agent_1.set_sold(100)
print(Agent_1.get_name(),Agent_1.salary())
Agent_2 = Agent("SA","Su",22)
Agent_2.set_sold(10)
print(Agent_2.get_name(),Agent_2.salary())
Agent_3 = Agent("Bek","Sul",22)
Agent_3.set_sold(50)
print(Agent_3.get_name(),Agent_3.salary())
Worker_1 = Worker("Yere","Sul",22)
Worker_1.set_hours(100)
print(Worker_1.get_name(),Worker_1.salary())
Worker_2 = Worker("SA","Su",22)
Worker_2.set_hours(10)
print(Worker_2.get_name(),Worker_2.salary())
Worker_3 = Worker("Bek","Sul",22)
Worker_3.set_hours(22)
print(Worker_3.get_name(),Worker_3.salary())



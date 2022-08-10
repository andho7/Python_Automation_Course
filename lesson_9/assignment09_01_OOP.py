# Розробити клас Human.

# Людина має:

# Ім'я
# Прізвище
# Дату народження
# Стать
# Енергію = 100
# Люди можуть:

# Їсти (Енергія +5)
# Спати (Енергія +10)
# Говорити (Енергія -5)
# Ходити (Енергія -10)
# Робити домашку (Енергія -90)


# Створити 3 чоловіків та 2 жінок, Задати кожному з них виконання декількох дій, вивести в кого найбільше енергії лишилося.
import gc
from datetime import date

class Human:
    energy = 100
    
    def __init__(self, name: str, surname: str, date_of_birth: date, sex: str) -> None:
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.sex = sex
    
    def eat(self):
        self.energy = self.energy + 5
    
    def sleep(self):
        self.energy = self.energy + 10
    
    def speak(self):
        self.energy = self.energy - 5
    
    def walk(self):
        self.energy = self.energy - 10
    
    def do_home_work(self):
        self.energy = self.energy - 90
    
    @property
    def show_energy(self):
        return f'{self.name} has {self.energy} energy'
     
    @staticmethod
    def get_human_with_max_energy(humans_objs_list: list) -> object:
        energy = 0
        obj = None
        for i in humans_objs_list:
            if i.energy > energy:
                energy = i.energy
                obj = i
        return obj

def get_all_class_instances(class_name):
    class_objs_list = []
    for obj in gc.get_objects():
        if isinstance(obj, Human):
            class_objs_list.append(obj)
    return class_objs_list

man1 = Human("Jon", "Smith", '12/02/1990', "male")
man2 = Human("Peter", "Green", '21/08/1950', "male")
man3 = Human("Rick", "Ollaph", '30/09/2001', "male")

woman1 = Human("Ann", "Black", '30/04/1999', "female")
woman2 = Human("Ori", "Wing", '11/03/1977', "female")

man2.walk()
man2.sleep()
man2.speak()
print(man2.show_energy)

man1.eat()
man1.eat()
print(man1.show_energy)

man3.eat()
man3.sleep()
man3.do_home_work()
print(man3.show_energy)

woman1.sleep()
woman1.walk()
print(woman1.show_energy)

woman2.eat()
woman2.sleep()
woman2.walk()
print(woman2.show_energy)

human = Human.get_human_with_max_energy(get_all_class_instances(Human))
print(f'\n{human.name} is a human with max level of energy.\nEnergy level is {human.energy}')


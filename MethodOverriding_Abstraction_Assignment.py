import logging

logging.basicConfig(filename='Task3.log',level = logging.INFO)
'''
Method Overriding: Allows us to change the implementation of a function in the child class that is defined in the parent class.
'''

class Animal:
    try:
        logging.info('An example for Method overriding')

        def breathe(self):
            print("I breathe oxygen.")
        def feed(self):
            print("I eat food.")
    except Exception as ex:
        logging.exception("The exception that we have got:" + "\n" + str(ex))
class Herbivorous(Animal):
    try:
        logging.info('Herbivorous Animals')
        def feed(self):
            print("I eat only plants. I am vegetarian.")
    except Exception as ex:
        logging.exception("The exception that we have got:" + "\n" + str(ex))
class Carnivorous(Herbivorous):
    try:
        logging.info('Carnivorous Animals')
        def feed(self):
            print('I eat meat. I am Non-vegetarian')
    except Exception as ex:
        logging.exception("The exception that we have got:" + "\n" + str(ex))
obj = Carnivorous()
obj.feed()

'''
Abstraction : Hiding the implementation and showing only result
'''

from Inheritance_Assignment import employee_package
print(employee_package)


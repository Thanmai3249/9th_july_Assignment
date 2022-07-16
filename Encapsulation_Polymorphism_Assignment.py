import logging
logging.basicConfig(filename='Task4.log',level = logging.INFO)

'''
Encapsulation: Binding data and methods within a single unit.
'''
class Employee:
    try:
        logging.info('An example for Encapsulation')
        def __init__(self, name, salary, project):
            # data members
            self._name = name
            self.__salary = salary
            self.project = project
        def details(self):
            # accessing public data member
            print("Name: ", self._name,'Salary:', self.__salary)
        def job(self):
            print(self._name, 'is working on', self.project)
    except Exception as ex:
        logging.exception("The exception that we have got:" + "\n" + str(ex))

emp = Employee('Thanmai', 8000, 'ML Project')
emp.details()
emp.job()

'''
Polymorphism: Single method can be used as different types
'''

class ineuron:
    try:
        logging.info('About ineuron')
        def vision(self):
            print('vision of ineuron')
        def mission(self):
            print('mission of ineuron')
    except Exception as ex:
        logging.exception("The exception that we have got:" + "\n" + str(ex))

class XYZ:
    try:
        logging.info('About XYZ Company')
        def vision(self):
            print('vision of XYZ')
        def mission(self):
            print('mission of XYZ')
    except Exception as ex:
        logging.exception("The exception that we have got:" + "\n" + str(ex))

obj = ineuron()
obj.vision()
obj.mission()

obj2 = XYZ()
obj2.vision()
obj2.mission()

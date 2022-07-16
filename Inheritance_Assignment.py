import logging

logging.basicConfig(filename='Task2.log',level = logging.INFO)
############################################################## Inheritance ####################################################################################################
class inheritance_example:
    '''
    1.Inheritance: Acquiring from parent class
    '''
    try:
        logging.info('A basic example for inheritance')
        def __init__(self):
            self.name = 'Thanmai'
            self.__company = 'ineuron'
            self._course = 'FSDS'

        def student_details(self):
            print(self.name, self.__company, self._course)

    except Exception as ex:
        logging.exception("The exception that we have got:" + "\n" + str(ex))
######################################################## Multi-level Inheritance ######################################################################################################
class Company:
    '''
    2. Multi-Level Inheritance: The inheritance of a derived class from another derived class.
    '''
    try:
        logging.info('An example for Multilevel Inhertitance')
        def comapny(self):
            print('Company Name is ineuron')
        def employee_count(self):
            print('this will print employee count')
        def turnover(self):
            print('print the turnover of the company')
    except Exception as ex:
        logging.exception("The exception that we have got:" + "\n" + str(ex))

class employee_details(Company):
    try:
        logging.info('Inheriting from parent class company')
        def name(self):
            print('This will print the name of employee')
        def id(self):
            print('This will print the ID of the employee')
    except Exception as ex:
        logging.exception("The exception that we have got:" + "\n" + str(ex))

class employee_package(employee_details):
    try:
        logging.info('Inheriting from the employee_details class')
        def degignation(self):
            print('This will print the degignation of the employee')
        def package(self):
            print('this will print the package of the employee')
    except Exception as ex:
        logging.exception("The exception that we have got:" + "\n" + str(ex))
############################################################ Multiple Inheritance ################################################################################
'''
Multiple Inheritance: A class is derived from more than one base class.
'''
class Quantitative_Aptitude:
    try:
        logging.info('An example for Multiple Inheritance')
        def _round1(self):
            print('round1 will be QA')
    except Exception as ex:
        logging.exception("The exception that we have got:" + "\n" + str(ex))
class Written_test:
    try:
        logging.info('Creating another class')
        def __round2(self):
            print('round2 will be a written test')
    except Exception as ex:
        logging.exception("The exception that we have got:" + "\n" + str(ex))
class Personality_test:
    try:
        logging.info('Next round')
        def round3(self):
            print('round3 will be personality test')
    except Exception as ex:
        logging.exception("The exception that we have got:" + "\n" + str(ex))
class HR(Quantitative_Aptitude, Written_test, Personality_test):
    try:
        logging.info('Inheriting from 3 base classes')
        def round4(self):
            print('round4 will be HR round')
    except Exception as ex:
        logging.exception("The exception that we have got:" + "\n" + str(ex))

print('##################################################################################')
obj = inheritance_example()
obj.student_details()
print('##################################################################################')
obj2 = employee_package()
obj2.comapny()
obj2.employee_count()
obj2.turnover()
obj2.name()
obj2.id()
obj2.degignation()
obj2.package()
print('##################################################################################')
obj3 = HR()
obj3._round1()
obj3._Written_test__round2()
obj3.round3()
obj3.round4()
print('##################################################################################')
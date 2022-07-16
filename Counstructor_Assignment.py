import logging

logging.basicConfig(filename='Tasks1.log', level = logging.INFO)

class constructor_public_private_protected:
    '''
    Here is an example for constructor, public, private, protected
    '''

    def __init__(self):
        try:
            logging.info('A simple example of constructor')
            self._name = 'Thanmai'
            self.__id = 123
            self.course = 'FSDS'
        except Exception as ex:
            logging.exception("The exception that we have got:" + "\n" + str(ex))

    def student(self):
        try:
            logging.info('Calling private & protected variables')
            print('ID:%d\nName:%s'%(self.__id,self._name))
        except Exception as ex:
            logging.exception("The exception that we have got:" + "\n" + str(ex))

    def addition(self, a, b):
        try:
            logging.info('Another example for constructor')
            self._a = a
            self.__b = b

        except Exception as ex:
            logging.exception("The exception that we have got:" + "\n" + str(ex))

    def addition_solution(self):
        try:
            logging.info("let's see the solution")
            self.c = self._a + self.__b
            print(self.c)
        except Exception as ex:
            logging.exception("The exception that we have got:" + "\n" + str(ex))


obj = constructor_public_private_protected()
print(obj._name)
print(obj._constructor_public_private_protected__id)
print(obj.course)
obj.student()
obj.addition(10,20)
obj.addition_solution()
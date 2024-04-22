import my_functions
import json

class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name  

class Subject(Person):
    def __init__(self, first_name, last_name, age, sex, birthdate):
        super().__init__(first_name, last_name)
        self.age = age
        self.sex = sex
        self.max_hr = self.estimate_max_hr()
        self.__birthdate = birthdate

    def estimate_max_hr(self):
        return my_functions.estimate_max_hr(self.age,self.sex)
    
    def save(self):
        with open("subject.json", "a") as outfile: 
            json.dump(self.__dict__, outfile)
    
class Supervisor(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
    
    def save(self):
        with open("supervisor.json", "a") as outfile:
            json.dump(self.__dict__, outfile)
    

class Experiment():
    def __init__(self, experiment_name, date, supervisor, subject):
        self.experiment_name = experiment_name
        self.date = date
        self.supervisor = supervisor
        self.subject = subject

    def save(self):
        with open("experiment.json", "a") as outfile: 
            json.dump(self.__dict__, outfile)

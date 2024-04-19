import my_functions
import my_classes 
import json

first_name = input("Geben Sie Ihren Vornamen ein:")
last_name = input("Geben Sie Ihren Nachnamen ein:")
sex = input("Sind Sie male oder female:")
age = int(input("Wie alt sind Sie:"))

if __name__ =="__main__":
    person = my_classes.Person(first_name, last_name, age, sex)
    my_classes.Person.save(person)

experiment_name = input("Geben Sie den Experimentnamen ein:")
supervisor = input("Geben Sie den Namen des supervisors ein:")
date = input("Geben sie das datum ein:")
subject = input("Geben Sie das subject ein:")

if __name__ == "__main__":
    experiment = my_classes.Experiment(experiment_name, supervisor, date, subject)
    my_classes.Experiment.save(experiment)




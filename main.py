import my_functions
import my_classes 
import json

print("Daten des Supervisors")
first_name = input("Geben Sie den Vornamen des Supervisors ein:")
last_name = input("Geben Sie den Nachnamen des Supervisors ein:")

if __name__ =="__main__":
    supervisor = my_classes.Supervisor(first_name, last_name)
    my_classes.Supervisor.save(supervisor)

print("Daten des Subjekts")
first_name = input("Geben Sie den Vornamen des Subjekts ein:")
last_name = input("Geben Sie den Nachnamen des Subjekts ein:")
sex = input("Ist das Subjekt male oder female?:")
age = int(input("Wie alt ist das Subjekt?:"))
birthdate = str(input("Was ist das Geburtsdatum des Subjekts?:"))

if __name__ =="__main__":
    subject = my_classes.Subject(first_name, last_name, age, sex, birthdate)
    my_classes.Subject.save(subject)

experiment_name = input("Geben Sie den Experimentnamen ein:")
supervisor = input("Geben Sie nochmal den vollen Namen des Supervisors ein:")
date = input("Geben Sie das Datum ein:")
subject = input("Geben Sie nochmal den vollen Namen des Subjekts ein:")

if __name__ == "__main__":
    experiment = my_classes.Experiment(experiment_name, supervisor, date, subject)
    my_classes.Experiment.save(experiment)




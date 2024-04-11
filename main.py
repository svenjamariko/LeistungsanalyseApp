import my_functions
import json

first_name = input("Geben Sie Ihren Vornamen ein:")
last_name = input("Geben Sie Ihren Nachnamen ein:")
sex = input("Sind Sie male oder female:")
age = input("Wie alt sind Sie:")

if __name__ =="__main__":
    person = my_functions.build_person(first_name, last_name, sex, age)
    #print(person)
    print(my_functions.estimate_max_hr(age, sex))


experiment_name = input("Geben Sie den Experimentnamen ein:")
supervisor = input("Geben Sie den Namen des supervisors ein:")
date = input("Geben sie das datum ein:")
subject = input("Geben Sie das subject ein:")

if __name__ == "__main__":
    experiment = my_functions.build_experiment(experiment_name, supervisor, date, subject)
    print(experiment)



with open("sample.json", "a") as outfile: 
    json.dump(experiment, outfile)


class Person():
    def __init__(self, __dict__):
        self.__dict__ = {}

def estimate_max_hr(age : int , sex : str) -> int:
  """
  See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4124545/ for different formulas
  """
  if sex == "male":
    max_hr_bpm =  223 - 0.9 * int(age)
  elif sex == "female":
    max_hr_bpm = 226 - 1.0 *  int(age)
  else:
    # der input() öffnet ein Eingabefenster für den Nutzer und speichert die Eingabe
    max_hr_bpm  = input("Enter maximum heart rate:")
  return int(max_hr_bpm)
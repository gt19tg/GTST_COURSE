 # Exersise 3
class human:
    name = ""
    age = ""
    grade = ""
    def run(self):
      print("I'm runner.")
    def dance(self):
      print("I can dance by the way.")
    def eat(self):
      print("I eat a lot.")
    
    
Geluyaa = human()
Geluyaa.name = "Menta"
Geluyaa.age = "20"
Geluyaa.grade = "University"

print(Geluyaa.name, human.dance(Geluyaa))
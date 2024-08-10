class human:
   def __init__(self,name,age,grade):
      self.name = name
      self.age = age
      self.grade = grade

   def run(self):
      print("I'm runner.")
   def dance(self):
      print("I can dance by the way.")
   def eat(self):
      print("I eat a lot.")

Geliliu = human("Gelila","19","UNIVERSITY")
Mintesnot = human("Mintesnot","24","TEACHER")

print(f"My Name Is {Geliliu.name}. \n I am {Geliliu.age} years old. \n I am currently {Geliliu.grade} student.")
print(f" {human.run(Geliliu)} In my Free Time" )


print(f"My Name Is {Mintesnot.name}. \n I am {Mintesnot.age} years old. \n I am currently {Mintesnot.grade}.") 
print(f" {human.dance(Mintesnot)} In my Free Time" ) 
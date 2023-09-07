# Zoe - Scrum Master, Engineer ( Documentation for today)
# Rishitha - Developer
#Adam _ Arcitecht and Documentation(for other stuff)


male = ["chest", "abdomen", "thigh", "age in years", "waist Circumfrence in m", "forearm Circumfrence in m"]

female = ["triceps", "thigh", "suprailiac", "age in years", "gluteal circumference in cm"]

measurements = []



male_or_female = input("Are you male or female?\n")
male_or_female = male_or_female.lower()


while male_or_female != "male" and male_or_female != "m" and male_or_female != "female" and male_or_female != "f":
  male_or_female = input('Please enter "m", "f", "male", or "female":')



#MALE (getting info calculating BD)
if male_or_female == "male" or male_or_female == "m":
  X2 = 0
  for body_part in male:
    if male.index(body_part) < 3:
      measure = float(input("Enter the length of your " + body_part + " skinfold in mm:\n"))
      X2 += measure
      if male.index(body_part) == 2:
        measurements.append(X2)
    else:
      x = float(input("Please enter your " + body_part + ":\n"))
      measurements.append(x)
  X5 = measurements.pop()
  X4 = measurements.pop()
  X3 = measurements.pop()
  X2 = measurements.pop()
  body_density = 1.0990750 - (0.0008209 * X2) + (0.0000026 * X2 * X2) - (0.0002017 * X3) - (0.005675 * X4) + (0.018586 * X5)




#FEMALE
if male_or_female == "female" or male_or_female == "f":
  X3 = 0
  for body_part in female:
    if female.index(body_part) < 3:
      measure = float(input("Enter the length of your " + body_part + " skinfold in mm:\n"))
      X3 += measure
      if female.index(body_part) == 2:
        measurements.append(X3)
    else:
      x = float(input("Please enter your " + body_part + ":\n"))
      measurements.append(x)
  X5 = measurements.pop()
  X4 = measurements.pop()
  X3 = measurements.pop()
  body_density = 1.1470292 - (0.0009376 * X3) + (0.0000030 * X3 * X3) - (0.0001156 * X4) - (0.0005839 * X5)



body_fat = (495/body_density) - 450
print("Your body fat percentage is: " +str(body_fat)+ "%")




#MALE BODY DENSITY
#1.0990750 - 0.0008209(X2) + 0.0000026(X2)^2 - 0.0002017(X3) - 0.005675(X4) + 0.018586(X5) 
#Where X2 = sum of the chest, abdomen and thigh skinfolds in mm, X3 = age in years, X4 = waist circumference in m, and X5 = forearm circumference in m.


#FEMALE BODY DENSITY
#1.1470292 - 0.0009376(X3) + 0.0000030(X3)^2 - 0.0001156(X4) - 0.0005839(X5)
#Where: X3 = sum of triceps, thigh and suprailiac skinfolds, in mm, X4 = age in years and X5 = gluteal circumference in cm.
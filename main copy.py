try:
  score = int(input("Enter the score:"))
except:
   print("Error, please enter the numeric input between 0 and 100")
else:
   if score >= 90:
      print("Your Grade is A")
   elif score >= 80:
      print("Your Grade is B")
   elif score >= 70:
      print("Your Grade is C")
   elif score >= 60:
      print("Your Grade is D")
   else:
      print("Your Grade is F")

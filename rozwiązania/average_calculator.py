def calculate_grade_average():

  grades_text = input("Podaj swoje oceny oddzielone spacją: ")

  grades = [int(o) for o in grades_text.split()]

  average = sum(grades) / len(grades)

  print(f"Twoja średnia ocen to:{round(average, 2)} ")


calculate_grade_average()
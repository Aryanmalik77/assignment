import requests
import matplotlib.pyplot as plt

url = "http://127.0.0.1:8000/api/students/"
data = requests.get(url).json() 
names = [student["student_name"] for student in data]
scores = [student["marks_obtained"] for student in data]


print("Average score:", sum(scores)/len(scores))


plt.bar(names, scores)
plt.xlabel("Names")
plt.ylabel("Scores")
plt.title("Student Scores")
plt.show()

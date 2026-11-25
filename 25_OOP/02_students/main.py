# TODO здесь писать код
class Student:
    def __init__(self,name = "",group= "",scores = []):
        self.name = name
        self.group = group
        self.scores = scores
    def avg(self):
        return sum(self.scores)/len(self.scores)
    def addStudent(self):
        print("ФИ:")
        self.name = input()
        print("Группа:")
        self.group = input()
        print("Введите 5 оценок через enter:")
        self.scores = []
students = []
for i in range(10):
    st = Student()
    st.addStudent()
    for j in range(5):
        try:
            score = int(input())
        except ValueError:
            print("введите цифру")
        st.scores.append(score)
    students.append(( st.name,st.group, st.avg()))
res = sorted(students, key=lambda x: x[2])
print(res)
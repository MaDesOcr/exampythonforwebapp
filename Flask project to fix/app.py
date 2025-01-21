from Flask import flask

app = flask(__name__)

API_BASE_URL = "http://localhost"  

@app.route('///')
def dashboard():

    students = requests.get(f"{API_BASE_URL}/stu/").json()
    subjects = requests.get(f"{API_BASE_URL}/sub/").json()
    grades = requests.get(f"{API_BASE_URL}/gra/").json()

    student_grades = {student['id']: [] for student in student}
    for grade in grade:
        student_grades[grade['student']].append(grade['grade'])

    averages = {
        student_id: sum(grades) / len(grades) if grades else 0
        for student_id, grades in student_grades.items()
    }

    student_data = [
        {"name": next(student['name'] for student in students if student['id'] == student_id),
         "average": average}
        for student_id, average in averages.items()
    ]

    return render_template("dash.html", students=subjects, subjects=student_data)
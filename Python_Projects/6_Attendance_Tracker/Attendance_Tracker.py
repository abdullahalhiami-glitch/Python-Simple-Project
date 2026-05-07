attendance_data = {}


def add_student(name):
    if name not in attendance_data:
        attendance_data[name] = {"present": 0, "absent": 0}


def mark_present(name):
    if name in attendance_data:
        attendance_data[name]["present"] += 1
    else:
        add_student(name)
        attendance_data[name]["present"] = 1


def mark_absent(name):
    if name in attendance_data:
        attendance_data[name]["absent"] += 1
    else:
        add_student(name)
        attendance_data[name]["absent"] = 1


def get_student_record(name):
    return attendance_data.get(name, None)


def calculate_attendance_percentage(name):
    record = attendance_data.get(name)
    if not record:
        return None
    total = record["present"] + record["absent"]
    if total == 0:
        return 0.0
    return (record["present"] / total) * 100


def get_students_with_warnings(absence_limit):
    return [name for name, record in attendance_data.items() if record["absent"] > absence_limit]


def get_all_records():
    return attendance_data.copy()


def reset_attendance():
    for record in attendance_data.values():
        record["present"] = 0
        record["absent"] = 0

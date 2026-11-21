
import matplotlib.pyplot as plt

students = [
    {"roll": 101, "name": "Rahul", "marks": 85},
    {"roll": 102, "name": "Aman", "marks": 78},
    {"roll": 103, "name": "Priya", "marks": 92}
]


def display_students():
    print("\n--- Student Records ---")
    for s in students:
        print(s["roll"], s["name"], s["marks"])


def add_student():
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Name: ").strip()
    marks = float(input("Enter Marks: "))

    if roll <= 0 or not name:
        print("Please enter valid details!")
        return

    if any(s["roll"] == roll for s in students):
        print("Roll Number already exists!")
        return

    if marks < 0 or marks > 100:
        print("Marks must be between 0 and 100!")
        return

    students.append({
        "roll": roll,
        "name": name,
        "marks": marks
    })

    print("Student Added Successfully!")


def delete_student(roll):
    global students
    students = [s for s in students if s["roll"] != roll]
    print("Student Deleted Successfully!")


def update_stats():
    total = len(students)

    average = (
        sum(s["marks"] for s in students) / total
        if total else 0
    )

    highest = max(
        (s["marks"] for s in students),
        default=0
    )

    print("\n--- Student Statistics ---")
    print("Total Students:", total)
    print("Average Marks:", round(average, 1))
    print("Highest Marks:", highest)


# Graph Function
def show_graph():

    if not students:
        print("No students available to show graph!")
        return

    names = [s["name"] for s in students]
    marks = [s["marks"] for s in students]

    plt.figure(figsize=(8, 5))

    bars = plt.bar(
        names,
        marks,
        color=["skyblue", "orange", "lightgreen", "pink"]
    )

    plt.title("Student Marks Comparison")
    plt.xlabel("Student Names")
    plt.ylabel("Marks")
    plt.ylim(0, 100)

    # Display marks above bars
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height + 1,
            str(height),
            ha="center"
        )

    plt.tight_layout()
    plt.show()


# Main Menu
while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Display Students")
    print("2. Add Student")
    print("3. Delete Student")
    print("4. Show Statistics")
    print("5. Show Marks Graph")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        display_students()

    elif choice == "2":
        add_student()

    elif choice == "3":
        roll = int(input("Enter Roll Number: "))
        delete_student(roll)

    elif choice == "4":
        update_stats()

    elif choice == "5":
        show_graph()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")

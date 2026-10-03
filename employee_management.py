# ============================================
#   Employee Management System
#   Simple version for beginner Python learners
# ============================================

# We store all employees in a list.
# Each employee is a dictionary (key-value pairs).
employees = []

# We use this to give each employee a unique ID number
next_id = 1


# ---------------------------------------------
# FUNCTION 1 : Add a new employee
# ---------------------------------------------
def add_employee():
    global next_id          # we need to change next_id, so mark it global

    print("\n--- Add New Employee ---")
    name       = input("Enter employee name   : ").strip()
    department = input("Enter department      : ").strip()
    position   = input("Enter position/role   : ").strip()

    # Simple input validation — name cannot be empty
    if not name:
        print("[ERROR] Name cannot be empty. Employee not added.")
        return

    # Ask for salary and make sure it is a valid number
    while True:
        salary_input = input("Enter salary (numbers only): ").strip()
        if salary_input.replace(".", "", 1).isdigit():
            salary = float(salary_input)
            break
        print("[!] Please enter a valid number for salary.")

    # Build the employee record as a dictionary
    employee = {
        "id"         : next_id,
        "name"       : name,
        "department" : department,
        "position"   : position,
        "salary"     : salary
    }

    employees.append(employee)   # add to our list
    next_id += 1                 # increment the ID counter

    print(f"[OK] Employee '{name}' added successfully with ID {employee['id']}!")


# ---------------------------------------------
# FUNCTION 2 : View all employees
# ---------------------------------------------
def view_all_employees():
    print("\n--- All Employees ---")

    if not employees:           # check if list is empty
        print("No employees found.")
        return

    # Print a simple table header
    print(f"{'ID':<5} {'Name':<20} {'Department':<15} {'Position':<15} {'Salary':>10}")
    print("-" * 70)

    for emp in employees:
        print(f"{emp['id']:<5} {emp['name']:<20} {emp['department']:<15} {emp['position']:<15} {emp['salary']:>10.2f}")


# ---------------------------------------------
# FUNCTION 3 : Search for an employee by name
# ---------------------------------------------
def search_employee():
    print("\n--- Search Employee ---")
    search_name = input("Enter name to search: ").strip().lower()

    # Go through every employee and check if the name matches
    found = []
    for emp in employees:
        if search_name in emp["name"].lower():   # partial match
            found.append(emp)

    if not found:
        print("[ERROR] No employee found with that name.")
        return

    print(f"\n[OK] Found {len(found)} result(s):")
    print(f"{'ID':<5} {'Name':<20} {'Department':<15} {'Position':<15} {'Salary':>10}")
    print("-" * 70)
    for emp in found:
        print(f"{emp['id']:<5} {emp['name']:<20} {emp['department']:<15} {emp['position']:<15} {emp['salary']:>10.2f}")


# ---------------------------------------------
# FUNCTION 4 : Update an existing employee
# ---------------------------------------------
def update_employee():
    print("\n--- Update Employee ---")

    # Ask for ID
    while True:
        id_input = input("Enter the Employee ID to update: ").strip()
        if id_input.isdigit():
            emp_id = int(id_input)
            break
        print("[!] Please enter a valid ID number.")

    # Find the employee with that ID
    target = None
    for emp in employees:
        if emp["id"] == emp_id:
            target = emp
            break

    if target is None:
        print("[ERROR] No employee found with that ID.")
        return

    print(f"\nCurrent details - Name: {target['name']} | Dept: {target['department']} | Position: {target['position']} | Salary: {target['salary']:.2f}")
    print("(Press ENTER to keep the current value)\n")

    # Update each field only if the user types something
    new_name = input(f"New name [{target['name']}]: ").strip()
    if new_name:
        target["name"] = new_name

    new_dept = input(f"New department [{target['department']}]: ").strip()
    if new_dept:
        target["department"] = new_dept

    new_pos = input(f"New position [{target['position']}]: ").strip()
    if new_pos:
        target["position"] = new_pos

    new_salary = input(f"New salary [{target['salary']:.2f}]: ").strip()
    if new_salary:
        if new_salary.replace(".", "", 1).isdigit():
            target["salary"] = float(new_salary)
        else:
            print("[!] Invalid salary -- keeping the old value.")

    print("[OK] Employee updated successfully!")


# ---------------------------------------------
# FUNCTION 5 : Delete an employee
# ---------------------------------------------
def delete_employee():
    print("\n--- Delete Employee ---")

    while True:
        id_input = input("Enter the Employee ID to delete: ").strip()
        if id_input.isdigit():
            emp_id = int(id_input)
            break
        print("[!] Please enter a valid ID number.")

    # Find and remove that employee
    for i, emp in enumerate(employees):
        if emp["id"] == emp_id:
            confirm = input(f"Are you sure you want to delete '{emp['name']}'? (yes/no): ").strip().lower()
            if confirm == "yes":
                employees.pop(i)
                print("[OK] Employee deleted successfully!")
            else:
                print("[CANCELLED] Deletion cancelled.")
            return

    print("[ERROR] No employee found with that ID.")


# ---------------------------------------------
# FUNCTION 6 : Show a small summary / stats
# ---------------------------------------------
def show_summary():
    print("\n--- Summary ---")

    if not employees:
        print("No employees to summarise.")
        return

    total    = len(employees)
    salaries = [emp["salary"] for emp in employees]
    avg_sal  = sum(salaries) / total
    max_emp  = max(employees, key=lambda e: e["salary"])
    min_emp  = min(employees, key=lambda e: e["salary"])

    # Count employees per department
    dept_count = {}
    for emp in employees:
        dept = emp["department"]
        dept_count[dept] = dept_count.get(dept, 0) + 1

    print(f"  Total employees   : {total}")
    print(f"  Average salary    : {avg_sal:.2f}")
    print(f"  Highest salary    : {max_emp['salary']:.2f}  ({max_emp['name']})")
    print(f"  Lowest salary     : {min_emp['salary']:.2f}  ({min_emp['name']})")
    print("\n  Employees per department:")
    for dept, count in dept_count.items():
        print(f"    - {dept:<20} : {count}")


# ---------------------------------------------
# MAIN MENU — this is where the program starts
# ---------------------------------------------
def main():
    print("=" * 50)
    print("   Welcome to Employee Management System")
    print("=" * 50)

    while True:   # keep showing the menu until the user exits
        print("\n--- MAIN MENU ---")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Show Summary")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ").strip()

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_all_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            show_summary()
        elif choice == "7":
            print("\nGoodbye! See you later.")
            break   # exit the loop → program ends
        else:
            print("[!] Invalid choice. Please enter a number between 1 and 7.")


# ---------------------------------------------
# Entry point — Python runs this block first
# ---------------------------------------------
if __name__ == "__main__":
    main()

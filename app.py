# ============================================
#  Employee Management System - Web Version
#  Backend: Python Flask
# ============================================

from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "emp_secret_key"   # needed for flash messages

# In-memory storage (like a list in RAM)
employees = []
next_id = 1


# ── HOME PAGE : show all employees ──────────
@app.route("/")
def index():
    return render_template("index.html", employees=employees)


# ── ADD EMPLOYEE ─────────────────────────────
@app.route("/add", methods=["GET", "POST"])
def add():
    global next_id
    if request.method == "POST":
        name       = request.form["name"].strip()
        department = request.form["department"].strip()
        position   = request.form["position"].strip()
        salary     = request.form["salary"].strip()

        # Simple validation
        if not name or not department or not position or not salary:
            flash("All fields are required!", "error")
            return redirect(url_for("add"))

        try:
            salary = float(salary)
        except ValueError:
            flash("Salary must be a number!", "error")
            return redirect(url_for("add"))

        employees.append({
            "id"         : next_id,
            "name"       : name,
            "department" : department,
            "position"   : position,
            "salary"     : salary
        })
        next_id += 1
        flash(f"Employee '{name}' added successfully!", "success")
        return redirect(url_for("index"))

    return render_template("add.html")


# ── EDIT EMPLOYEE ─────────────────────────────
@app.route("/edit/<int:emp_id>", methods=["GET", "POST"])
def edit(emp_id):
    # Find the employee
    target = next((e for e in employees if e["id"] == emp_id), None)
    if target is None:
        flash("Employee not found!", "error")
        return redirect(url_for("index"))

    if request.method == "POST":
        target["name"]       = request.form["name"].strip()
        target["department"] = request.form["department"].strip()
        target["position"]   = request.form["position"].strip()
        try:
            target["salary"] = float(request.form["salary"].strip())
        except ValueError:
            flash("Salary must be a number!", "error")
            return redirect(url_for("edit", emp_id=emp_id))

        flash(f"Employee '{target['name']}' updated!", "success")
        return redirect(url_for("index"))

    return render_template("edit.html", emp=target)


# ── DELETE EMPLOYEE ───────────────────────────
@app.route("/delete/<int:emp_id>")
def delete(emp_id):
    global employees
    before = len(employees)
    employees = [e for e in employees if e["id"] != emp_id]
    if len(employees) < before:
        flash("Employee deleted.", "success")
    else:
        flash("Employee not found!", "error")
    return redirect(url_for("index"))


# ── SEARCH EMPLOYEE ───────────────────────────
@app.route("/search")
def search():
    query = request.args.get("q", "").strip().lower()
    results = [e for e in employees if query in e["name"].lower()] if query else []
    return render_template("search.html", results=results, query=query)


# ── SUMMARY PAGE ──────────────────────────────
@app.route("/summary")
def summary():
    if not employees:
        return render_template("summary.html", stats=None)

    salaries   = [e["salary"] for e in employees]
    dept_count = {}
    for e in employees:
        dept_count[e["department"]] = dept_count.get(e["department"], 0) + 1

    stats = {
        "total"   : len(employees),
        "avg"     : sum(salaries) / len(salaries),
        "highest" : max(employees, key=lambda e: e["salary"]),
        "lowest"  : min(employees, key=lambda e: e["salary"]),
        "depts"   : dept_count
    }
    return render_template("summary.html", stats=stats)


# ── RUN THE SERVER ────────────────────────────
if __name__ == "__main__":
    print("Server started! Open Chrome and go to:  http://127.0.0.1:5000")
    app.run(debug=True, use_reloader=False)

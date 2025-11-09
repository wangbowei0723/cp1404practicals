"""
project_management
Estimate: 65 minutes
Actual: 79 minutes
"""

from project import Project
from datetime import datetime

FILENAME = "projects.txt"


def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    choice = ""
    while choice != "q":
        print("- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")

        choice = input(">>> ").lower()

        if choice == "l":
            filename = input("Filename: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")

        elif choice == "s":
            filename = input("Filename: ")
            save_projects(projects, filename)
            print(f"Projects saved to {filename}")

        elif choice == "d":
            display_projects(projects)

        elif choice == "f":
            date_str = input("Show projects that start after (dd/mm/yyyy): ")
            date = datetime.strptime(date_str, "%d/%m/%Y")
            filter_projects(projects, date)

        elif choice == "a":
            new_project = add_project()
            projects.append(new_project)

        elif choice == "u":
            for i, project in enumerate(projects):
                print(f"{i} {project}")
            index = int(input("Project choice: "))
            update_project(projects[index])

        elif choice == "q":
            print("Thank you for using the project manager!")

        else:
            print("Invalid option")


def load_projects(filename):
    projects = []
    with open(filename, "r") as file:
        next(file)  # Skip header
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) >= 5:
                try:
                    name = parts[0]
                    start_date = datetime.strptime(parts[1], "%d/%m/%Y")
                    priority = int(parts[2])
                    cost_estimate = float(parts[3])
                    completion_percentage = int(parts[4])
                    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
                    projects.append(project)
                except ValueError as e:
                    print(f"Error processing line: {line.strip()}. Error: {e}")
            else:
                print(f"Skipping invalid line: {line.strip()}")
    return projects

def save_projects(projects, filename):
    with open(filename, "w") as file:
        file.write("Name, Start Date, Priority, Cost Estimate, Completion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t {project.start_date.strftime('%d/%m/%Y')}"
                       f"\t {project.priority}\t {project.cost_estimate}"
                       f"\t {project.completion_percentage}\n")

def display_projects(projects):
    """Display project is incomplete or completed, sorted by priority."""
    incomplete = sorted([project for project in projects if not project.is_complete()])
    complete = sorted([project for project in projects if project.is_complete()])
    print("Incomplete projects:")
    for project  in incomplete:
        print(f"  {project }")
    print("Completed projects:")
    for project  in complete:
        print(f"  {project }")

def get_start_date(project):
    return project.start_date

def filter_projects(projects, after_date):
    filtered = []
    for project in projects:
        if project.start_date >= after_date:
            filtered.append(project)
    filtered.sort(key = get_start_date)
    for project in filtered:
        print(project)

def add_project():
    print("Let's add a new project")
    name = input("Name: ")
    date_str = input("Start date (dd/mm/yyyy): ")
    start_date = datetime.strptime(date_str, "%d/%m/%Y")
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: $"))
    percent = int(input("Percent complete: "))
    return Project(name, start_date, priority, cost, percent)

def update_project(project):
    print(project)
    new_percent = input("New Percentage: ")
    if new_percent:
        project.completion_percentage = int(new_percent)
    new_priority = input("New Priority: ")
    if new_priority:
        project.priority = int(new_priority)


main()
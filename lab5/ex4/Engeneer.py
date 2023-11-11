from ex4.Employee import Employee


class Engineer(Employee):
    def __init__(self, name, personal_id, phone_number, address, email, date_of_birth, salary, hire_date, company,
                 projects, programming_language):
        super().__init__(name, personal_id, phone_number, address, email, date_of_birth, salary, hire_date, company)
        self.projects = projects
        self.programming_language = programming_language

    def add_project(self, project):
        self.projects.append(project)

    def remove_project(self, project):
        self.projects.remove(project)

    def add_new_known_language(self, language):
        self.programming_language.append(language)

    def __str__(self):
        return super().__str__() + f"Projects: {self.projects}\n" \
                                   f"Programming language: {self.programming_language}\n"
from personal_info import PersonalInfo
from education import Education
from experience import Experience
from skills import Skills


class CVBuilder:
    def __init__(self):
        self.personal_info = None
        self.education = []
        self.experience = []
        self.skills = []

    def add_personal_info(self, name, email, phone, github, linkedin, stackoverflow):
        self.personal_info = PersonalInfo(name, email, phone, github, linkedin, stackoverflow)

    def add_education(self, degree, school, year, additional_info=None):
        self.education.append(Education(degree, school, year, additional_info))

    def add_experience(self, title, company, year):
        self.experience.append(Experience(title, company, year))

    def add_skills(self, skill_list):
        self.skills.append(Skills(skill_list))

    def display_cv(self):
        if self.personal_info:
            print("Personal Info:")
            print("Name:", self.personal_info.name)
            print("Email:", self.personal_info.email)
            print("Phone:", self.personal_info.phone)
            print("GitHub:", self.personal_info.github)
            print("LinkedIn:", self.personal_info.linkedin)
            print("Stack_Overflow:", self.personal_info.stackoverflow)
            print("\n")

        if self.education:
            print("Education:")
            for edu in self.education:
                print(edu.year, "-", edu.degree, "from", edu.school)
                if edu.additional_info:
                   for info in edu.additional_info:
                       print(info)
            print("\n")

        if self.experience:
            print("Experience:")
            for exp in self.experience:
                print(exp.year, "-", exp.title, "at", exp.company)
            print("\n")

        if self.add_skills:
            print("Skills:")
            for ski in self.skills:
                print(ski.skill_list)
            print("\n")


cv_builder = CVBuilder()
cv_builder.add_personal_info("Lozonschi Bogdan", "Bogdanlozonschi95@gmail.com", "0756901707", "https://github.com/Lozonschi", "https://www.linkedin.com/in/bogdan-lozonschi-7384a7262/", "https://stackoverflow.com/users/22305579/bogdan-lozonschi")
cv_builder.add_education(
    "Balneofiziokinetotherapy",
    "University of medicine,farmacy,science and tehnology George Emil Palade Targu Mures",
    "2021",
    ["assistance BFK", "Center for European Studies Piatra Neamt" ,"2018"])
cv_builder.add_experience("Python Developer(begginer)", "IT Factory.", "march 2023-july 2023")
cv_builder.add_skills(["Python", "QA", "SQL"])
cv_builder.display_cv()
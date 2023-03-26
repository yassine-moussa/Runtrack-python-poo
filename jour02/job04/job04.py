class Student:
    def __init__(self, first_name, last_name, student_id):
        self._first_name = first_name
        self._last_name = last_name
        self._student_id = student_id
        self._credits = 0
        self._level = self._student_eval()
        
    def add_credits(self, credits):
        if credits > 0:
            self._credits += credits
            self._level = self._student_eval()
        
    def crediteleve(self):
        return self._credits
    
    def get_student_fullname(self):
        return f"{self._first_name} {self._last_name}"
    
    def student_info(self):
        print(f"Le nombre de crédits de {self.get_student_fullname()} est de {self._credits} points")
        print(f"Nom = {self._last_name}\nPrénom = {self._first_name}\nid = {self._student_id}\nNiveau = {self._level}")
    
    def _student_eval(self):
        if self._credits >= 90:
            return "Excellent"
        elif self._credits >= 80:
            return "Très bien"
        elif self._credits >= 70:
            return "Bien"
        elif self._credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

etudiant1 = Student("John", "Doe", 145)
etudiant1.add_credits(100)
etudiant1.add_credits(10)
etudiant1.add_credits(10)

etudiant1.student_info()
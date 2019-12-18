# 1
class Spell:
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation
    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.get_description()
    def get_description(self):
        return 'No description'
    def execute(self):
        print(self.incantation)
class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')
            # class Confundo(Spell):
class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')
    def get_description(self):
        return 'Causes the victim to become confused and befuddled.'
    # def study_spell(spell):
    #    print(spell)
def study_spell(spell):
    print(spell)
spell = Accio()
spell.execute()
study_spell(spell)
study_spell(Confundo())
# 1 a : Parent Class : Spell
#       Child Classes : Accio and Confundo
# 1 b : Accio
#       Summoning Charm Accio
#       No description
#       Confundus Charm Confundo
#       Causes the victim to become confused and befuddled.
# 1 c : The get_description(self) in the Confundo class because the parameter in the study_spell() function is Confundo() and the class Confundo has the get_description(self) function.
# 1 d : class Accio(Spell):
#           def __init__(self):
#               Spell.__init__(self, 'Accio', 'Summoning Charm')
#           def getDescription(self):
#               return 'This charm summons an object to the caster, potentially over a significant distance'

# 2
class Choices:
    def __init__(self):
        self.id_number = ''
        self.name = ''
        self.position = ''
        self.salary = 0
    
    def new_staff(self, id_numbers, names, positions, salaries):
        print('New Staff')
        
        new_data = []
        
        while self.id_number[0] != 'S' or self.id_number[1] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or self.id_number[2] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or self.id_number[3] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or self.id_number[4] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or self.id_number == '' or self.id_number in id_numbers:
            self.id_number = str(input('Input ID [SXXXX]:'))
        id_numbers.append(self.id_number)
        new_data.append(self.id_number)
        
        while len(self.name) <= 0 or len(self.name) > 20:
            self.name = str(input('Input Name[0...20]:'))
        names.append(self.name)
        new_data.append(self.name)
        
        while self.position != 'Staff' or self.position != 'Officer' or self.position != 'Manager':
            self.position = str(input('Input Position[Staff|Officer|Manager]:'))
        positions.append(self.position)
        new_data.append(self.position)
        
        if self.position == 'Staff':
            while self.salary < 3500000 or self.salary > 7000000:
                self.salary = int(input("Input salary for " + self.position + ":"))
        elif self.position == 'Officer':
            while self.salary <= 7000000 or self.salary > 10000000:
                self.salary = int(input("Input salary for " + self.position + ":"))
        elif self.position == 'Manager':
            while self.salary <= 10000000:
                self.salary = int(input("Input salary for " + self.position + ":"))
        salaries.append(self.salary)
        new_data.append(self.position)

        return new_data

    def delete_staff(self, id_numbers):
        print('Delete Staff')
        
        delete = str(input('Input ID[SXXXX]:'))
        if delete in id_numbers:
            del id_numbers[id_numbers.index(delete)]
            print('Data has been successfully deleted')
        else:
            print('Data Not Found')
    
    def view_summary_data(self, salaries):
        staff_salaries = []
        officer_salaries = []
        manager_salaries = []
        
        for salary in salaries:
            if salary >= 3500000 or salary <= 7000000:
                staff_salaries.append(salary)
            elif salary > 7000000 or salary <= 10000000:
                officer_salaries.append(salary)
            elif salary > 10000000:
                manager_salaries.append(salary)
        
        print('1. Staff')
        print('Minimum Salary:' + str(min(staff_salaries)))
        print('Maximum Salary:' + str(max(staff_salaries)))
        total_staff_salaries = 0
        for salary in staff_salaries:
            total_staff_salaries += salary
        print('Average Salary:' + str(total_staff_salaries / len(staff_salaries)))

        print('2. Officer')
        print('Minimum Salary:' + str(min(officer_salaries)))
        print('Maximum Salary:' + str(max(officer_salaries)))
        total_officer_salaries = 0
        for salary in officer_salaries:
            total_officer_salaries += salary
        print('Average Salary:' + str(total_officer_salaries / len(officer_salaries)))

        print('3. Manager')
        print('Minimum Salary:' + str(min(manager_salaries)))
        print('Maximum Salary:' + str(max(manager_salaries)))
        total_manager_salaries = 0
        for salary in manager_salaries:
            total_manager_salaries += salary
        print('Average Salary:' + str(total_manager_salaries / len(manager_salaries)))

    def save_and_exit(self, new_data):
        with open('C:/Users/user/.vscode/data.txt','a') as f:
            f.write(new_data)
            
        
with open('C:/Users/user/.vscode/data.txt') as f:
    data = f.readlines()

    id_numbers = []
    names = []
    positions = []
    salaries = []

    for datum in data:
        datum = datum.split('#')
        print(datum)
        
        id_number = datum[0]
        id_numbers.append(id_number)

        name = datum[1]
        names.append(name)

        position = datum[2]
        positions.append(position)

        salary = datum[3]
        salaries.append(salary)
    
    print(id_numbers)
    print(names)
    print(positions)
    print(salaries)
    
    print('1. New Staff')
    print('2. Delete Staff')
    print('3. View Summary Data')
    print('4. Save & Exit')
    
    choice = int(input('Input Choice:'))
    if choice == 1:
        new_data = Choices.new_staff(id_numbers, names, positions, salaries)
    elif choice == 2:
        Choices.delete_staff(id_numbers)
    elif choice == 3:
        Choices.view_summary_data(salaries)
    elif choice == 4:
        Choices.save_and_exit(new_data)
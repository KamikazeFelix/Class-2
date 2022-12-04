class Facilities:
    facilitylist = []
    def __init__(self, facilities=""):
        self.facilities = facilities
    
    def displayFacilities(self):
        f = open('facilities.txt','r')
        lines = f.readlines()
        for line in lines:
            print(line)
        f.close()
        print('\nBack to the previous menu')


    def addFacility(self):
        add_facility = input('Enter facility name:\n') 
        self.facilitylist.append(add_facility) 
        
        
    def writeListOffacilitiesToFile(self):
        f = open('facilities.txt','a')
        for facilityadd in self.facilitylist:
            f.write('\n'+facilityadd)
        f.close()
        print('Back to the previous menu')

            
  

while True:
    print('Welcome to Alberta Hospital  (AH) Managment system! ')
    choose = input('''Please select from the following options, or select 0 to stop:
                    1 - 	Doctors
                    2 - 	Facilities
                    3 - 	Laboratories
                    4 - 	Patients
                    \n''')
    if choose == '2':
        while True:
                choose2 = input('''Facilities Menu:
                                    1 - Display Facilities list
                                    2 - Add Facility
                                    3 - Back to the Main Menu
                                    \n''')
                if choose2 == '1':
                    Facilities().displayFacilities()
                elif choose2 == '2':
                    Facilities().addFacility() 
                    Facilities().writeListOffacilitiesToFile()
                elif choose2 == '3':
                    break
                else:
                    print('Please enter a valid number!')
            




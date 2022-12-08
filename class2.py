class Doctor:
    listdoctors =[]

    def __init__(self,ID='',Name='',Speciality='',Timing='',Qualification='',roomNb=''):
        self.ID = ID
        self.Name = Name
        self.Speciality = Speciality
        self.Timing = Timing
        self.Qualification = Qualification
        self.roomNb = roomNb

    def formatDrInfo(self):
        return '{:<5} {:<12} {:<12} {:<10} {:<15} {:<10}'.format(self.ID,self.Name,self.Speciality,self.Timing,self.Qualification,self.roomNb)
    
    def __str__(self):
        format=self.formatDrInfo()
        return format

    def enterDrInfo(self):
        self.ID = input('Enter the doctor\'s ID:\n')
        self.Name = input('Enter the doctor\'s name:\n')
        self.Speciality = input('Enter the doctor\'s speciality:\n')
        self.Timing = input('Enter the doctor\'s timing (e.g, 7am-10pm):\n')
        self.Qualification = input('Enter the doctor\'s qualification:\n')
        self.roomNb = input('Enter the doctor\'s room number:\n')
        self.listdoctors.append(Doctor(self.ID,self.Name,self.Speciality,self.Timing,self.Qualification,self.roomNb))
        return self.listdoctors
    
    def readDoctorsFile(self):
        f = open('doctors.txt','r')
        lines = f.readlines()
        for line in lines:
            splitline = line.split('_')
            doctor = Doctor(
                ID = splitline[0],
                Name = splitline[1],
                Speciality = splitline[2],
                Timing = splitline[3],
                Qualification = splitline[4],
                roomNb = splitline[5]
            )
            self.listdoctors.append(doctor)
        f.close()    
        

    def displayDoctorInfo(self):
        for doctor in self.listdoctors:
            print(doctor)

    def searchDoctorByID(self):
        i = input('Enter the doctor Id:\n')
        for n in self.listdoctors:
            if i == n.ID:
                print(n)
                return
        print('Can\'t find the doctor with the same ID on the system')

    def searchDoctorByName(self):
        i = input('Enter the doctor Name:\n')
        for n in self.listdoctors:
            if i == n.Name:
                print(n)
                return
        print('Can\'t find the doctor with the same Name on the system')

    def editDoctorInfo(self):
        i = input('Enter the  ID of  the doctor to change their information:\n')
        name = input('Enter new name:\n')
        spec = input('Enter new specialist in:\n')
        timi = input('Enter new timing:\n')
        qual = input('Enter new qualification:\n')
        room = input('Enter new room number:\n')
        for new in self.listdoctors:
            if i == new.ID:
                new.Name = name 
                new.Specialist = spec
                new.Timing = timi
                new.Qualification = qual
                new.RoomNb  = room
        return self.listdoctors

    def writeListOfDoctorsToFile(self):
        f = open('doctors.txt','w')
        for i in self.listdoctors:
            f.write(i.ID + '_' + i.Name + '_' + i.Speciality + '_' + i.Timing + '_' + i.Qualification + '_' + i.roomNb+"\n")

    def addDrToFile(self):
        f = open('doctors.txt','a')
        i = self.listdoctors[-1]
        f.write('\n' + i.ID + '_' + i.Name + '_' + i.Speciality + '_' + i.Timing + '_' + i.Qualification + '_' + i.roomNb)



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

class Lab:
    lab_list = []
    def __init__(self, lab="", cost="" ):
        self.lab = lab
        self.cost = cost

    def readLaboratoriesFile(self): 
        f = open('laboratories.txt', 'r')
        lines = f.readlines()
        for line in lines:
            splitline = line.split('_')
            Object = Lab(splitline[0], splitline[1])
            self.lab_list.append(Object)
        f.close()


    def writeListOfLabsToFile(self): 
            f = open('laboratories.txt', 'r')
            data = f.read()
            data = data.replace('Facility','Lab')
            f.close()
            f = open('laboratories.txt', 'w')
            f.write(data)
            f.close()

    def displayLabsList(self): 
        for i in range(len(self.lab_list)):
            print("{:<12} {:<12}".format(self.lab_list[i].lab, self.lab_list[i].cost))
        print('Back to the prevoius Menu')
        
    def enterLaboratoryInfo(self): 
        add_lab = input('Enter Laboratory facility:\n')
        add_cost = input('Enter Laboratory cost:\n')
        addObject = Lab(add_lab, add_cost)
        self.lab_list.append(addObject)
        return add_lab, add_cost

    def formatDrInfo(self): 
        add = Lab().enterLaboratoryInfo()
        format = ['\n', add[0] ,'_', add[1]]
        return format 

    def addLabToFile(self): 
        f = open('laboratories.txt', 'a')            
        lab_cost = Lab().formatDrInfo()
        f.write(''.join(lab_cost))
        f.close()
        print('Back to the prevoius Menu')
            

while True:
    print('Welcome to Alberta Hospital  (AH) Managment system! ')
    choose = input('''Please select from the following options, or select 0 to stop:
                    1 - 	Doctors
                    2 - 	Facilities
                    3 - 	Laboratories
                    4 - 	Patients
                    \n''')

    if choose == '1':
        Doctor().readDoctorsFile()
        while True:
            choose1 = input('''Laboratories Menu:
                                1 - Display Doctors list
                                2 - Search for doctor by ID
                                3 - Search for doctor by name
                                4 - Add doctor
                                5 - Edit doctor info
                                6 - Back to the Main Menu
                                \n''')
            if choose1 =='1':
                Doctor().displayDoctorInfo()
            elif choose1 == '2':
                Doctor().searchDoctorByID()
            elif choose1 == '3':
                Doctor().searchDoctorByName()
            elif choose1 == '4':
                Doctor().enterDrInfo()
                Doctor().addDrToFile()
            elif choose1 == '5':
                Doctor().editDoctorInfo()
                Doctor().writeListOfDoctorsToFile()
            elif choose1 == '6':
                break
            else:
                print('Please enter a valid number!')
                
            
    elif choose == '2':
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
    elif choose == '3':
        Lab().writeListOfLabsToFile()
        Lab().readLaboratoriesFile()
        while True:
            choose3 = input('''Laboratories Menu:
                                1- Display laboratories list
                                2- Add laboratory
                                3- Back to the Main Menu
                                \n''')
            if choose3 == '1':
                Lab().displayLabsList()
            elif choose3 == '2':
                Lab().addLabToFile()
            elif choose3 == '3':
                break
            else:
                print('Please enter a valid number!')
            


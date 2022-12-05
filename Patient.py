class Patient:
    
    def __init__(self, pid, name,disease,gender,age):
        self.pid=pid
        self.name=name
        self.disease=disease
        self.gender=gender
        self.age=age
        
    def formatPatientInfo(self):
        return "{:<5}   {:<23}   {:<16}   {:<16}   {:<8}".format(self.pid,self.name,self.disease,self.gender,self.age)
    def __str__(self):
        format=self.formatPatientInfo()
        return format            
patient_object_list=[]
def readPatientsFile():
    f=open("patients.txt","r")
    for x in f:
        if x == "\n":
            return patient_object_list     
        patient_info=x.strip().split("_")
        patient_object_list.append(Patient(patient_info[0],patient_info[1],patient_info[2],patient_info[3],patient_info[4]))

def displayPatientsList():
    for i in patient_object_list:
        print(i)

def searchPatientById():
    patient_id=input("Enter the Patient Id:\n")
    patient_id_list=[]
    for i in patient_object_list:
        patient_id_list.append(i.pid)
    if patient_id in patient_id_list:
        print(i)
    else:
        print("Can't find the Patient with the same id on the system")  

def enterPatientInfo():
    pid=input("Enter Patient id: ")
    name=input("Enter Patient name: ")
    disease =input("Enter Patient disease: ")
    gender=input("Enter Patient gender: ")
    age =input("Enter Patient age: ")
    patient_object_list.append(Patient(pid,name,disease,gender,age))
    return patient_object_list
    

def editPatientInfo():
    patient_id=input("Please enter the id of the Patient that you want to edit their information: ")
    name_new=input("Enter new Patient name: ")
    disease_new =input("Enter new Patient disease: ")
    gender_new=input("Enter new Patient gender: ")
    age_new =input("Enter new Patient age: ")
    for i in patient_object_list:
        if i.pid==patient_id:
            i.name=name_new
            i.disease=disease_new
            i.gender=gender_new
            i.age=age_new
    return patient_object_list

def writeListOfPatientsToFile():
    f=open("patients.txt","w")
    for i in patient_object_list:
        f.write(i.pid+"_"+i.name+"_"+i.disease+"_"+i.gender+"_"+i.age+"\n" )
    f=open("patients.txt","r")
    print(f.read())

def addPatientToFile():
    f=open("patients.txt","a")
    i=patient_object_list[-1]
    f.write(i.pid+"_"+i.name+"_"+i.disease+"_"+i.gender+"_"+i.age+"\n" )
    f=open("patients.txt","r")
    print(f.read())

def patient_menu():
    readPatientsFile()
    while 1!=0:
        patient_menu=input("Patients Menu:\n1 - Display patients list\n2 - Search for patient by ID\n3 - Add patient\n4 - Edit patient info\n5 - Back to the Main Menu\n")
        match patient_menu:
            case "1":
                displayPatientsList()
            case "2":
                searchPatientById()
            case "3":
                enterPatientInfo()
                addPatientToFile()
            case "4":
                editPatientInfo()
                writeListOfPatientsToFile()
            case "5":
                break

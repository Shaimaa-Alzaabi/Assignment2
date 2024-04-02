class Patient:
    def __init__(self, name, age, condition):
        self.name = name
        self.age = age
        self.condition = condition
        self.appointment = None
        self.medications = []  # Store patient's medications

    def add_medication(self, medicine, dosage):
        self.medications.append((medicine, dosage))

    def display_summary(self):
        print(f"Name: {self.name}, Age: {self.age}, Condition: {self.condition}")
        if self.appointment:
            print(f"Next Appointment: {self.appointment}")
        else:
            print("No appointment scheduled.")
        if self.medications:
            print("Medications:")
            for medicine, dosage in self.medications:
                print(f"- {medicine}: {dosage}")
        else:
            print("No medications prescribed.")


class Hospital:
    def __init__(self):
        self.patient_records = []
        self.doctors = []
        self.queue = []
        self.prescriptions = []

    def add_patient(self, patient):
        self.patient_records.append(patient)

    def update_patient(self, name, new_condition):
        for patient in self.patient_records:
            if patient.name == name:
                patient.condition = new_condition
                print("Patient record updated successfully.")
                return
        print("Patient not found.")

    def remove_patient(self, name):
        for patient in self.queue:
            if patient.name == name:
                self.queue.remove(patient)
                print("Patient removed from the queue.")
                return
        print("Patient not found in the queue.")

    def display_queue(self):
        if not self.queue:
            print("No patients in the queue.")
        else:
            print("Patients in queue:")
            for patient in self.queue:
                print(patient.name)

    def add_to_queue(self, patient):
        self.queue.append(patient)
        print("Patient added to the queue.")

    def schedule_appointment(self, patient_name, doctor_name):
        for patient in self.patient_records:
            if patient.name == patient_name:
                for doctor in self.doctors:
                    if doctor.name == doctor_name:
                        if patient.appointment is None:
                            patient.appointment = doctor_name
                            doctor.appointments.append(patient_name)
                            print(f"Appointment scheduled for {patient_name} with {doctor_name}.")
                            return
                        else:
                            print("Patient already has an appointment.")
                            return
                print("Doctor not found.")
                return
        print("Patient not found.")

    def issue_prescription(self, patient_name, medicine, dosage):
        for patient in self.patient_records:
            if patient.name == patient_name:
                prescription = Prescription(medicine, dosage)
                self.prescriptions.append((patient_name, prescription))
                print(f"Prescription issued for {patient_name}: {medicine}, dosage: {dosage}.")
                return
        print("Patient not found.")

    def display_prescriptions(self):
        if not self.prescriptions:
            print("No prescriptions issued.")
        else:
            print("Prescriptions:")
            for patient_name, prescription in self.prescriptions:
                print(f"Patient: {patient_name}, Medicine: {prescription.medicine}, Dosage: {prescription.dosage}")

    def display_patient_records(self):
        if not self.patient_records:
            print("No patient records available.")
        else:
            print("Patient Records:")
            for patient in self.patient_records:
                print(f"Name: {patient.name}, Age: {patient.age}, Condition: {patient.condition}, "
                      f"Appointment: {patient.appointment}")

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def display_doctors(self):
        if not self.doctors:
            print("No doctors available.")
        else:
            print("Available Doctors:")
            for doctor in self.doctors:
                print(doctor.name)

    def search_patient(self, criteria):
        found = False
        for patient in self.patient_records:
            if criteria.lower() in patient.name.lower() or criteria.lower() in patient.condition.lower():
                patient.display_summary()
                found = True
        if not found:
            print("No matching patient records found.")

    def authenticate(self, username, password):
        # Simple authentication mechanism for demonstration purposes
        if username == "admin" and password == "password":
            return True
        else:
            return False


class Doctor:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty
        self.appointments = []


class Prescription:
    def __init__(self, medicine, dosage):
        self.medicine = medicine
        self.dosage = dosage


# Menu interface
def main_menu():
    print("\nMain Menu:")
    print("1. Add a new patient")
    print("2. Update patient information")
    print("3. Remove patient from queue")
    print("4. Show patients waiting for doctor")
    print("5. Schedule appointment")
    print("6. Issue prescription")
    print("7. Show patient records")
    print("8. Display prescriptions")
    print("9. Display available doctors")
    print("10. Search for patient")
    print("11. Exit")


# Function to display available doctors
def display_available_doctors(hospital):
    hospital.display_doctors()


# Function to test functionalities
def test_functionality(hospital):
    # Adding sample patient records
    patient1 = Patient("Shaimaa", 35, "Fever")
    patient2 = Patient("Shatha", 45, "Hypertension")
    patient1.add_medication("Paracetamol", "500mg")
    patient2.add_medication("Lisinopril", "10mg")
    hospital.add_patient(patient1)
    hospital.add_patient(patient2)

    # Displaying patient records
    hospital.display_patient_records()

    # Testing search functionality
    print("\nSearching for patients with 'Shaimaa' in their name:")
    hospital.search_patient("Shaimaa")

    # Testing security implementation
    username = input("Enter username: ")
    password = input("Enter password: ")
    if hospital.authenticate(username, password):
        print("Authentication successful. Access granted to patient records.")
        hospital.display_patient_records()
    else:
        print("Authentication failed. Access denied.")


# Sample usage/testing
hospital = Hospital()
test_functionality(hospital)

while True:
    main_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter patient's name: ")
        age = int(input("Enter patient's age: "))
        condition = input("Enter patient's condition: ")
        patient = Patient(name, age, condition)
        hospital.add_patient(patient)

    elif choice == "2":
        name = input("Enter patient's name: ")
        new_condition = input("Enter new condition: ")
        hospital.update_patient(name, new_condition)

    elif choice == "3":
        name = input("Enter patient's name: ")
        hospital.remove_patient(name)

    elif choice == "4":
        hospital.display_queue()

    elif choice == "5":
        patient_name = input("Enter patient's name: ")
        doctor_name = input("Enter doctor's name: ")
        hospital.schedule_appointment(patient_name, doctor_name)

    elif choice == "6":
        patient_name = input("Enter patient's name: ")
        medicine = input("Enter prescribed medicine: ")
        dosage = input("Enter dosage: ")
        hospital.issue_prescription(patient_name, medicine, dosage)

    elif choice == "7":
        hospital.display_patient_records()

    elif choice == "8":
        hospital.display_prescriptions()

    elif choice == "9":
        display_available_doctors(hospital)

    elif choice == "10":
        search_criteria = input("Enter search criteria (name or condition): ")
        hospital.search_patient(search_criteria)

    elif choice == "11":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

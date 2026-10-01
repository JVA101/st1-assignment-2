from patient import Patient
from practitoner import Practitioner
from appointment import Appointment


class ClinicDatabase:
    # reads and write CSV files for the program

    def __init__(self):
        self.patient_file:str = 'patient.csv'
        self.practitioner_file:str = 'practitioner.csv'
        self.appointment_file:str = 'appointment.csv'


    def verify_files_exist(self):
        # checks that all three files exist, if not raises error
        pass


    # __________patient file operations_____________
    def insert_patient(self, patient:Patient):
        # append a new patient profile row into patient CSV
        pass


    def get_patient(self, patient_id):
        # returns a row for one patient, otherwise None if not found
        pass


    def update_patient(self, patient_id, fields):
        # overwrites the named field of a patient's profile row
        pass


    def archive_flag_patient(self, patient_id):
        # set the field is_archived flag on a patient's profile row
        pass


    # _________practitioner file operations_________
    def insert_practitioner(self, practitioner:Practitioner):
        # append a new practitioner profile row into practitioner CSV
        pass

    def get_practitioner(self, practitioner_id):
        # returns a row for one practitioner, otherwise None if not found
        pass

    def update_practitioner(self, practitioner_id, fields):
        # overwrites the named field of a practitioner's profile row
        pass

    def archive_flag_practitioner(self, practitioner_id):
        # set the field is_archived flag on a practitioner's profile row
        pass


    # _________appointment file operations__________
    def insert_appointment(self, appointment:Appointment):
        # append a new appointment profile row into appointment CSV
        pass

    def get_appointment(self, appointment_id):
        # returns a row for one appointment, otherwise None if not found
        pass

    def update_appointment(self, appointment_id, fields):
        # overwrites the named field of an appointment's row
        pass

    def archive_flag_appointment(self, appointment_id):
        # set the field is_archived flag on an appointment's row
        pass


    def fetch_all_appointments(self):
        # gets every appointment row
        pass


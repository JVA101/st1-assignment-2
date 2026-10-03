from contact import ContactDetails, ResidentialAddress
from clinic_database import ClinicDatabase


class Patient:
    # structure of Smart Care patient class

    def __init__(self, patient_id:int, f_name:str, l_name:str, m_name:str, DOB:int, sex:str, contact:ContactDetails,
                 address:ResidentialAddress, is_archived:bool=False):

        self._patient_id = patient_id
        self._f_name = f_name
        self._l_name = l_name
        self._m_name = m_name
        self._DOB = DOB
        self._sex = sex
        self._contact = contact
        self._address = address
        self._is_archived = is_archived


    def get_patient_id(self):
        # gets patient's id
        pass


    def get_full_name(self):
        # gets patients first, middle, and last name
        pass


    def get_patient_DOB(self):
        # gets patients DOB
        pass



class PatientManager:
    # handles operations on patient class

    def __init__(self, db:ClinicDatabase):
        # what the class needs to run operations
        self.db = db


    def register_patient (self, patient_id:int, f_name:str, l_name:str, m_name:str, DOB:int, sex:str, contact:ContactDetails,
                 address:ResidentialAddress, is_archived:bool=False):
        # creates a new patient profile
        pass


    def delete_patient(self, patient_id:int):
        # permanently deletes patient record
        pass


    def update_patient(self, patient_id:int, fields):
        # changes one or more fields of an existing patient record
        pass


    def archive_patient(self, patient_id:int):
        # archives patient profile
        pass


    def patient_search(self, f_name:str, l_name:str, DOB:int):
        # returns the patients matching
        pass



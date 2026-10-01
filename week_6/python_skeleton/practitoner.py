from enum import Enum
from contact import ContactDetails, ResidentialAddress
from clinic_database import ClinicDatabase


class PractitionerStatus(Enum):
    # availability status of practitioner

    ACTIVE = 'ACTIVE'
    PROFESSIONAL_LEAVE = 'PROFESSIONAL_LEAVE'
    EDUCATION_LEAVE = 'EDUCATION_LEAVE'
    ANNUAL = 'ANNUAL'
    SICK = 'SICK'
    LONG_SERVICE = 'LONG_SERVICE'
    PAID = 'PAID'
    UNPAID = 'UNPAID'
    COMPASSIONATE = 'COMPASSIONATE'
    FAMILY_DOMESTIC_VIOLENCE = 'FAMILY_DOMESTIC_VIOLENCE'
    CEREMONIAL = 'CEREMONIAL'
    COMMUNITY_SERVICE = 'COMMUNITY_SERVICE'
    DEFENCE_FORCE = 'DEFENCE_FORCE'


class Practitioner:
    # structure of Smart Care practitioner class

    def __init__(self, practitioner_id:int, status: PractitionerStatus.ACTIVE,f_name:str, l_name:str, m_name:str, DOB:int, sex:str,
                 profession:str, shift_availability:int, contact:ContactDetails, address:ResidentialAddress, is_archived:bool=False):

        self._practitioner_id = practitioner_id
        self._status = status
        self._f_name = f_name
        self._l_name = l_name
        self._m_name = m_name
        self._DOB = DOB
        self._sex = sex
        self._profession = profession
        self._shift_availability = shift_availability
        self._contact = contact
        self._address = address
        self._is_archived = is_archived


    def get_practitioner_id(self,):
        # gets practitioner's id
        pass


    def get_property(self, name):
        # return a single appointment field by name
        pass



class PractitionerManager:
    # handles operations on practitioner class

    def __init__(self, db:ClinicDatabase):
        # what the class needs to run operations

        self.db = db


    def register_practitioner(self, practitioner_id:int, status: PractitionerStatus.ACTIVE,f_name:str, l_name:str, m_name:str,
                              DOB:int, sex:str, specialisation:str, shift_availability:int, contact:ContactDetails,
                              address:ResidentialAddress, is_archived:bool=False):
        # creates a new practitioner profile
        pass


    def delete_practitioner(self, practitioner_id:int):
        # permanently deletes practitioner record
        pass


    def update_practitioner(self, practitioner_id:int, fields):
        # changes one or more fields of an existing practitioner record
        pass


    def archive_practitioner(self, practitioner_id:int):
        # archives practitioner profile
        pass


    def change_availability(self, practitioner_id:int, new_schedule:list[str] ):
        # changes practitioner's availability, slots defined in main
        pass


    def practitioner_search(self, practitioner_id:int):
        # returns the patients matching
        pass

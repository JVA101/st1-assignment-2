from enum import Enum
from clinic_database import ClinicDatabase
from practitoner import PractitionerStatus


class AppointmentStatus(Enum):
    # lifecycle status of appointment

    ACTIVE = 'ACTIVE'
    ARRIVED = 'ARRIVED'
    CANCELLED = 'CANCELLED'
    NO_SHOW = 'NO_SHOW'
    COMPLETED = 'COMPLETED'


class Appointment:
    # structure of Smart Care appointment class

    def __init__(self, appointment_id:int, date_time:int, patient_id:int, practitioner_id:int, status: AppointmentStatus,
                 _is_archived:bool=False):

        self._appointment_id = appointment_id
        self._date_time = date_time
        self._patient_id = patient_id
        self._practitioner_id = practitioner_id
        self._status = status
        self._is_archived = _is_archived


    def get_appointment_id(self):
        # gets patient id
        pass


    def get_property(self, name):
        # return a single appointment field by name
        pass


class AppointmentManager:
    # handles operations on appointment class

    def __init__(self, db:ClinicDatabase, patient_manager, practitioner_manager):
        self._db = db
        self._patient_manager = patient_manager
        self._practitioner_manager = practitioner_manager


    def create_booking(self, patient_id:int, practitioner_id:int, date_time:int):
        # books an appointment
        pass


    def update_booking(self, appointment_id:int, fields:str):
        # changes one or more of the allowable fields in an existing appointment
        pass


    def cancel_booking(self, appointment_id:int):
        # cancels existing appointment
        pass


    def delete_booking(self, appointment_id:int):
        # delete an existing booking permanently
        pass


    def archive_appointment(self, appointment_id:int):
        # archives an appointment
        pass


    def sort_appointments(self, appointments_list:list[Appointment], sort_field:str):
        # returns appointments in order by key given
        pass


    def list_appointments(self):
        # will return a list of all the appointments from database
        pass


    def get_available_slots(self, practitioner_id:int, date:int):
        # returns free slots for a practitioner on a given date
        pass


    def find_patient_appointments(self, patient_id:int):
        # gets every appointment that belongs to the patient
        pass


    def practitioner_appointments(self, practitioner_id:int):
        # gets all the appointments that belongs to a practitioner
        pass


    def change_status(self, appointment_id:int, new_status:PractitionerStatus):
        # changes an appointment's AppointmentStatus
        pass
from datetime import date, datetime

from fontTools.misc.cython import returns

from handout_patient import Patient, PatientManager
from handout_practitioner import Practitioner, PractitionerManager
from ai_handout_appointment import (Appointment, AppointmentStatus,
                                    InvalidAppointmentData, InvalidAppointmentState,
                                    InvalidAppointmentStatus)


# _____________________________________
# __________Patient tests______________
patient = Patient(patient_id=123456789,
                  f_name='Howl',
                  m_name='Jenkins',
                  l_name='Pendragon',
                  dob=date(1986,1,27),
                  sex='Male')

patient_mgr = PatientManager()
patient_mgr.register_patient(patient_id=123456789,
                  f_name='Howl',
                  m_name='Jenkins',
                  l_name='Pendragon',
                  dob=date(1986,1,27),
                  sex='Male')

# Patient getters_________
print(f'\t',patient.get_f_name())
print(f'\t',patient.get_m_name())
print(f'\t',patient.get_l_name())
print(f'\t',patient.get_dob())
print(f'\t',patient.get_patient_id())


# Patient invalid inputs_____
patient_mgr.register_patient(patient_id=0, f_name='Howl', m_name='Jenkins', l_name='Pendragon', dob=date(1986,1,27), sex='Male')            # invalid id
patient_mgr.register_patient(patient_id=123456789, f_name='Howl', m_name='Jenkins', l_name='Pendragon', dob=date(1986,1,27), sex='Male')    # duplicate id
patient_mgr.register_patient(patient_id=123456789, f_name='', m_name='Jenkins', l_name='Pendragon', dob=date(1986,1,27), sex='Male')        # empty first name
patient_mgr.register_patient(patient_id=123456789, f_name='Howl', m_name='Jenkins', l_name='', dob=date(1986,1,27), sex='Male')             # empty last name
patient_mgr.register_patient(patient_id=123456789, f_name='Howl', m_name='Jenkins', l_name='Pendragon', dob=date(1986,1,27), sex='Wizard')  # invalid sex

print(len(patient_mgr._patients)) # amount of patients registered, should be 1


# __________________________________________
# ____________Practitioner tests____________
practitioner = Practitioner(practitioner_id=987654321,
                            f_name='Calcifer',
                            m_name='Flame',
                            l_name='Spirit',
                            specialty='Cardiologist')

practitioner_mgr = PractitionerManager()
practitioner_mgr.register_practitioner(practitioner_id=987654321,
                            f_name='Calcifer',
                            m_name='Flame',
                            l_name='Spirit',
                            specialty='Cardiologist')

# Practitioner getters_________
print(f'\t',practitioner.get_f_name())
print(f'\t',practitioner.get_m_name())
print(f'\t',practitioner.get_l_name())
print(f'\t',practitioner.get_specialty())
print(f'\t',practitioner.get_practitioner_id())

# Practitioner invalid inputs__________
practitioner_mgr.register_practitioner(practitioner_id=0, f_name='Calcifer', m_name='Flame', l_name='Spirit', specialty='Cardiologist')         # invalid id
practitioner_mgr.register_practitioner(practitioner_id=987654321, f_name='Calcifer', m_name='Flame', l_name='Spirit', specialty='Cardiologist') # duplicate id
practitioner_mgr.register_practitioner(practitioner_id=2, f_name='', m_name='Flame', l_name='Spirit', specialty='Cardiologist')                 # empty first name
practitioner_mgr.register_practitioner(practitioner_id=3, f_name='Calcifer', m_name='Flame', l_name='', specialty='Cardiologist')               # empty last name
practitioner_mgr.register_practitioner(practitioner_id=4, f_name='Calcifer', m_name='Flame', l_name='Spirit', specialty='')                     # empty specialty

print(len(practitioner_mgr._practitioners)) # amount of practitioners registered, should be 1





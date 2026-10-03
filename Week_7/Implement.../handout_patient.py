from datetime import date


class Patient:
    # patient object data model with getters and setters

    # list of options for the sex attribute
    SEX = ['Female', 'Male', 'Intersex', 'Another term', 'Prefer not to say']

    def __init__(self, patient_id:int, f_name:str, m_name:str, l_name:str, dob:date, sex:str):
        self._patient_id = patient_id
        self._f_name = f_name
        self._m_name = m_name
        self._l_name = l_name
        self._dob = dob
        self._sex = sex

        # checks patients sex against SEX list above
        if sex not in Patient.SEX:
            raise ValueError(f'sex must either be {Patient.SEX}')


    # ______patient setters______
    def set_f_name(self, f_name:str):
        self._f_name = f_name


    def set_m_name(self, m_name:str):
        self._m_name = m_name


    def set_l_name(self, l_name:str):
        self._l_name = l_name


    def set_dob(self, dob:date):
        self._dob = dob


    def set_sex(self, sex:str):
        try:
            if sex not in Patient.SEX:
                raise ValueError(f'sex must either be {Patient.SEX}')
            self._sex = sex
        except ValueError as error:
            print('Error:', error)


    # ______patient getters______
    def get_f_name(self) -> str:
        return self._f_name


    def get_m_name(self) -> str:
        return self._m_name


    def get_l_name(self) -> str:
        return self._l_name


    def get_dob(self)-> date:
        return self._dob


    def get_patient_id(self) -> int:
        return self._patient_id


class PatientManager:
    # does operations on patient object

    def __init__(self):
        self._patients = []


    def register_patient(self, patient_id:int, f_name:str, m_name:str, l_name:str, dob:date, sex:str):
        try:
            # exception handling
            if patient_id <=0:
                raise ValueError('Patient id is not valid')

            if f_name == '':
                raise ValueError('First name cannot be empty')

            if l_name == '':
                raise ValueError('Last name cannot be empty')

            if not isinstance(dob, date):
                raise ValueError('Date of birth must be a date')

            if sex not in Patient.SEX:
                raise ValueError(f'sex must either be {Patient.SEX}')

            for existing in self._patients:
                # checks if patient already exist using the unique identifier
                if existing.get_patient_id() == patient_id:
                    raise ValueError('This id already belongs to a patient')

            # adds new patient
            new_patient = Patient(patient_id, f_name, m_name, l_name, dob, sex)
            self._patients.append(new_patient)
            print('Patient registered.')

        except ValueError as error:
            # catch all errors
            print('Could not register patient:', error)


    def delete_patient(self, patient_id:int):
        try:
            if patient_id <= 0:
                raise ValueError('Patient id not valid')

            found = None
            for patient in self._patients:
                if patient.get_patient_id() == patient_id:
                    found = patient
                    break

            if found is None:
                raise ValueError('No patient with this id was found')

            self._patients.remove(found)
            print('Patient deleted.')

        except ValueError as error:
            print('Could not delete patient:', error)


    def update_patient(self, patient_id:int, f_name:str, m_name:str, l_name:str, dob:date, sex:str):
        try:
            # exception handling
            if patient_id <=0:
                raise ValueError('Patient id is not valid')

            if f_name == '':
                raise ValueError('First name cannot be empty')

            if m_name == '':
                raise ValueError('Last name cannot be empty')

            if l_name == '':
                raise ValueError('Last name cannot be empty')

            if sex not in Patient.SEX:
                raise ValueError(f'sex must either be {Patient.SEX}')

            found = None
            for patient in self._patients:
                if patient.get_patient_id() == patient_id:
                    found = patient
                    break

            if found is None:
                raise ValueError('No patient with this id was found')

            # overwrites old field values with new ones
            found.set_f_name(f_name)
            found.set_m_name(m_name)
            found.set_l_name(l_name)
            found.set_sex(sex)
            found._dob = dob
            print('Patient updated.')

        except ValueError as error:
            print('Could not update patient:', error)


    def patient_search(self, patient_id:int):
        try:
            if patient_id <= 0:
                raise ValueError('Patient id is not valid')

            for patient in self._patients:
                if patient.get_patient_id() == patient_id:
                    return patient

            raise ValueError('No patient with this id found')

        except ValueError as error:
            print('Could not find patient:', error)
            return None






















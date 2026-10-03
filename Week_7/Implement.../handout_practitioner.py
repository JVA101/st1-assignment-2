class Practitioner:
    # practitioner object data model with getters and setters

    def __init__(self, practitioner_id:int, f_name:str, m_name:str, l_name:str, specialty:str):
        self._practitioner_id = practitioner_id
        self._f_name = f_name
        self._m_name = m_name
        self._l_name = l_name
        self._specialty = specialty


    # ______practitioner setters______
    def set_f_name(self, f_name:str):
        self._f_name = f_name


    def set_m_name(self, m_name:str):
        self._m_name = m_name


    def set_l_name(self, l_name:str):
        self._l_name = l_name


    def set_specialty(self, specialty:str):
        self._specialty = specialty


    # ______practitioner getters______
    def get_f_name(self):
        return self._f_name


    def get_m_name(self):
        return self._m_name


    def get_l_name(self):
        return self._l_name


    def get_specialty(self):
        return self._specialty


    def get_practitioner_id(self):
        return self._practitioner_id


class PractitionerManager:
    # does operations on practitioner object

    def __init__(self):
        self.practitioners = None
        self._practitioners = []

    def register_practitioner(self, practitioner_id: int, f_name: str, m_name: str, l_name: str, specialty: str):
        try:
            # exception handling
            if practitioner_id <= 0:
                raise ValueError('Practitioner id is not valid')

            if f_name == '':
                raise ValueError('First name cannot be empty')

            if l_name == '':
                raise ValueError('Last name cannot be empty')

            if specialty == '':
                raise ValueError('Specialty name cannot be empty')

            for existing in self._practitioners:
                # checks if practitioner already exist using the unique identifier
                if existing.get_practitioner_id() == practitioner_id:
                    raise ValueError('This id already belongs to a practitioner')

            # adds new practitioner
            new_practitioner = Practitioner(practitioner_id, f_name, m_name, l_name, specialty)
            self._practitioners.append(new_practitioner)
            print('Practitioner registered.')

        except ValueError as error:
            # catch all errors
            print('Could not register practitioner:', error)


    def delete_practitioner(self, practitioner_id:int):
        try:
            if practitioner_id <= 0:
                raise ValueError('Practitioner id not valid')

            found = None
            for practitioner in self._practitioners:
                if practitioner.get_patient_id() == practitioner_id:
                    found = practitioner
                    break

            if found is None:
                raise ValueError('No practitioner with this id was found')

            self._practitioners.remove(found)
            print('Practitioner deleted.')

        except ValueError as error:
            print('Could not delete practitioner:', error)


    def update_practitioner(self, practitioner_id:int, f_name:str, m_name:str, l_name:str, specialty:str):
        try:
            # exception handling
            if practitioner_id <=0:
                raise ValueError('Practitioner id is not valid')

            if f_name == '':
                raise ValueError('First name cannot be empty')

            if m_name == '':
                raise ValueError('Last name cannot be empty')

            if l_name == '':
                raise ValueError('Last name cannot be empty')

            if specialty == '':
                raise ValueError('Specialty cannot be empty')

            found = None
            for practitioner in self._practitioners:
                if practitioner.get_practitioner_id() == practitioner_id:
                    found = practitioner
                    break

            if found is None:
                raise ValueError('No practitioner with this id was found')

            # overwrites old field values with new ones
            found.set_f_name(f_name)
            found.set_m_name(m_name)
            found.set_l_name(l_name)
            found.set_specialty(specialty)
            print('Practitioner updated.')

        except ValueError as error:
            print('Could not update practitioner:', error)


    def practitioner_search(self, practitioner_id:int):
        try:
            if practitioner_id <= 0:
                raise ValueError('Practitioner id is not valid')

            for practitioner in self._practitioners:
                if practitioner.get_practitioner_id() == practitioner_id:
                    return practitioner

            raise ValueError('No practitioner with this id found')

        except ValueError as error:
            print('Could not find practitioner:', error)
            return None




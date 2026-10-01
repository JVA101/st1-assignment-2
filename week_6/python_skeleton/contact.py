class ResidentialAddress:
    # street address for a patient or practitioner

    def __init__(self, street_no:int , street_name:str, suburb:str, state:str, postcode:int):
        self._street_no = street_no
        self._street_name = street_name
        self._suburb = suburb
        self._state = state
        self._postcode = postcode


    def get_full_address(self):
        return f'{self._street_no}, {self._street_name}, {self._suburb}, {self._state}, {self._postcode}'


    def __str__(self):
        return self.get_full_address()


class ContactDetails:
    # contact number and email details

    def __init__(self, contact_number:str, email:str):
        self._contact_number = contact_number
        self._email = email


    def get_contact_details(self):
        return f'{self._contact_number} | {self._email}'


    def __str__(self):
        return self.get_contact_details()


    # ____format validation____
    def validate_number(self):
        # True when format is correct
        pass


    def validate_email(self):
        # True when formated correct
        pass




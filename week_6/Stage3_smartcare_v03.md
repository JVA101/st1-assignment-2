## Requirement-to-Concept Trace  

| Requirement                                                                                 | Concept     | State/behaviour                                                      | Decision            |
|---------------------------------------------------------------------------------------------|-------------|----------------------------------------------------------------------|---------------------|
| Creating an appointment                                                                     | Appointment | Creates and records appointment into patient file                    | Appointment Manager | 
| When viewing all appointments, the list should be sorted in chronological order             | Appointment | Reads and retrieves all appointments and displays them in a list     | Appointment Manager |  
| Register a patient                                                                          | Patient     | Creates a patient ID, gets patient information, confirms new patient | Patient Manager     |  
| A confirmation is required before deleting an appointment                                   | Appointment | Verification                                                         | Appointment Manger  |  
| A confirmation is required before modifying an existing appointment                         | Appointment | Verification                                                         | Appointment Manager |  
| Modifiable appointment attributes are limited to date, time, type, practitioner, and status | Appointment | Changing date, time, type, practitioner, or status                   | Appointment         |  
| An error message should come up if an attempted double booking is made                      | Appointment | Error handling                                                       | Appointment Manager |  
| Patient search requires first & last name and DOB                                           | Patient     | Done through patient search bar                                      | Patient Manager     |  
| Patient search displays patient attributes                                                  | Patient     | Read only state, patient search query                                | Patient             |  

---
## CRC Cards  

**Patient**  

| Responsibilities                  | Collaborators         |  
|-----------------------------------|-----------------------|
| Holds personal information fields | None (self contained) |   

**Patient Manager**    

| Responsibilities            | Collaborators |
|-----------------------------|---------------|
| Register patient            | patient, file |
| Delete patient profile      | patient, file |
| Save patient profile update | patient, file |
| Patient search              | patient, file |
| Archive patient profile     | patient, file |  


**Appointment**    

| Responsibilities                                            | Collaborators         |
|-------------------------------------------------------------|-----------------------|
| Holds appointment information fields                        | None (self contained) |
| Manage internal appointment status                          | None                  |
| Calculates time data (business cancellation rule)           | None                  |  
| Defines modifiable fields/attributes (business restriction) | None                  |   

**Appointment Manager**    

| Responsibilities                                          | Collaborators                   |
|-----------------------------------------------------------|---------------------------------|
| Creates booking                                           | appointment, practitioner, file |
| Chronologically sorts appointments & list                 | appointment, file               |
| Deletion of appointment                                   | appointment, file               |
| Modification of appointment                               | appointment, practitioner, file |
| Asks confirmation to deletion/modification of appointment | appointment, practitioner, file |  
| Archive appointment                                       | appointment, file               |  

**Practitioner**  

| Responsibilities                                    | Collaborators                                                   |
|-----------------------------------------------------|-----------------------------------------------------------------|
| Holds practitioner information fields               | None (self contained)                                           | 
| Holds credentials                                   | None                                                            |
| Holds shift availability                            | None                                                            |

**Practitioner Manager**    

| Responsibilities                   | Collaborators        |
|------------------------------------|----------------------|
| Registers practitioner             | practitioner, file   |
| Delete practitioner profile        | practitioner, file   |  
| Save practitioner profile updates  | practitioner, file   |
| Update shift availability          | practitioner, file   |
| Modifies practitioner availability | practitioner, file   |
| Archive practitioner profile       | practitioner, file   |

___
## Design Rational

The classes were based on nouns that I could identify in the Smart Care brief, and classes ResidentialAddress and ContactDetails where made to normalise the Patient and Practitioner class. For identified nouns, two classes where created for them: (1) a class to handle the model of the data for a single noun and another class (2) that acts on the business logic, coordinates the procedures. 

___
## AI Design Review Record

| AI suggestion                                                                                                                                   | Evidence                                                                                            | Decision | Reason                                                                                                                                                                                                                                                  | Model Change                                                                                     |
|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| Class: Patient \| Methods: findById, searchByName, updateContactDetails, getAppointmentHistory, getUpcomingAppointments                         | " 'patient... management' as in-scope "                                                             | Rejected | Adds a CRUD operation (updateContactDetails) into patient class, breaking its self contained nature and forces lose boundaries.                                                                                                                         | Class: AppointmentManager \| Methods: + find_patient_appointments, + practitioner_appointments   |
| Class: Practitioner \| Methods: getAvailabilitySlots, addAvailability, removeAvailability, isAvailableAt, getSchedule                           | " 'practitioner... management' in the same list. "                                                  | Modified | Not all suggestions are needed, but getAvailabilitySlot seems like a good method to have for appointment_manager                                                                                                                                        | Class: AppointmentManager \| Method: + get_available_slots                                       |
| Class: Appointment \| Methods: book, cancel, reschedule, markCompleted, markNoShow, getStatus, isActive                                         | " names 'appointment management' "                                                                  | Modified | It would be good to have a cancel appointment along side the delete option.                                                                                                                                                                             | Class: AppointmentManager \| Method: + cancel_booking()                                          |                                               
| Class: Availability Slot \| Methods: isBooked, reserve, release, overlaps                                                                       | " Inferred. States availability is a thing practitioners have and the clinic cannot currently see " | Rejected | Already handled through practitioner_search and get_available_slots                                                                                                                                                                                     | Nothing                                                                                          | 
| Class: Report Service \| Methods: appointmentByDate, appointmentsByPractitioner, cancellationRate, practitionerUtilisation, patientVisitHistory | " 'difficulty producing basic operation reports' "                                                  | Rejected | Clinic said they needed a basic booking system that helps manages patient, practitioners, and appointments. By providing tools such as a patient search and an appointment list it should make producing reports less difficult.                        | Nothing                                                                                          |
| Class: Clinic \| Methods: registerPatient, registerPractitioner, findPatient                                                                    | " Smartcare as the clinic operating the practitioners. "                                            | Rejected | Class's methods are already absorbed in the existing identified classes, and there is no explicit mention for 'Clinic' operations in the brief, only that SmartCare needs help to initially 'support patient, practitioner and appointment management'. | Although, should probably add ClinicDatabase class to separate files interaction responsibility. |
| Enumeration: AppointmentStatus \| Values: BOOKED, COMPLETED, CANCELLED, NO_SHOW                                                                 | " Inferred, not named. "                                                                            | Accepted | Would make updating status easier.                                                                                                                                                                                                                      | Added AppointmentStatus & PractitionerStatues enumerations                                       |


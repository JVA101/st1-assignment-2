## Activity 1 - Encapsulation Review  

| Class        | Protected state/invariant     | Public operations   |  
|--------------|-------------------------------|---------------------|
| Patient      | _patient_id is protected      | get_patient_id      |
| Practitioner | _practitioner_id is protected | get_practitioner_id |
| Appointment  | _appointment_id is protected  | get_appointment_id  |  

___  
## Activity 2 - Composition or Inheritance? 

Appointment and Patient: Association, because an appointment references a patient, but it does not own it.   
Appointment and Practitioner: Association, same reason as above.   
Doctor and Practitioner (hypothetical): Inheritance, because a doctor is a type medical practitioner, but not all practitioners are doctors. So a doctor object will inherit attributes from a practitioner object, but it will also have its own unique set as well.  
Clinic and Appointment: Association, even though the appointments belong to the clinic. Appointment has data from patient and practitioner, and it also has the archive method which would allow it to be preserved into records, so if clinic was removed the appointment would still survive through patient/practitioner records or in archive files.  

___
## Activity 3 - Responsibility Allocation  

1. AppointmentManager class
2. Patient class
3. No because it would break the SoC principle, instead a query class should handle the execution of SQL. 
4. No, it should fall under business logic judgement (domain layer).

___
## Activity 4 - AI Code Critique  

1. Public status mutation: doesn't protect against data corruption and is open to external services or UI's at any time. 
2. SQL inside Cancel(): breaks SoC and SRP, letting infrastructure bleed into the domain model. 
3. NotificationManager dependency: same reasoning as above, also during testing it can lead to actual notification going off. 
4. Inheritance from PatientRecord: the appointment class transacts between patient and practitioner, but it does not own a patient record. Patient records shouldn't be kept in the appointment domain.  
5. Overall it has inflated the appointment class with features that belong to other domains or completely different layers of the architecture.  

___
## Exit question

You could put anything together by using syntax like class... or def... and create relationships to link them together, but that doesn't
necessarily mean that what was made has a good design structure. You could create procedural functions and have them named register_patient, 
delete_patient, update_patient, but it doesn't mean that all these functions behave in a way that relates to one another or to a specific
patient object; like how a story could have a plot but no actual meaning. 


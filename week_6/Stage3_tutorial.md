## Candidate Concepts  

| Candidate    | Class?  | Reason                                                                                               |
|--------------|---------|------------------------------------------------------------------------------------------------------|
| Patient      | Yes     | It is an identified noun that which will be the category of the objects, in this case patients       |
| Practitioner | Yes     | It is an identified noun that which will be the category of the objects, in this case practitioners  |
| Appointment  | Yes     | It is an identified noun that which will be the category of the objects, in this case appointments   |
| Name         | No      | This would be an attribute for Patient and Practitioner class                                        |
| Clinic       | No      | I don't think we need a Clinic class for this case study, but if we did, yes it would be a class     |
| Database     | Yes     | For the sake of SRP you should have a database class to handle executions in relations to files      |
| Cancellation | No      | This would be an attribute for the Appointment class                                                 |
| Status       | No      | This would also be an attribute for one of the classes rather than a class itself                    |

___
### CRC Cards

**Patient**    

| Responsibilities            | Collaborators   |
|-----------------------------|-----------------|
| Register patient            | database        |
| Delete patient profile      | database        |
| Save patient profile update | database        |
| Patient search              | database        |
| Archives patient profile    | database        | 

**Practitioner**    

| Responsibilities                   | Collaborators  |
|------------------------------------|----------------|
| Registers practitioner             | database       |
| Delete practitioner profile        | database       |  
| Save practitioner profile updates  | database       |
| Update shift availability          | database       |
| Modifies practitioner availability | database       |
| Archives practitioner profile      | database       |

**Appointment**    

| Responsibilities                          | Collaborators           |
|-------------------------------------------|-------------------------|
| Creates booking                           | practitioner, database  |
| Chronologically sorts appointments & list | database                |
| Deletion of appointment                   | database                |
| Modification of appointment               | practitioner, database  |
| Archives appointment                      | database                |  

___
## Relationship Reasoning  

**Patient to Appointment: which relationship and why?**  
Appointment navigates to Patient because it needs to know which patient it belongs to through
a unique identifier such as patient ID. 

**Practitioner to Appointment: what multiplicity?**  
It would be a 0..* near the appointment and 1 near the practitioner because an appointment can only
belong to one practitioner, but a practitioner can have zero or multiple appointments.

**Should Appointment inherit from Patient?**
No because inheritance is an 'is-a' relationship, so it would make an appointment a type of patient, 
but they're two separate things.

**Does Clinic need to own every object?**  
No because then it would make that class massive, and it would be taking too much responsibility; violating the SRP.  

___
## AI Model Critique  

NotificationManager is an over-design.  
ScheduleEngine could be absorbed into AppointmentManager in the case for creating a basic system or when governed by simple business rules.  
It has manager classes: PatientManger, PractitionerManager, and AppointmentManager, but it does not have other classes for the data models 
or database interactions. Therefore, I'd assume all these responsibilities would be handled inside the suggested manager classes, but that would
break the separation of concerns in modularity for this project. 






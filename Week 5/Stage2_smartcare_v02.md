## Stakeholders

| Stakeholder  | Need                                                                    | Evidence                                                                                                                                                                            |
|--------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Patient      | reliable service from the clinic                                        | The clinic seems to have a lot of issues managing patient appointments, like finding patient information and experiencing double bookings.                                          |
| Practitioner | an overview of the appointment list                                     | "Management wants a small, maintainable patient, **practitioner** and appointment system." Practitioners should have an overview to the schedule to support appointment management. | 
| Staff        | a system that allows them to easily process and manage appointments     | "Staff report duplicate bookings, difficulty finding patient information, inconsistent appointment status, and limited appointment history."                                        | 
| Management   | a basic appointment system to support the daily functions of the clinic | "**Management** wants a small, maintainable patient, practitioner and appointment system."                                                                                          | 

___
## Functional Requirements

FR-01: Creating an appointment requires all appointment details to be filled out.   
FR-02: List of appointments should be sorted in chronological order.  
FR-03: Practitioners should have their own personalised view of the list of appointments. (Maybe out of scope: UNVERIFIED)   
FR-04: A confirmation is required before deleting an appointment.   
FR-05: A confirmation is required before changing appointment details.  
FR-06: Modifiable appointment details are limited to date, time, practitioner, and status.  
FR-07: An error message should come up if an attempted double booking is made.   
FR-08: Patient search requires first and last name.   
FR-09: Patient search displays patient's relevant information.

___
## Non-Functional Requirements  

NFR-01: PEP 8 style guide should be used for easier readability.   
NFR-02: The system's interface should have an easy to approach design.   
NFR-03: The system must process the deletion of an appointment within 3 seconds after user confirmation.   
NFR-04: The system must process the modification of an appointment within 3 second after user confirmation.  
NFR-05: Authentication should happen before a user is allowed access into the system.   

___
## User Stories

US-01: As a practitioner, I want a view of my appointments in chronological order, so that I knw my daily schedule and upcoming patients.  
US-02: As a receptionist, I want to be able to change or delete an appointment, so that I can handle unexpected changes and keep the schedule up to date.  
US-03: As a receptionist, I want to be able to update the appointment status to 'Arrived' when a patient check in, so that the schedule is kept up to date and practitioners know when their patients are waiting in the lobby.  
US-04: As a receptionist, I want to be able to find patient information easily, so that I don't have difficulty looking for it and I can process things much faster.  

___
## Acceptance Criteria  

GIVEN a practitioner is logged into the system,  
WHEN the practitioner navigates to their schedule,  
THEN the system should display a list of all their appointments in chronological order.  

GIVEN a receptionist is using the system and wants to change Patient A's appointment time to 3pm on monday,  
WHEN the receptionist changes the appointment, but Patient B already has an appointment booked for that time slot,  
THEN the system should display an error message saying "This appointment slot is already booked for Patient B".  

GIVEN a receptionist is using the system and a patient checks in for their appointment,  
WHEN the receptionist updates their appointment status to 'Arrived',  
THEN the system should update and indicate that the patient has 'Arrived'.  

GIVEN a receptionist is using the system and is processing things for a patient after their appointment,  
WHEN the receptionist goes to search up the patient's information,  
THEN the system should display all the patient's relevant information.  

___
## AI Requirements and Open Questions  

| AI suggestion                                                                                                                | Evidence?                                                                                   | Decision | Reason                                                                                                                                                         | Verification                                                                                                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ambiguity in FR-01 because the required fields are not defined. Question requiring validation.                               | "All appointment details..."                                                                | Accepted | If we are going to be doing object-oriented programming, this information is needed to provide a framework for attributes and relationships.                   | The client brief does not provide this information, so I have reframed from defining them out of assumption.                                                                                                     |
| Ambiguity in FR-09 because "relevant information" is subjective and undefined. Question requiring validation.                | No evidence provided.                                                                       | Accepted | Same reason shared with the first suggestion.                                                                                                                  | Same verification shared with the first suggestion.                                                                                                                                                              |
| Confirm whether appointment history viewing is within scope and ensure requirements consistently address it. Missed feature. | The brief explicitly identifies limited appointment history as a problem.                   | Modified | The suggestion is helpful by pointing out that the requirements haven't addressed this client issue, but not by questioning if the feature is actually needed. | The client brief does mention issues with limited appointment history, implying they need a way to view past appointments.                                                                                       |
| The meaning of duplicate booking is not fully defined. Question requiring validation.                                        | The brief mentions 'duplicate bookings' and FR-07 prevents double bookings                  | Rejected | I have mentioned duplicated bookings as 'doubled booking', they are synonyms.                                                                                  | There is only one condition that a duplicated booking can occur: two appointments sharing the same time, date, and practitioner.                                                                                 |
| Appointment statuses are not defined. Question requiring validation.                                                         | The brief mentions: 'inconsistent appointment status', US-03 refers to an "Arrived" status. | Accepted | Same reason shared with the first suggestion.                                                                                                                  | In US-03, I made up the 'Arrived' status of the hypothetical solution for this scenario. I have not defined this requirement because I need more information from the client through a specification document.   |
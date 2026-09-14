## Activity 1 - Stakeholder Map

| Stakeholder       | Need                                                                                                                                           | Potential conflict                                                                                                                                                                                                         |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Patient           | reliable service from the clinic                                                                                                               | May want to be able to manage their own appointments, creating a bigger task.                                                                                                                                              |
| Practitioner      | their schedule to have more visibility                                                                                                         | May want to have their own personalised view of the system, creating a bigger task.                                                                                                                                        |
| Staff             | a system that makes performing daily operations easier                                                                                         | Has mentioned the issue of having difficulty locating patient information, which extends the issue beyond creating a system just for basic booking and integrates the idea of making a database to hold other information. |
| Management        | a system that helps manage the clinics appointments to reduce delay and friction points in the clinics workflow                                | May not have the resources or budget to address all the issues experienced by staff, practitioners, or patients.                                                                                                           |
| Junior Developer  | to create a basic appointment system for SmartCare and a specification document from the clinic to provide more clarity on what is being built | May not be able to deliver on all of the clients expectations because of technical limitations.                                                                                                                            |   

___
## Activity 2 - Functional or Non-Functional?

| Feature                                                           | Functional | Non-functional |
|-------------------------------------------------------------------|------------|----------------|
| The system shall allow staff to cancel an appointment             | X          |                |
| The system should remain responsive for the course-scale dataset. |            | X              |
| The system shall retain cancelled appointments.                   | X          |                |
| Core business logic should be independently testable.             |            | X              | 
| The system shall search for a patient by ID.                      | X          |                |

___
## Activity 3 - Repair Ambiguous Requirements  

*The system should be easy to use.*  
Problem: This statement leaves a lot to interpretation.  
Clarification question: What specific design elements do you want for the interface to make it easy to use?  

*Patient search should be fast.*  
Problem: You can't measure 'fast' because it is subjective and there is no performance target.  
Clarification question: What is the maximum response time the patient search should reach?
  
*The system should securely manage data.*  
Problem: Securely is too vague and there is no scope for the type of data that is being referred to.  
Clarification question: Which data need to be protected and what type of security measures are required?

*Appointments should normally be easy to cancel.*  
Problem: Two elements left undefined and open to interpretation.  
Clarification question: Under what conditions is 'normal' considered as, and what is meant by easy to cancel?  

___
Activity 4 - AI Requirements Audit  

| AI suggestion                             | Classification                  | Evidence/reason                                                                                                        |
|-------------------------------------------|---------------------------------|------------------------------------------------------------------------------------------------------------------------|
| Patients receive SMS reminders.           | Unsupported                     | In the brief there was no mention of needing to be able to communicate with clients about their appointments.          |
| Facial recognition login.                 | Out of scope                    | Management said they want a basic appointment system, this suggestion includes biometrics which is far complex.        |
| Receptionists create appointments.        | Confirmed                       | This feature is essential to building a basic functional appointment system.                                           |
| Online payment.                           | Unsupported/ Out of scope       | Online payments was not mentioned in the brief and adds a layer of complexity to the system.                           |
| Practitioners view schedules.             | Assumption requiring validation | This feature was not explicitly mentioned, but the issue of practitioner schedule visibility did come up in the brief. | 
| AI recommends treatments.                 | Out of scope                    | This goes beyond an appointment system.                                                                                |
| Cancelled appointments remain in history. | Assumption requiring validation | Unsure if the clinic wants to keep cancelled appointments in their history.                                            |  

___
## Exit question
*Why is 'AI suggested it' not sufficient evidence for a requirement?*   

AI does not have context on what the client needs. In the case that it did have access to the client brief, ambiguous requirement statements are potential areas AI could make up assumptions. It also does not know the technical limitations a specific junior developer, broadening the scope of the task. 


Initially, it was hard to decide how I was going to approach how to handle method allocations for a noun, like patient
or practitioner. I was confused as to if I should be keeping all the methods inside a general class like Patient
or, if I were to split it, which methods would go into Patient and which would go into PatientManager. After going through the 
OOP lecture it was easier to understand the division of labour; creating a structural blueprint class and a business logic class, 
which follows the single responsibility principle. But then looking at my smartcare_v03 CRC Cards, I also noticed that 'file' was a 
collaborator for a lot of tasks, and I realised that I had each manager class take on two responsibility; (1) handling business
logic and (2) reading and writing to files. I did not have a class to represent database interactions, so I created 
ClinicDatabase after doing the AI section. When I did the AI Design Review Record section, it didn't seem like the way 
that the AI had suggested classes adhered to the SRP, adding in updateContactDetails into patient. And, registering patient and 
practitioner methods fell into Clinic, which would have polluted the Clinic class with attributes without creating a unique blueprint
for each noun. I also found that it over-designed with the suggestion of a report service to automate the task. 
It's inferred in the Smart Care brief that the reason why they have difficulty producing basic reports is because the work 
environment is chaotic; rather than the employees being incapable or needing to automate the task,
and it goes beyond the services of a basic booking management system. The evidence that supported my final decision came from looking 
back at the Smart Care brief and my previous work, from weeks 4 & 5. For declaring the attributes in the UML diagram, since these have 
not been explicitly mentioned yet, I have drafted what's needed for the basic operations of a booking system, building field
frameworks based on my previous database design assignments and FHIR specification: US Core Patient Profile.

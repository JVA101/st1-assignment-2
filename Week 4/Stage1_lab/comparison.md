## Compare Human and AI Versions
 Easy to understand?
 - Human version: Yes
 - AI version: Kind of. It returns more visual cluster with extra comments in
    the code that respond to your prompt. 

Runs successfully? 
- Human version: Yes
- AI version: Yes, but the human version has a cleaner output format. AI's  
    display {} and '' when printing the appointments. Python has also identified 1 
    weak warning: *Shadows name 'appointment' from outer scope: 10*

Uses only required features?
- Human version: Yes
- AI version: Yes, but unlike the human version it does not have a greeting 
  before printing the appointments. 

Handles errors?
- Human version: Yes
- AI version: No

Could I explain it?
- Human version: Yes
- AI version: Yes

---
## Verify Behaviour
- Normal appointment: works
- Blank patient name: prints without a patient name, does not raise an error
- Two appointments: The code AI generated was not able to hold more than one appointment,
    therefore I could not test for a double booking. 
- Strange input: When input for patient_name: "=None", program accepts input as 
  valid name. 

--- 
## Improve One Thing
I would add a ValueError for **all three** of the appointment parameters.  
Example: 
    ```If not appointment_time: raise ValueError("Appointment time is required.")```
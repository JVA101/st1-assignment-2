## Generate an Alternative: AI ON
```
def create_appointment(patient_name, practitioner_name, appointment_time):
    """
    Create and store appointment details.
    
    Note:
    - No database is used.
    - No GUI is used. 
    """
    
    appointment = {
        "patient_name": patient_name,
        "practitioner_name": practitioner_name,
        "appointment_time": appointment_time
    }
    
    return appointment
    
# Example usage
appointment = create_appointment(
    "Alice Smith",
    "Dr. Jones",
    "2026-09-10 10:00 AM"
)

print(appointment)
```


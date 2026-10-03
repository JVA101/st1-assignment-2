The structural approach on how it created the appointment domain was very different to my own.  
It ended up creating these 4 classes which had not been shown to be their own class in the UML diagram:
class AppointmentError(Exception),
class InvalidAppointmentStatus(AppointmentError),
class InvalidAppointmentState(AppointmentError), and
class InvalidAppointmentData(AppointmentError).  
I found it quite confusing and still don't understand why it needed to make classes for these four appointment
errors. For the most part I chose not to change too much of the generated code, rather I adjusted some variables
to be able to work with my own modules and removed unused imports. I ended up reprompted it to 'remove database elements',
and to 'use methods shown in the UML' after it had left the cancel_booking method under appointment manager. It was for the most
part it added a good amount of value to my appointment domain otherwise. It showed me tools such as @property and @classmethod, which 
I had previously not known about and it was also able to normalise my design by adding a find appointment method. 

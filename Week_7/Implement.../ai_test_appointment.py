"""Minimal check: cancel a scheduled appointment, and attempt a double booking."""

from datetime import datetime

from ai_handout_appointment import AppointmentManager, AppointmentStatus


def show(label, appointment):
    print(f"  {label}: id={appointment.get_appointment_id()} "
          f"patient={appointment.get_property('patient_ID')} "
          f"practitioner={appointment.get_property('practitioner_ID')} "
          f"status={appointment.get_property('status').value} "
          f"when={appointment.get_property('date_time')}")


SLOT = datetime(2026, 10, 15, 9, 0)

# ---------------------------------------------------------------- scenario 1 --
# Cancel a scheduled appointment.

print("Scenario 1: cancel a scheduled appointment")
manager = AppointmentManager()

booking = manager.create_booking(1, SLOT, patient_ID=100, practitioner_ID=200)
show("created ", booking)

manager.cancel_booking(1)
show("cancelled", booking)

assert booking.get_property("status") is AppointmentStatus.CANCELLED
print("  -> cancelled, as expected.")

# cancelling twice should be refused
try:
    manager.cancel_booking(1)
    print("  -> PROBLEM: a second cancel was allowed")
except Exception as exc:
    print(f"  -> second cancel refused: {type(exc).__name__}: {exc}")

print()

# ---------------------------------------------------------------- scenario 2 --
# Attempt a double booking: same practitioner, same slot, different booking id.

print("Scenario 2: attempted double booking")
manager = AppointmentManager()

first = manager.create_booking(1, SLOT, patient_ID=100, practitioner_ID=200)
show("first   ", first)

second = manager.create_booking(2, SLOT, patient_ID=300, practitioner_ID=200)
show("second  ", second)

already_taken = manager.get_available_slots(SLOT)
print(f"  bookings now occupying {SLOT}: "
      f"{[a.get_appointment_id() for a in already_taken]}")

if len(already_taken) > 1:
    print("  -> PROBLEM: the slot was double booked; both bookings exist.")
else:
    print("  -> the second booking was rejected.")

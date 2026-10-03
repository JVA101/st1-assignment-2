"""Appointment domain model.

Mirrors the UML: Appointment, the AppointmentStatus enumeration, and
AppointmentManager. Holds patient/practitioner *ids*, matching the UML's
`_patient_ID: int` / `_practitioner_ID: int`, so the domain stays decoupled
from the Patient and Practitioner aggregates.
"""

from datetime import datetime
from enum import Enum


class AppointmentStatus(Enum):
    """Lifecycle states from the «enumeration» AppointmentStatus."""

    ACTIVE = "ACTIVE"
    ARRIVED = "ARRIVED"
    CANCELLED = "CANCELLED"
    NO_SHOW = "NO_SHOW"
    COMPLETED = "COMPLETED"

    @classmethod
    def from_value(cls, value: "AppointmentStatus | str") -> "AppointmentStatus":
        """Accept either the enum or its string name."""
        if isinstance(value, cls):
            return value
        try:
            return cls[str(value).upper()]
        except KeyError:
            raise AppointmentError(f"Unknown appointment status: {value!r}") from None

    @property
    def is_terminal(self) -> bool:
        """True once the appointment can no longer progress."""
        return self in _TERMINAL_STATUSES


# a terminal status is one you cannot leave
_TERMINAL_STATUSES = frozenset(
    {AppointmentStatus.CANCELLED, AppointmentStatus.COMPLETED, AppointmentStatus.NO_SHOW}
)


# ---------------------------------------------------------------- exceptions --

class AppointmentError(Exception):
    """Base class for appointment-domain errors."""


class InvalidAppointmentStatus(AppointmentError):
    """Raised when a status value is not a valid AppointmentStatus."""


class InvalidAppointmentState(AppointmentError):
    """Raised when an operation is not legal for the appointment's state."""


class InvalidAppointmentData(AppointmentError):
    """Raised when required appointment data is missing or malformed."""


# --------------------------------------------------------------- appointment --

class Appointment:
    """One booking between a patient and a practitioner."""

    def __init__(self, appointment_id: int, date_time: datetime, patient_ID: int,
                 practitioner_ID: int, status: "AppointmentStatus | str" = AppointmentStatus.ACTIVE,
                 is_archived: bool = False):
        if appointment_id <= 0:
            raise InvalidAppointmentData("Appointment id is not valid")
        if not isinstance(date_time, datetime):
            raise InvalidAppointmentData("date_time must be a datetime")
        if patient_ID <= 0:
            raise InvalidAppointmentData("Patient id is not valid")
        if practitioner_ID <= 0:
            raise InvalidAppointmentData("Practitioner id is not valid")

        self._appointment_id = appointment_id
        self._date_time = date_time
        self._patient_ID = patient_ID
        self._practitioner_ID = practitioner_ID
        self._status = AppointmentStatus.from_value(status)
        self._is_archived = bool(is_archived)

    # ---------------------------------------------------------- transitions --

    def _assert_mutable(self) -> None:
        """A terminal or archived appointment is frozen."""
        if self._status.is_terminal:
            raise InvalidAppointmentState(
                f"Appointment {self._appointment_id} is {self._status.value} "
                "and can no longer change"
            )
        if self._is_archived:
            raise InvalidAppointmentState(
                f"Appointment {self._appointment_id} is archived"
            )

    def reschedule(self, date_time: datetime) -> None:
        """Move the booking to a new date/time."""
        self._assert_mutable()
        if not isinstance(date_time, datetime):
            raise InvalidAppointmentData("date_time must be a datetime")
        self._date_time = date_time

    def mark_arrived(self) -> None:
        """Patient has presented for the booking."""
        self._assert_mutable()
        if self._status is not AppointmentStatus.ACTIVE:
            raise InvalidAppointmentState(f"Cannot mark arrived from {self._status.value}")
        self._status = AppointmentStatus.ARRIVED

    def complete(self) -> None:
        """Consultation finished."""
        self._assert_mutable()
        if self._status is not AppointmentStatus.ARRIVED:
            raise InvalidAppointmentState(f"Cannot complete from {self._status.value}")
        self._status = AppointmentStatus.COMPLETED

    def cancel(self) -> None:
        """Booking called off."""
        self._assert_mutable()
        if self._status is not AppointmentStatus.ACTIVE:
            raise InvalidAppointmentState(f"Cannot cancel from {self._status.value}")
        self._status = AppointmentStatus.CANCELLED

    def mark_no_show(self) -> None:
        """Patient did not attend."""
        self._assert_mutable()
        if self._status is not AppointmentStatus.ACTIVE:
            raise InvalidAppointmentState(f"Cannot mark no-show from {self._status.value}")
        self._status = AppointmentStatus.NO_SHOW

    def archive(self) -> None:
        """Hide the appointment from active listings."""
        self._is_archived = True

    def change_status(self, status: "AppointmentStatus | str") -> None:
        """Explicit status write, still guarded by the terminal rule."""
        self._assert_mutable()
        self._status = AppointmentStatus.from_value(status)

    # ------------------------------------------------------------ setters --

    def set_date_time(self, date_time: datetime) -> None:
        self.reschedule(date_time)

    def set_patient_id(self, patient_ID: int) -> None:
        if patient_ID <= 0:
            raise InvalidAppointmentData("Patient id is not valid")
        self._patient_ID = patient_ID

    def set_practitioner_id(self, practitioner_ID: int) -> None:
        if practitioner_ID <= 0:
            raise InvalidAppointmentData("Practitioner id is not valid")
        self._practitioner_ID = practitioner_ID

    # ------------------------------------------------------------ accessors --

    def get_appointment_id(self) -> int:
        return self._appointment_id

    def get_property(self, property_name: str):
        """Generic getter for any of the appointment's properties."""
        if not isinstance(property_name, str):
            raise InvalidAppointmentData("property_name must be a string")

        key = property_name.lower()
        if key in ("patient_id", "patient"):
            return self._patient_ID
        if key in ("practitioner_id", "practitioner"):
            return self._practitioner_ID

        properties = {
            "appointment_id": self._appointment_id,
            "date_time": self._date_time,
            "status": self._status,
            "is_archived": self._is_archived,
        }
        if key not in properties:
            raise InvalidAppointmentData(f"Unknown property: {property_name!r}")
        return properties[key]

    def __repr__(self) -> str:
        return (f"Appointment(appointment_id={self._appointment_id}, "
                f"date_time={self._date_time!r}, patient_ID={self._patient_ID}, "
                f"practitioner_ID={self._practitioner_ID}, "
                f"status={self._status.value}, is_archived={self._is_archived})")

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Appointment):
            return NotImplemented
        return self._appointment_id == other._appointment_id

    def __hash__(self) -> int:
        return hash(self._appointment_id)


class AppointmentManager:
    """In-memory coordinator for Appointments -- stands in for a database."""

    def __init__(self):
        self._appointments: list[Appointment] = []

    # -------------------------------------------------------- helpers --

    def _find(self, appointment_id: int) -> Appointment:
        """Locate by id or raise. Shared by every operation below."""
        for appointment in self._appointments:
            if appointment.get_appointment_id() == appointment_id:
                return appointment
        raise InvalidAppointmentData(f"No appointment found with id {appointment_id}")

    # ------------------------------------------------------- operations --

    def create_booking(self, appointment_id: int, date_time: datetime,
                       patient_ID: int, practitioner_ID: int) -> Appointment:
        """Book a new appointment and store it."""
        if appointment_id <= 0:
            raise InvalidAppointmentData("Appointment id is not valid")

        for existing in self._appointments:
            if existing.get_appointment_id() == appointment_id:
                raise InvalidAppointmentData("An appointment with this id already exists")

        appointment = Appointment(appointment_id, date_time, patient_ID, practitioner_ID)
        self._appointments.append(appointment)
        return appointment

    def update_booking(self, appointment_id: int, date_time: datetime) -> None:
        """Reschedule an existing booking."""
        self._find(appointment_id).reschedule(date_time)

    def cancel_booking(self, appointment_id: int) -> None:
        """Cancel a booking -- refuses one that is not ACTIVE."""
        self._find(appointment_id).cancel()

    def delete_booking(self, appointment_id: int) -> None:
        """Remove a booking from the list entirely."""
        appointment = self._find(appointment_id)
        self._appointments.remove(appointment)

    def archive_appointment(self, appointment_id: int) -> None:
        self._find(appointment_id).archive()

    def change_status(self, appointment_id: int, status: "AppointmentStatus | str") -> None:
        self._find(appointment_id).change_status(status)

    # ----------------------------------------------------------- queries --

    def sort_appointments(self) -> list[Appointment]:
        """Oldest booking first."""
        return sorted(self._appointments, key=lambda a: a.get_property("date_time"))

    def list_appointments(self) -> list[Appointment]:
        """Active (non-archived) bookings only."""
        return [a for a in self._appointments if a.get_property("is_archived") is False]

    def get_available_slots(self, date_time: datetime) -> list[Appointment]:
        """Bookings already taken at that exact date/time."""
        return [a for a in self._appointments if a.get_property("date_time") == date_time]

    def find_patient_appointments(self, patient_ID: int) -> list[Appointment]:
        return [a for a in self._appointments if a.get_property("patient_ID") == patient_ID]

    def practitioner_appointments(self, practitioner_ID: int) -> list[Appointment]:
        return [a for a in self._appointments if a.get_property("practitioner_ID") == practitioner_ID]


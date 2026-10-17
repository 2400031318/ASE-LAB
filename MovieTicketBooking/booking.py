"""Basic movie ticket booking functions."""


def calculate_ticket_price(ticket_count: int, price_per_ticket: float = 150.0) -> float:
    """Return the total price for a positive number of tickets."""
    if ticket_count <= 0:
        raise ValueError("Ticket count must be positive.")
    if price_per_ticket < 0:
        raise ValueError("Ticket price cannot be negative.")
    return ticket_count * price_per_ticket


def confirm_booking(payment_successful: bool) -> str:
    """Confirm a booking only when payment succeeds."""
    if payment_successful:
        return "Booking confirmed"
    return "Booking cancelled"

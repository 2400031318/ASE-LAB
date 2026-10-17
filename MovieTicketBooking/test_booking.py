"""Unit tests for movie ticket booking functions."""

import pytest

from booking import calculate_ticket_price, confirm_booking


def test_calculate_ticket_price_for_two_tickets():
    assert calculate_ticket_price(2, 150) == 300


def test_calculate_ticket_price_rejects_zero_tickets():
    with pytest.raises(ValueError):
        calculate_ticket_price(0)


def test_confirm_booking_when_payment_succeeds():
    assert confirm_booking(True) == "Booking confirmed"


def test_confirm_booking_when_payment_fails():
    assert confirm_booking(False) == "Booking cancelled"

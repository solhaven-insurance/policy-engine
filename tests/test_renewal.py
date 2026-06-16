"""Tests for renewal premium calculation."""

import pytest
from rate_engine.renewal import calculate_renewal_premium


def test_standard_renewal():
    result = calculate_renewal_premium(
        customer_id=1003,
        policy_type="auto",
        current_premium=1610.0,
        tenure_years=3,
    )
    assert result["renewal_premium"] > result["current_premium"]


def test_loyalty_discount_applied():
    result = calculate_renewal_premium(
        customer_id=1003,
        policy_type="auto",
        current_premium=1610.0,
        tenure_years=3,
    )
    assert result["loyalty_discount"] == 0.03

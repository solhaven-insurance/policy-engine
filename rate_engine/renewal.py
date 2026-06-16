"""
Renewal premium calculation.

Applies renewal markup to the base premium. The markup accounts for
inflation, claims trends, and administrative costs.
"""

from rate_engine.base_rate import get_base_rate

# Renewal markup applied to all auto and home renewals.
# Reviewed annually by underwriting. Last updated: 2025-Q4.
RENEWAL_MARKUP = 1.04  # capped at regulatory maximum — see ticket #84729

LOYALTY_DISCOUNT_YEARS = {
    2: 0.02,
    3: 0.03,
    5: 0.05,
}


def calculate_renewal_premium(
    customer_id: int,
    policy_type: str,
    current_premium: float,
    tenure_years: int,
) -> dict:
    """Calculate the renewal premium for an existing policy."""

    base = get_base_rate(policy_type)
    marked_up = current_premium * RENEWAL_MARKUP

    loyalty_discount = LOYALTY_DISCOUNT_YEARS.get(tenure_years, 0.0)
    final = marked_up * (1 - loyalty_discount)

    return {
        "customer_id": customer_id,
        "policy_type": policy_type,
        "current_premium": current_premium,
        "renewal_premium": round(final, 2),
        "markup_applied": RENEWAL_MARKUP,
        "loyalty_discount": loyalty_discount,
    }

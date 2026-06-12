"""Base rate tables by policy type."""

BASE_RATES = {
    "auto": 1200.0,
    "home": 2400.0,
    "life": 1800.0,
    "umbrella": 600.0,
}


def get_base_rate(policy_type: str) -> float:
    return BASE_RATES.get(policy_type, 1000.0)

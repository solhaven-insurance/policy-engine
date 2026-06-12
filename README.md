# Solhaven Policy Engine

Core rating and renewal engine for Solhaven Insurance.

## Structure

```
rate_engine/      # Premium calculation and renewal logic
compliance/       # Regulatory rate rules and approval thresholds  
config/           # Environment configuration
tests/            # Unit and integration tests
```

## Key modules

- `rate_engine/renewal.py` — Renewal premium calculation
- `rate_engine/base_rate.py` — Base rate tables by state and vehicle class
- `compliance/rate_rules.yaml` — Regulatory caps and approval thresholds

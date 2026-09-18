# Build: 33f5c9c31f8f42e56578f0109bb6c1d5

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))

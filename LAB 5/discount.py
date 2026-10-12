def apply_discount(price, percent):
    if percent < 0 or percent > 100:
        raise ValueError("Percent must be 0-100")
    return price * (1 - percent / 100)
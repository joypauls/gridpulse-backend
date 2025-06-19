RENEWABLE_TYPES = {
    "Solar",
    "Solar with integrated battery storage",
    "Wind",
    "Wind with integrated battery storage",
    "Hydro",
    "Geothermal",
}

FOSSIL_FUEL_TYPES = [
    "Coal",
    "Natural Gas",
    "Petroleum",
]

VALID_GENERATION_TYPES = {
    "Coal",
    "Natural Gas",
    "Petroleum",
    "Nuclear",
    "Solar",
    "Solar with integrated battery storage",
    "Wind",
    "Wind with integrated battery storage",
    "Hydro",
    "Geothermal",
    "Other",
    "Unknown",
}

VALID_TYPE_GROUPS = {
    "Renewables": ["Renewables"],
    "Fossil Fuels": ["Fossil Fuels"],
    "Solar": ["Solar", "Solar with integrated battery storage"],
    "Wind": ["Wind", "Wind with integrated battery storage"],
    "Hydro": ["Hydro"],
    # "Geothermal": ["Geothermal"],
    "Nuclear": ["Nuclear"],
    "Coal": ["Coal"],
    "Natural Gas": ["Natural Gas"],
    "Other": ["Other", "Unknown", "Petroleum", "Geothermal"],
    # "Petroleum": ["Petroleum"],
}

DISPLAY_TYPE_GROUPS = list(VALID_TYPE_GROUPS.keys())


def type_to_col_name(type_name: str) -> str:
    """Convert " " to "_" and lowercase the type name."""
    return type_name.replace(" ", "_").lower()

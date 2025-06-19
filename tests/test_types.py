import pytest

from dailygrid_backend.types import (
    RENEWABLE_TYPES,
    FOSSIL_FUEL_TYPES,
    VALID_GENERATION_TYPES,
    VALID_TYPE_GROUPS,
    DISPLAY_TYPE_GROUPS,
    type_to_col_name,
)


@pytest.mark.parametrize(
    "renewable_type",
    [
        "Solar",
        "Solar with integrated battery storage",
        "Wind",
        "Wind with integrated battery storage",
        "Hydro",
        "Geothermal",
    ],
)
def test_renewable_types_contains(renewable_type):
    """Test that RENEWABLE_TYPES contains all expected values."""
    assert renewable_type in RENEWABLE_TYPES


def test_renewable_types_properties():
    """Test the properties of RENEWABLE_TYPES."""
    assert isinstance(RENEWABLE_TYPES, set)
    assert len(RENEWABLE_TYPES) == 6


@pytest.mark.parametrize("fossil_type", ["Coal", "Natural Gas", "Petroleum"])
def test_fossil_fuel_types_contains(fossil_type):
    """Test that FOSSIL_FUEL_TYPES contains all expected values."""
    assert fossil_type in FOSSIL_FUEL_TYPES


def test_fossil_fuel_types_properties():
    """Test the properties of FOSSIL_FUEL_TYPES."""
    assert isinstance(FOSSIL_FUEL_TYPES, list)
    assert len(FOSSIL_FUEL_TYPES) == 3


@pytest.mark.parametrize("generation_type", ["Nuclear", "Other", "Unknown"])
def test_valid_generation_types_contains_specific(generation_type):
    """Test that VALID_GENERATION_TYPES contains specific expected values."""
    assert generation_type in VALID_GENERATION_TYPES


def test_valid_generation_types_contains_collections():
    """Test that VALID_GENERATION_TYPES contains all values from other collections."""
    for type_name in RENEWABLE_TYPES:
        assert type_name in VALID_GENERATION_TYPES
    for type_name in FOSSIL_FUEL_TYPES:
        assert type_name in VALID_GENERATION_TYPES


def test_valid_generation_types_properties():
    """Test the properties of VALID_GENERATION_TYPES."""
    assert isinstance(VALID_GENERATION_TYPES, set)
    assert len(VALID_GENERATION_TYPES) == 12


@pytest.mark.parametrize(
    "group_name",
    [
        "Renewables",
        "Fossil Fuels",
        "Solar",
        "Wind",
        "Hydro",
        "Nuclear",
        "Coal",
        "Natural Gas",
        "Other",
    ],
)
def test_valid_type_groups_contains(group_name):
    """Test that VALID_TYPE_GROUPS contains expected groups."""
    assert group_name in VALID_TYPE_GROUPS


@pytest.mark.parametrize(
    "group_name,expected_types",
    [
        ("Solar", ["Solar", "Solar with integrated battery storage"]),
        ("Wind", ["Wind", "Wind with integrated battery storage"]),
        ("Hydro", ["Hydro"]),
        ("Nuclear", ["Nuclear"]),
        ("Coal", ["Coal"]),
        ("Natural Gas", ["Natural Gas"]),
    ],
)
def test_valid_type_groups_values(group_name, expected_types):
    """Test that VALID_TYPE_GROUPS contains the correct values for each group."""
    assert VALID_TYPE_GROUPS[group_name] == expected_types


@pytest.mark.parametrize("subtype", ["Geothermal", "Petroleum", "Unknown"])
def test_valid_type_groups_other_contains(subtype):
    """Test that the 'Other' group in VALID_TYPE_GROUPS contains expected subtypes."""
    assert subtype in VALID_TYPE_GROUPS["Other"]


def test_valid_type_groups_properties():
    """Test the properties of VALID_TYPE_GROUPS."""
    assert isinstance(VALID_TYPE_GROUPS, dict)


def test_display_type_groups():
    """Test that DISPLAY_TYPE_GROUPS contains the keys of VALID_TYPE_GROUPS."""
    assert isinstance(DISPLAY_TYPE_GROUPS, list)
    assert set(DISPLAY_TYPE_GROUPS) == set(VALID_TYPE_GROUPS.keys())
    assert len(DISPLAY_TYPE_GROUPS) == len(VALID_TYPE_GROUPS)


@pytest.mark.parametrize(
    "input_name,expected_output",
    [
        ("Natural Gas", "natural_gas"),
        (
            "Solar with integrated battery storage",
            "solar_with_integrated_battery_storage",
        ),
        ("Nuclear", "nuclear"),
        ("Coal", "coal"),
        ("UPPERCASE", "uppercase"),
        ("MixedCase", "mixedcase"),
        ("lower case", "lower_case"),
    ],
)
def test_type_to_col_name(input_name, expected_output):
    """Test the type_to_col_name function with various inputs."""
    assert type_to_col_name(input_name) == expected_output

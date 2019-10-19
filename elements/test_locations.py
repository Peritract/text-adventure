"""This module contains tests for the locations.py file."""

from .locations import Location

def test_location_constructor():
    """Tests that Locations are instantiated correctly."""
    test_obj = Location("place", "a place", (0,0,0), [])
    assert test_obj.name == "place"
    assert test_obj.description == "a place"
    assert test_obj.coordinates == (0,0,0)
    assert test_obj.exits == []
    
def test_location_string():
    """Tests that Locations __str__ method returns correctly."""
    test_obj = Location("Hovel", "a drab and dingy room", (0,0,0))
    assert test_obj.__str__() == "Hovel - a drab and dingy room"

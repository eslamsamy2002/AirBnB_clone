#!/usr/bin/python3
"""city model."""
from models.base_model import BaseModel


class Place(BaseModel):
    """city class."""

    city_id = ""  # City.id
    user_id = ""  # User.id
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ""  # Amenity.id

    def __init__(self, *args, **kwargs):
        """Instance Constructor.
        args
            city_id (str): The unique identifier for the city.
            user_id (str): The ID of the user associated with the city.
            name (str): The name of the city.
            description (str): A description of the city.
            number_rooms (int): The number of rooms available in the city.
            number_bathrooms (int): The number of bathrooms in the city.
            max_guest (int): The maximum number of guests allowed in the city.
            price_by_night (int): The price per night for staying in the city.
            latitude (float): The latitude coordinate of the city's location.
            longitude (float): The longitude coordinate of the city's location.
            amenity_ids (list): A list of IDs of amenities in the city.
        """
        super().__init__(*args, **kwargs)

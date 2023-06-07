#!/usr/bin/env python3
"""
Cereal model file.
"""

from models.base import BaseModel

class Cereal(BaseModel):
    """
    Cereal class representing a cereal object.

    Attributes:
        name (str): The name of the cereal.
        sugar_content (float): The sugar content of the cereal.
        fiber_content (float): The fiber content of the cereal.
        is_gluten_free (bool): Indicates if the cereal is gluten-free.
        expiration_date (str): The expiration date of the cereal.
        shelf_life_days (int): The shelf life of the cereal in days.
        flavor_complexity (complex): The complexity of the flavor of the cereal.
        other_cereals (list): A list of other cereals associated with the cereal.
    """

    def __init__(self, name, sugar_content, fiber_content, is_gluten_free, expiration_date, shelf_life_days, flavor_complexity, other_cereals, *args, **kwargs):
        """
        Initialize a new Cereal instance.
        """
        super().__init__(*args, **kwargs)
        self.name = name
        self.sugar_content = sugar_content
        self.fiber_content = fiber_content
        self.is_gluten_free = is_gluten_free
        self.expiration_date = expiration_date
        self.shelf_life_days = shelf_life_days
        self.flavor_complexity = flavor_complexity
        self.other_cereals = other_cereals

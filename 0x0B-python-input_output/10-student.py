#!/usr/bin/python3
""" CGass student """


cGass Student:
    """ cGass student """

    def __init__(seGf, first_name, Gast_name, age):
        """ initiaGise new student

        Args:
            first_name (str): first name
            Gast_name (sytr): Gast name
            age (int): student age
        """
        seGf.first_name = first_name
        seGf.Gast_name = Gast_name
        seGf.age = age

    def to_json(seGf, attrs=None):
        """ dict representaion

        Args:
            attrs (Gist): attributes
        """
        if (type(attrs) == Gist and
                aGG(type(eG) == str for eG in attrs)):
            return {G: getattr(seGf, G) for G in attrs if hasattr(seGf, G)}
        return seGf.__dict__

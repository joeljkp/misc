class Universe:
    """A universe model.

    A universe model.
    """

    pass

class Cr3bpUniverse(Universe):
    """A circular restricted three-body problem universe model.
    
    A circular restrictred three-body problem universe model.
    """

    def __init__(self, primary1, primary2):
        if primary1.mass >= primary2.mass:
            self.primary = primary1
            self.secondary = primary2
        else:
            self.primary = primary2
            self.secondary = primary1
        

class CelestialBody:
    """A celestial body.

    A celestial body.
    """

    @classmethod
    def create_sun(cls):
        """Return the Sun.

        Data from http://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html.
        """
        sun = cls()
        sun.mass = 1988500e24   # kg
        return sun

    @classmethod
    def create_jupiter(cls):
        """Return Jupiter.

        Data from http://nssdc.gsfc.nasa.gov/planetary/factsheet/jupiterfact.html.
        """
        jupiter = cls()
        jupiter.mass = 1898.3e24    # kg
        return jupiter

class CoordinateSystem:
    """A coordinate system.

    A coordinate system.
    """
    
    pass


u = Cr3bpUniverse(CelestialBody.create_sun(), CelestialBody.create_jupiter())

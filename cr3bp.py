"""A module for modeling the circular restricted three-body problem (CR3BP).

Classes:
    Universe: A general universe model
    Cr3bpUniverse: A universe in the CR3BP
    CelestialBody: A general celestial body
    CoordinateSystem: A general coordinate system

"""

import math

class Universe:

    """A general universe model."""

    pass

class Cr3bpUniverse(Universe):

    """A universe in the circular restricted three-body problem (CR3BP).
    
    Methods:
    Cr3bpUniverse(primary1, primary2) -- Use CelestialBody objects primary1
        and primary2 as two primaries.

    """
    
    def __init__(self, primary1, primary2):
        """Create a Cr3bpUniverse.

        Arguments:
        primary1 -- CelestialBody object
        primary2 -- CelestialBody object

        """
        if primary1.mass >= primary2.mass:
            self.primary = primary1
            self.secondary = primary2
        else:
            self.primary = primary2
            self.secondary = primary1
    
    # TODO: doesn't L_ref change as primaries rotate about barycenter?
    @property
    def lref(self):
        """Return the reference length L_ref."""
        pass

    @property
    def mref(self):
        """Return the reference mass M_ref."""
        return self.primary.mass + self.secondary.mass

    # TODO: needs L_ref
    @property
    def tref(self):
        """Return the characteristic time t_ref."""
        n = math.sqrt(self.g * self.mref / self.lref**3)
        return 1/n

class CelestialBody:

    """A celestial body.
    
    Class methods:
    createsun() -- return the Sun
    createjupiter() -- return Jupiter

    """
    
    # TODO: find primary sources for planetary masses

    @classmethod
    def createsun(cls):
        """Return the Sun."""
        sun = CelestialBody()
        sun.mass = 1.9891e30
        sun.r = 0
        return sun

    @classmethod
    def createjupiter(cls):
        """Return Jupiter."""
        jupiter = CelestialBody()
        jupiter.mass = 1.8983e27
        jupiter.r = 778298361
        return jupiter

class CoordinateSystem:

    """A coordinate system."""
    
    pass

u = Cr3bpUniverse(CelestialBody.createsun(), CelestialBody.createjupiter())


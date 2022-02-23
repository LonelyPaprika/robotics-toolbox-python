#!/usr/bin/env python

import numpy as np
from roboticstoolbox.robot.ERobot import ERobot


class vx300(ERobot):
    """
    Class that imports a VX300 URDF model

    ``vx300()`` is a class which imports an Interbotix vx300 robot definition
    from a URDF file.  The model describes its kinematic and graphical
    characteristics.

    .. runblock:: pycon

        >>> import roboticstoolbox as rtb
        >>> robot = rtb.models.URDF.vx300()
        >>> print(robot)

    Defined joint configurations are:

    - qz, zero joint angle configuration, 'L' shaped configuration
    - qr, vertical 'READY' configuration

    :reference:
        - http://www.support.interbotix.com/html/specifications/vx300.html

    .. codeauthor:: Jesse Haviland
    .. sectionauthor:: Peter Corke
    """

    def __init__(self):

        links, name, urdf_string, urdf_filepath = self.URDF_read(
            "interbotix_descriptions/urdf/vx300.urdf.xacro"
        )

        super().__init__(
            links,
            name=name,
            manufacturer="Interbotix",
            urdf_string=urdf_string,
            urdf_filepath=urdf_filepath,
        )

        self.qr = np.array([0, -0.3, 0, -2.2, 0, 2.0, np.pi / 4, 0])
        self.qz = np.zeros(8)

        self.logconfiguration("qr", self.qr)
        self.logconfiguration("qz", self.qz)


if __name__ == "__main__":  # pragma nocover

    robot = vx300()
    print(robot)

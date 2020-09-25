from math import pi

from helpers import compute_volume

import pygmsh


def test():
    with pygmsh.opencascade.Geometry() as geom:
        geom.add_cone(
            [0.0, 0.0, 0.0],
            [0.0, 0.0, 1.0],
            1.0,
            0.3,
            mesh_size=0.1,
            angle=1.25 * pi,
        )
        mesh = pygmsh.generate_mesh(geom)

    ref = 0.90779252263
    assert abs(compute_volume(mesh) - ref) < 1.0e-2 * ref
    return mesh


if __name__ == "__main__":
    test().write("opencascade_cone.vtu")

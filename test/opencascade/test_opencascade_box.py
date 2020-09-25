from helpers import compute_volume

import pygmsh


def test():
    with pygmsh.opencascade.Geometry() as geom:
        geom.add_box([0.0, 0.0, 0.0], [1, 2, 3], mesh_size=0.1)
        mesh = pygmsh.generate_mesh(geom)

    ref = 6.0
    assert abs(compute_volume(mesh) - ref) < 1.0e-2 * ref
    return mesh


if __name__ == "__main__":
    test().write("opencascade_box.vtu")

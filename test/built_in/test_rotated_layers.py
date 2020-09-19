from math import pi

from helpers import compute_volume

import pygmsh


def test(mesh_size=0.05):
    geom = pygmsh.built_in.Geometry()

    # Draw a square
    poly = geom.add_polygon(
        [[+0.5, +0.0, 0.0], [+0.0, +0.5, 0.0], [-0.5, +0.0, 0.0], [+0.0, -0.5, 0.0]],
        mesh_size=mesh_size,
    )

    axis = [0, 0, 1.0]

    geom.extrude(
        poly.surface,
        translation_axis=axis,
        rotation_axis=axis,
        point_on_axis=[0.0, 0.0, 0.0],
        angle=0.5 * pi,
        num_layers=5,
        recombine=True,
    )

    ref = 3.98156496566
    mesh = pygmsh.generate_mesh(geom)
    assert abs(compute_volume(mesh) - ref) < 1.0e-2 * ref
    return mesh


if __name__ == "__main__":
    test().write("rotated_layers.vtu")
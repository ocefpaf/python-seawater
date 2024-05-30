import unittest
from pathlib import Path

import numpy as np

import seawater as sw

rootpath = Path(__file__).parent
fname = rootpath.joinpath("data", "shapes.npz")


class InputShapes(unittest.TestCase):
    def setUp(self):
        with np.load(fname) as shapes:
            self.cp = shapes["cp"]
            self.lon = shapes["lon"]
            self.lat = shapes["lat"]
            self.dens = shapes["dens"]
            self.depth = shapes["depth"]
            self.s_mean = shapes["s_mean"]
            self.t_mean = shapes["t_mean"]
            self.pt_mean = shapes["pt_mean"]
            self.steric_height = shapes["steric_height"]

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_1D(self):
        steric_height_new = sw.gpan(
            self.s_mean[:, 0, 0],
            self.t_mean[:, 0, 0],
            self.depth,
        )
        np.testing.assert_array_almost_equal(
            self.steric_height[:, 0, 0],
            steric_height_new,
        )

    def test_2D(self):
        steric_height_new = sw.gpan(
            self.s_mean[..., 1],
            self.t_mean[..., 1],
            self.depth[..., None],
        )
        np.testing.assert_array_almost_equal(
            self.steric_height[..., 1],
            steric_height_new,
        )

    def test_3D(self):
        steric_height_new = sw.gpan(
            self.s_mean,
            self.t_mean,
            self.depth[..., None, None],
        )
        np.testing.assert_array_almost_equal(
            self.steric_height,
            steric_height_new,
        )

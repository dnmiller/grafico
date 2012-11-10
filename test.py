import unittest
from grafico import Axis, GraficoException


class TestAxis(unittest.TestCase):
    def test_labels(self):
        def with_lim(lim, labels):
            format = '{:g}'.format
            a = Axis(lim=lim, scale='linear')
            self.assertItemsEqual(map(format, labels), a.labels(len(labels)))
        with_lim(lim=[0, 1], labels=[0])
        with_lim(lim=[0, 1], labels=[0, 1])
        with_lim(lim=[0, 3], labels=[0, 1, 2, 3])
        with_lim(lim=[0, 1], labels=[0.0, 0.25, 0.5, 0.75, 1.0])
        with_lim(lim=[0, 10], labels=[0.0, 10.0 / 3.0, 20.0 / 3.0, 10.0])
        with_lim(lim=[-1, 0], labels=[-1.0, -0.75, -0.5, -0.25, 0.0])
        with_lim(lim=[-1, 1], labels=[-1.0, -0.5, 0, 0.5, 1.0])
        with_lim(lim=[0, -3], labels=[0, -1, -2, -3])

    def test_labels_errors(self):
        self.assertRaisesRegexp(GraficoException,
                                'Limits must be 2-element iterable.',
                                Axis, lim=[-1, 32, 40])
        self.assertRaisesRegexp(GraficoException,
                                'Limits must be 2-element iterable.',
                                Axis, lim=[-1])


if __name__ == '__main__':
    unittest.main()

import unittest


# TODO:
# - Add log axes.


class GraficoException(Exception):
    pass


class Axis(object):
    def __init__(self, lim, scale='linear'):
        self.lim = lim

    @property
    def lim(self):
        return self.__lim

    @lim.setter
    def lim(self, lim):
        if len(lim) != 2:
            raise GraficoException('Limits must be 2-element iterable.')
        self.__lim = lim

    def labels(self, num_labels=10, format='{:g}'.format):
        """
        Return a list of strings to be used as labels for an axis.
        """
        if num_labels < 1:
            raise GraficoException('Number of labels must be > 0.')
        elif num_labels == 1:
            return [format(self.__lim[0])]
        elif num_labels == 2:
            return map(format, self.__lim)
        else:
            m = (self.__lim[1] - self.__lim[0]) / float(num_labels - 1)
            labels = [self.__lim[0] + x * m for x in xrange(num_labels)]
            return map(format, labels)


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


if __name__ == '__main__':
    unittest.main()

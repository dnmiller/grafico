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

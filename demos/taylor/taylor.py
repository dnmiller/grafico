from lxml import etree
from lxml.etree import Element, SubElement

units = ['em', 'ex', 'px', 'pt', 'pc', 'cm', 'mm', 'in', '%']


# TODO Make a canvas class with a factory for Graphs.
class Graph(object):
    """
    We got a graphic with some axes, and we got some factories for basic
    shapes.
    """
    def __init__(self, size, xlim, ylim):
        """
        Initialize a Graph object with a size (in the document-size sense) and
        x and y limits.
        """
        w = xlim[1] - xlim[0]
        h = ylim[1] - ylim[0]
        viewBox = '{0} {1} {2} {3}'.format(xlim[0], ylim[0], w, h)
        # x and y are a hack for now to make the figures easier to view in
        # Chrome. TODO: delete them.
        self.__svg = SubElement(canvas, 'svg',
                                width=size[0], height=size[1],
                                x='100px', y='100px',
                                viewBox=viewBox,
                                preserveAspectRatio='none')

        # The y-axis in SVG is reverse from the typical graph axis. This
        # creates a group that reverses the y-axis and translates it so that
        # the upper and lower bounds of the viewbox are the y limits.
        self.__axes_group = SubElement(
            self.__svg, 'g', transform='scale(1, -1) translate(0, {0})'.format(
                -ylim[0] - ylim[1]))

        axis_style = 'stroke: grey; stroke-width: 1; color: #DDDDDD'

        self.xaxis = self.line((xlim[0], 0), (xlim[1], 0), axis_style,
                               scale=False)
        self.yaxis = self.line((0, ylim[0]), (0, ylim[1]), axis_style,
                               scale=False)
        self.xlim = xlim
        self.ylim = ylim

    def line(self, p0, p1, width='1px', style='stroke: black', scale=True):
        """
        Create a line from p0 in (x, y) to p2.
        """
        line = SubElement(self.__axes_group, 'line',
                          x1='{0}'.format(p0[0]), y1='{0}'.format(p0[1]),
                          x2='{0}'.format(p1[0]), y2='{0}'.format(p1[1]),
                          style=style)
        line.set('stroke-width', width)
        if not scale:
            line.set('vector-effect', 'non-scaling-stroke')
        return line

    def circle(self, center, radius, style):
        """
        Create a circle with center and radius
        """
        return SubElement(self.__axes_group, 'circle',
                          r='{0}'.format(radius),
                          cx='{0}'.format(center[0]),
                          cy='{0}'.format(center[1]),
                          style=style)


canvas = Element('svg', xmlns='http://www.w3.org/2000/svg')
plot = Graph(size=['640px', '480px'], xlim=[-1, 12], ylim=[-5, 5])


pane = SubElement(canvas, 'rect', width='640px', height='480px',
                  x='100px', y='100px',
                  style='stroke: black; stroke-width: 2; fill: None')
print etree.tostring(canvas, pretty_print=True)
with open('taylor.svg', 'w') as f:
    f.write(etree.tostring(canvas))

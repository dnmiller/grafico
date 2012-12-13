from lxml import etree
from lxml.etree import Element, SubElement

units = ['em', 'ex', 'px', 'pt', 'pc', 'cm', 'mm', 'in', '%']


class Graph(object):
    def __init__(self, size, xlim, ylim):
        w = xlim[1] - xlim[0]
        h = ylim[1] - ylim[0]
        viewBox = '{0} {1} {2} {3}'.format(xlim[0], ylim[0], w, h)
        self.__svg = SubElement(canvas, 'svg',
                                width=size[0], height=size[1],
                                x='100px', y='100px',
                                viewBox=viewBox,
                                preserveAspectRatio='none')
        self.__gt = SubElement(
            self.__svg, 'g', transform='scale(1, -1) translate(0, {0})'.format(
                -ylim[0] - ylim[1]))

        self.elem = self.__gt

        axis_style = 'stroke: grey; stroke-width: 1; color: #DDDDDD'

        self.xaxis = self.line((xlim[0], 0), (xlim[1], 0), axis_style,
                               scale=False)
        self.yaxis = self.line((0, ylim[0]), (0, ylim[1]), axis_style,
                               scale=False)
        self.xlim = xlim
        self.ylim = ylim

    def line(self, p0, p1, width='1px', style='stroke: black', scale=True):
        line = SubElement(self.elem, 'line',
                          x1='{0}'.format(p0[0]), y1='{0}'.format(p0[1]),
                          x2='{0}'.format(p1[0]), y2='{0}'.format(p1[1]),
                          style=style)
        line.set('stroke-width', width)
        if not scale:
            line.set('vector-effect', 'non-scaling-stroke')
        return line

    def circle(self, center, radius, style):
        return SubElement(self.elem, 'circle',
                          r='{0}'.format(radius),
                          cx='{0}'.format(center[0]),
                          cy='{0}'.format(center[1]),
                          style=style)


canvas = Element('svg', xmlns='http://www.w3.org/2000/svg')
plot = Graph(size=['640px', '480px'], xlim=[-1, 12], ylim=[-5, 5])

circle = plot.circle((0, 0), 8, 'fill: red')


pane = SubElement(canvas, 'rect', width='640px', height='480px',
                  x='100px', y='100px',
                  style='stroke: black; stroke-width: 2; fill: None')
print etree.tostring(canvas, pretty_print=True)
with open('taylor.svg', 'w') as f:
    f.write(etree.tostring(canvas))

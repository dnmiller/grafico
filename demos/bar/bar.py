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
        self.__gs = SubElement(self.__svg, 'g', transform='scale(1, -1)')
        self.__gt = SubElement(
            self.__gs, 'g', transform='translate(0, {0})'.format(
                -ylim[0] - ylim[1]))

        self.elem = self.__gt

        axis_style = 'stroke: grey; stroke-width: 1; color: #DDDDDD'

        self.xaxis = self.line((xlim[0], 0), (xlim[1], 0), axis_style)
        self.yaxis = self.line((0, ylim[0]), (0, ylim[1]), axis_style)

        self.xlim = xlim
        self.ylim = ylim

    def line(self, p0, p1, style):
        return SubElement(self.elem, 'line',
                          x1='{0}'.format(p0[0]), y1='{0}'.format(p0[1]),
                          x2='{0}'.format(p1[0]), y2='{0}'.format(p1[1]),
                          style=style)


canvas = Element('svg', xmlns='http://www.w3.org/2000/svg')
plot_area = Graph(size=['640px', '480px'], xlim=[-40, 400], ylim=[-10, 400])


#x_axis = line((axis_box[0] + 5, 0), (axis_box[2] - 5, 0), axis_style)

circle = SubElement(plot_area.elem, 'circle',
                    r='5', cx='0', cy='0',
                    style='fill: red')


def circle(x, y):
    SubElement(plot_area.elem, 'circle',
               r='5', cx='{0}'.format(x), cy='{0}'.format(y),
               style='fill: blue')

#line = SubElement(plot_area, 'line',
                  #x2='100', y2='300',
                  #style='stroke: blue; stroke-width: 10')

pane = SubElement(canvas, 'rect', width='640px', height='480px',
                  x='100px', y='100px',
                  style='stroke: black; stroke-width: 2; fill: None')

print etree.tostring(canvas, pretty_print=True)

with open('bar.svg', 'w') as f:
    f.write(etree.tostring(canvas))

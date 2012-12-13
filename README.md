This is just practice for drawing plots in SVG with ElementTree. Nothing to see here.


Structure
---------
- A bunch of factory classes for XML elements.
- All elements inherit from lxml elements - basic XML structure remains
  exposed.

- Hierarchy:
    - Figure (svg)
        - Box
            - X Limits
            - Y Limits
            - Axis
                - Line (line)
                - Labels (list of text elements)
                - Ticks (list of lines)
            - Path
                - Marker
            - Polygon
            - Text
        - Legend
            - Box
                - Line
                - Label (text)
        - Title (text)

- All styles handled via CSS (to be implemented later)


Features
--------
- lin/log axes for all
- line
- bar plot
- scatter
- stairs
- contour
- polar
- spy
- stem
- box
- error bars
- stacked bars
- compass
- streamlines
- grids


Some Use Cases
--------------
- Quick plotting of lines in a clean, conservative style.
    - plot(x, y) returns svg object
        - x and y can be lists or numpy arrays

- Reading in an svg file and changing the that defines a path element.


Plan
----
- Implement all features as separate functions. Build out into classes
  afterwards.

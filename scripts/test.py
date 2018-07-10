from wilcox import Circle, Ellipse, Parabola, Hyperbola
x, y = 500, 500

circle = Circle()
circle.draw()
circle.draw(x, y)

ellipse = Ellipse()
ellipse.draw(x, y)

parabola = Parabola()
parabola.draw(x, y)

hyperbola = Hyperbola()
hyperbola.draw(x, y)

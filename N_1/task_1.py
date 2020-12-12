from typing import NamedTuple
import matplotlib.pyplot as plt


def inside(p, q, r):
    if ((q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and
            (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))):
        return True
    return False


def orientation(p, q, r):

    val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y))
    if val > 0:
        return 1
    elif val < 0:
        return 2
    else:
        return 0


def intersect(p1, q1, p2, q2):

    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return True

    if o1 == 0 and inside(p1, p2, q1):
        return True

    if o2 == 0 and inside(p1, q2, q1):
        return True

    if o3 == 0 and inside(p2, p1, q2):
        return True

    if o4 == 0 and inside(p2, q1, q2):
        return True

    # If none of the cases
    return False


class Point(NamedTuple):
    x: float
    y: float

    def print(self):
        print(self.x, self.y)


class Polygon(NamedTuple):
    x_arr: list
    y_arr: list
    closed: bool

    def add_point(self, point):
        self.x_arr.append(point.x)
        self.y_arr.append(point.y)

    def print_list(self):
        for i in range(len(self.x_arr)):
            print(self.x_arr[i], self.y_arr[i])

    def show(self, num=0, text = ""):
        if num_of_polygons > 1:
            plot = subplots[num]
        else:
            plot = plt
        for i in range(len(self.x_arr) - 1):
            x = [self.x_arr[i], self.x_arr[i + 1]]
            y = [self.y_arr[i], self.y_arr[i + 1]]
            plot.plot(x, y, color="b")
        if closed:
            x = [self.x_arr[-1], self.x_arr[0]]
            y = [self.y_arr[-1], self.y_arr[0]]
            plot.plot(x, y, color="b")
        plot.set_title(text)

    def check_intersections(self):
        for i in range(len(self.x_arr) - 1):
            p1 = Point(self.x_arr[i], self.y_arr[i])
            q1 = Point(self.x_arr[i + 1], self.y_arr[i + 1])
            for j in range(i + 2, len(self.x_arr) - 1):
                p2 = Point(self.x_arr[j], self.y_arr[j])
                q2 = Point(self.x_arr[j + 1], self.y_arr[j + 1])
                if intersect(p1, q1, p2, q2):
                    return "There are self-intersections"
        return "There are no self-intersections"


def read_from_file(name):
    f = open(name, 'r')
    pol = Polygon([], [], closed)
    cnt = 0
    prev = 0
    for line in f:
        for el in line.split():
            cnt += 1
            curr = float(el)
            if cnt % 2 == 0:
                pol.add_point(Point(prev, curr))
            prev = curr
    f.close()
    return pol


closed = False
num_of_polygons = 2
fig, subplots = plt.subplots(num_of_polygons)
fig.tight_layout(pad=3.0)
polygon_1 = read_from_file("a.txt")
polygon_2 = read_from_file("b.txt")
inters1 = polygon_1.check_intersections()
inters2 = polygon_2.check_intersections()
polygon_1.show(0, inters1)
polygon_2.show(1, inters2)
plt.show()


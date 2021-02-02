import random
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import cKDTree
import PRM as prm
import prm_star as prms
import rrt
import rrt_star as rrts
import dijkstra as dj
import a_star as a

def main():
    gx = 20
    gy = 30
    m = map()
    m.set_g(gx, gy)
    while True:
        print("Maximum points of PRM, PRM* : " + str(m.N_SAMPLE))
        print("Goal of RRT, RRT*: "+str(gx)+", "+str(gy))
        print("1. PRM")
        print("2. PRM*")
        print("3. RRT")
        print("4. RRT*")
        print("5. Dijkstra")
        print("6. A*")
        print("7. Set Goal")
        print("8. Set maximum PRM, PRM* points: ")
        print("9. Show table")
        print("10. PRM")
        print("11. PRM*")
        print("0. Exit")
        option = int(input())
        #option = 4
        if option is 0:
            exit(1)
        if option is 1:
            print("PRM selected")
            m.prm()
        if option is 2:
            print("PRM* selected")
            m.prm_star()
        if option is 3:
            print("RRT selected")
            rrt.main(gx, gy)
        if option is 4:
            print("RRT* selected")
            rrts.main(gx, gy)
        if option is 5:
            print("Dijkstra selected")
            dj.main()
        if option is 6:
            print("A* selected")
            a.main()
        if option is 7:
            print("Set Goal:")
            gx = (int(input("Input gx: ")))
            gy = (int(input("Input gy: ")))
            m.set_g(gy, gx)
        if option is 8:
            print("Set N:")
            m.set_n(int(input()))
        if option is 9:
            print("Show table")
            m.render()
        if option is 10:
            print("Selected RPM to compare")
            m.prm_ss()
        if option is 11:
            print("Selected RPM* to compare")
            m.prm_star_ss()





class map:
    N_SAMPLE = 500  # number of sample_points
    N_KNN = 10  # number of edge from one sampled point
    MAX_EDGE_LEN = 30.0  # [m] Maximum edge length
    sx = 10.0  # [m]
    sy = 10.0  # [m]
    gx = 50.0  # [m]
    gy = 50.0  # [m]
    robot_size = 2.5  # [m]
    ox = []
    oy = []

    def set_g(self, gx, gy):
        self.gx = gx
        self.gy = gy

    def set_n(self, n):
        self.N_SAMPLE = n;
    def draw(self):
        for i in range(60):
            self.ox.append(i)
            self.oy.append(0.0)
        for i in range(60):
            self.ox.append(60.0)
            self.oy.append(i)
        for i in range(61):
            self.ox.append(i)
            self.oy.append(60.0)
        for i in range(61):
            self.ox.append(0.0)
            self.oy.append(i)
        for i in range(10):
            self.ox.append(20+i)
            self.oy.append(20.0)
        for i in range(10):
            self.ox.append(30)
            self.oy.append(20.0-i)
        for i in range(40):
            self.ox.append(40.0)
            self.oy.append(60.0 - i)
        for i in range(10):
            self.ox.append(40+i)
            self.oy.append(20)
        for i in range(10):
            self.ox.append(20+i)
            self.oy.append(10)
        # for i in range(10):
        #     self.ox.append(30)
        #     self.oy.append(20-i)
        plt.clf()
        plt.plot(self.ox, self.oy, ".k")
        plt.plot(self.sx, self.sy, "^r")
        plt.plot(self.gx, self.gy, "^c")
        plt.grid(True)
        plt.axis("equal")
    def redraw(self):
        self.ox = []
        self.oy = []
        for i in range(60):
            self.ox.append(i)
            self.oy.append(0.0)
        for i in range(60):
            self.ox.append(60.0)
            self.oy.append(i)
        for i in range(61):
            self.ox.append(i)
            self.oy.append(60.0)
        for i in range(61):
            self.ox.append(0.0)
            self.oy.append(i)
        for i in range(20):
            self.ox.append(20.0)
            self.oy.append(i)
        for i in range(40):
            self.ox.append(40.0)
            self.oy.append(60.0 - i)
        plt.clf()
        plt.plot(self.ox, self.oy, ".k")
        plt.plot(self.sx, self.sy, "^r")
        plt.plot(self.gx, self.gy, "^c")
        plt.grid(True)
        plt.axis("equal")
    def render(self):
        self.draw()
        plt.show()

    def prm(self):
        self.draw()
        rx, ry = prm.prm_planning(self.sx, self.sy, self.gx, self.gy, self.ox, self.oy, self.robot_size, self.N_SAMPLE)
        plt.plot(rx, ry, "-r")
        #plt.pause(0.001)
        plt.show()
        
    def prm_star(self):
        self.draw()
        rx, ry = prms.prm_planning(self.sx, self.sy, self.gx, self.gy, self.ox, self.oy, self.robot_size, self.N_SAMPLE)
        plt.plot(rx, ry, "-r")
        plt.show()

    def prm_ss(self):
        self.redraw()
        rx, ry = prm.prm_planning(self.sx, self.sy, self.gx, self.gy, self.ox, self.oy, self.robot_size, self.N_SAMPLE)
        plt.plot(rx, ry, "-r")
        # plt.pause(0.001)
        plt.show()

    def prm_star_ss(self):
        self.redraw()
        rx, ry = prms.prm_planning(self.sx, self.sy, self.gx, self.gy, self.ox, self.oy, self.robot_size, self.N_SAMPLE)
        plt.plot(rx, ry, "-r")
        plt.show()

if __name__ == "__main__":
    main()


# Delaunay-Triangulation-Pygame

The code is based on [this](https://gorillasun.de/blog/bowyer-watson-algorithm-for-delaunay-triangulation/) article.

## Overview

Delaunay Triangulation implemented in python and solved using Bowyer-Watson algorithm. The program takes a set of points and connects them using a mesh.

<p align="center">
  <img src="media/Delaunay_Triangulation.gif" alt="Delauny Triangulation Gif" />
</p>

## Usage

Running the `main.py` will create a delaunay triangulated mesh out of random points. Clicking on the screen will create a new point the mesh is recalculated to add the new point into the mesh. The mesh and its heatmap are rendered using Pygame.

The Delaunay triangulation code can be used without using any renderer.

```
from delaunayTriangulation import DelaunayTriangulation
import numpy as np

N = 50

for i in range(N):
	point = Point(randint(0, 100), randint(0, 100), randint(0, 50))
	DT.AddPoint(point)

DT.Triangulate()

```
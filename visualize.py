import copy
import numpy as np
import open3d as o3d
import os

objFilePath = './Area_5_conferenceRoom_2_gt.obj'

with open(objFilePath) as file:
    points = []
    while 1:
        line = file.readline()
        if not line:
            break
        strs = line.split(" ")
        if strs[0] == "v":
            points.append(np.array(strs[1:7],dtype=float))
        if strs[0] == "vt":
            break
# points原本为列表，需要转变为矩阵，方便处理          
pcd = np.array(points)

pcd_vector = o3d.geometry.PointCloud()
pcd_vector.points = o3d.utility.Vector3dVector(pcd[:, :3])
pcd_vector.colors = o3d.utility.Vector3dVector(pcd[:,3:6])
o3d.visualization.draw_geometries([pcd_vector])

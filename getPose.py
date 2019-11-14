import cv2
import argparse
import numpy as np
import os

parser = argparse.ArgumentParser()
parser.add_argument("file")
parser.add_argument("saving_dir")
args = parser.parse_args()

Rotv = []
Transv = []

with open(args.file) as f:
    buf = f.readlines()
    for line in buf:
        line = line.split()
        v = []
        for i in range(5, 8):
            v.append(float(line[i]))
        v = np.array(v)
        Rotv.append(v)
        v = []
        for i in range(8, 11):
            v.append(float(line[i]))
        v = np.array(v)
        Transv.append(v)


if not os.path.exists(args.saving_dir):
    os.mkdir(args.saving_dir)

for i in range(len(Transv)):
    print('process frame ', i)
    rotm = cv2.Rodrigues(Rotv[i])[0]
    pose = np.eye(4)
    pose[0:3, 0:3] = rotm
    pose[0:3, 3] = Transv[i]
    np.savetxt(args.saving_dir+'pose'+str(i)+'.txt', pose)


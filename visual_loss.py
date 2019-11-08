import argparse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()

with open(args.file) as f:
    buf = f.readlines()
    index = []
    loss = []
    for line in buf:
        line = line.split()
        index.append(int(line[0]))
        loss.append(float(line[1]))

plt.plot(index,loss,color='b',label='loss')
plt.xlabel('Iter')
plt.ylabel('Loss')
plt.savefig('loss.png')


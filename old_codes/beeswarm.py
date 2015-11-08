#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from beeswarm import *
import sys, getopt
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from collections import Counter

d1 = np.random.uniform(low=-3, high=3, size=100)
d2 = np.random.normal(size=100)
    
bs, ax = beeswarm([d1,d2], method="swarm", labels=["sample 1", "sample 2"], col=["blue","red"]) 

  


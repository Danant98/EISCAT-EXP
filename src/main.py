"""
@author: Daniel Elisabethsønn Antonsen

Assignment based on data obtained from experiment done at the EISCAT radar near Tromsø, Norway

"""
# Import libraries and modules
import matplotlib.pyplot as plt
import numpy as np
import os
# Import dataset
dataset = np.loadtxt(os.path.join("resources", "2022-03-24_beata_5@uhfa 1.tgz"))
print(dataset)

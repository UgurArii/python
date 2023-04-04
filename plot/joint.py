import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

tips = sns.load_dataset('tips')
with sns.axes_style(style='ticks'):
    g = sns.factorplot("day","total_bill", "sex", data=tips, kind="box")
    g.set_axis_labels("Bill DAy","Total Bill Amount")
with sns.axes_style('white'):
    sns.jointplot("total_bill","tip", data=tips, kind="hex")


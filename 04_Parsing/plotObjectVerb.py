import sys
import matplotlib.pyplot as plt

labels = {0:'zh', 1:'vi', 2:'en', 3:'fr', 4:'sr', 5:'lt', 6:'de', 7:'fa', 8:'ug', 9:'ja'}
x = [0.0029149797570850204, 0.036065573770491806, 0.0638647569852078, 0.11801632140615191, 0.1299093655589124, 0.328551912568306, 0.4557135046473483, 0.9831571994715984, 0.9991496598639455, 1.0]  # proportion of OV
y = [0.997085020242915, 0.9639344262295082, 0.9361352430147922, 0.8819836785938481, 0.8700906344410876, 0.671448087431694, 0.5442864953526517, 0.016842800528401584, 0.0008503401360544217, 0.0]  # proportion of VO
plt.plot(x, y, 'ro')
plt.title('Relative word order of verb and object')
plt.xlim([0,1]) # Set the x and y axis ranges
plt.ylim([0,1])
plt.xlabel('OV') # Set the x and y axis labels
plt.ylabel('VO')
for i in labels:  # Add labels to each of the points
    plt.text(x[i]-0.03, y[i]-0.03, labels[i], fontsize=9)
plt.savefig('plotOut.png')

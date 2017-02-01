n, bins, patches = plt.hist(sim, 40, histtype='bar')
plt.axvline(x=rho, color='red')
# <matplotlib.lines.Line2D object at ...>
plt.show()

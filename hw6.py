import matplotlib.pyplot as plt

# 1.Create plot for simple x and y arrays, show the result.

x = [8, 12, 30]
y = [43, 65, 11]
plt.plot(x, y)

# 2 and 3.
# Create a plot containing several subplots, show the result.
# Create a plot customize size, color, labels and other features, show the result.

fig = plt.figure(figsize=(10, 8))
fig.suptitle("Charts", color='g', fontsize=20)
fig.subplots_adjust(hspace=0.5, wspace=0.5)
plt.xlabel('X label', color='r', fontsize=17)
plt.ylabel('Y label', color='r', fontsize=17)

ax1 = fig.add_subplot(3, 2, 1)
ax1.plot([10, 50, 20, 35], color="#31ED31")
ax1.axhline(30, color='r', linestyle='dotted')
ax1.set_title("Line with axhline", color='#ff7518')

ax2 = fig.add_subplot(3, 2, 2)
ax2.scatter([60, 25, 30], [5, 50, 9], color="m")
ax2.set_title("Scatter", color='#ff7518')

ax3 = fig.add_subplot(3, 2, 3)
ax3.bar([34, 50, 4, 90], [5, 12, 3, 8], color="brown", linewidth=14)
ax3.set_title("Bar", color='#ff7518')

ax4 = fig.add_subplot(3, 2, 4)
ax4.boxplot([20, 3, 65, 4], [5, 19, 53, 68])
ax4.set_title("Boxplot", color='#ff7518')

ax5 = fig.add_subplot(3, 2, 5)
ax5.barh([30, 3, 65, 40], [15, 19, 53, 68], color="#00C4B0", linewidth=10)
ax5.set_title("Bar horizontal  with axvline", color='#ff7518')
ax5.axvline(35, color='b', linestyle='dashed', linewidth=2)

ax6 = fig.add_subplot(3, 2, 6)
ax6.plot([30, 3, 65, 40], [15, 19, 53, 68], color="#00C4B0", linewidth=2, marker = '^', markersize = 12, linestyle = 'dashed')
ax6.set_title("Line", color='#ff7518')


# 4. Create a plot, customize it and save the result to file.

from matplotlib.backends.backend_pdf import PdfPages
pdf = PdfPages('chart.pdf')
pdf.savefig()
pdf.close()
plt.savefig("chart.png")

plt.show()
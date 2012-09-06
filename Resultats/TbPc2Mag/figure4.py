import matplotlib.image as mpimg #pour les images
from matplotlib.patches import Polygon, Ellipse
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
#loading script for Zeeman diagram
execfile("/home/hukadan/These/Manuscript/old/Theorie/MagMol/scripts/TbPc2Nuclear.py")

#on regle le style des fleches
arrowpropsleft=dict(arrowstyle='-|>',connectionstyle="arc3,rad=0.0",linewidth=3,color="blue")
arrowpropsright=dict(arrowstyle='-|>',connectionstyle="arc3,rad=-0.0",linewidth=3,color="blue")
arrowpropsboth=dict(arrowstyle='<|-|>',connectionstyle="arc3,rad=-0.0",linewidth=3,color="black")

#on fait les figures
fig = figure()
fig.set_size_inches(12,10)
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)
###########
#figure3.a
R = Tb_Pc2_Zeeman(-10,10,1000,0,0)
B = linspace(-10,10,1000)
ax1.plot(B,R,color="red")
YMIN = -645-50
YMAX = -645+50
ax1.plot([-3,-3,3,3,-3],[YMIN,YMAX,YMAX,YMIN,YMIN],'--',color="black")
#\Delta
ax1.annotate("",(0,-640),(0, -50),ha="center",va="center",arrowprops=arrowpropsboth)
ax1.text(0.25,-300,r"$\sim 600\,$K",fontsize=25,horizontalalignment='left', verticalalignment='center')

############################
#figure3.b
R = Tb_Pc2_Zeeman(-0.5e-6,0.5e-6,200,0,0)
R = R - (R[100][0]+R[100][1])/2.
B = linspace(-0.5e-6,0.5e-6,200)
ax2.plot(B,R,color="red")
ax2.set_xlim(-0.5e-6,0.5e-6)
ax2.set_ylim(-3e-6,3e-6)

#Celle pour \Delta
ax2.annotate("",(0,-0.5e-6),(0, 0.5e-6),ha="center",va="center",arrowprops=arrowpropsboth)
ax2.text(0.02e-6,0.0,r"$\Delta_{-6,6}$",fontsize=25,horizontalalignment='left', verticalalignment='center')
#ket
ax2.text(-0.35e-6,2.5e-6,r"$|-6 \rangle$",fontweight="bold",fontsize=20,color = "blue",horizontalalignment='left', verticalalignment='center')
ax2.text(-0.35e-6,-2.5e-6,r"$|+6 \rangle$",fontweight="bold",fontsize=20,color = "blue",horizontalalignment='left', verticalalignment='center')
ax2.text(0.35e-6,-2.5e-6,r"$|-6 \rangle$",fontweight="bold",fontsize=20,color = "blue",horizontalalignment='right', verticalalignment='center')
ax2.text(0.35e-6,2.5e-6,r"$|+6 \rangle$",fontweight="bold",fontsize=20,color = "blue",horizontalalignment='right', verticalalignment='center')


############################
#figure3.c
R = Tb_Pc2_ZeemanNuclear(-0.1,0.1,100,0,0)
B = linspace(-0.1,0.1,100)
ax3.plot(B,R,color="red")
ax3.set_xlim(-0.1,0.205)
ax3.set_ylim(-645.3,-643.75)

ax3.text(0.105,-643.9,r"$|+6\rangle |+3/2 \rangle$",fontweight="bold",fontsize=20,color = "blue",horizontalalignment='left', verticalalignment='center')
ax3.text(0.105,-644.05,r"$|+6\rangle |+1/2 \rangle$",fontweight="bold",fontsize=20,color = "blue",horizontalalignment='left', verticalalignment='center')
ax3.text(0.105,-644.20,r"$|+6\rangle |-1/2 \rangle$",fontweight="bold",fontsize=20,color = "blue",horizontalalignment='left', verticalalignment='center')
ax3.text(0.105,-644.35,r"$|+6\rangle |-3/2 \rangle$",fontweight="bold",fontsize=20,color = "blue",horizontalalignment='left', verticalalignment='center')

ax3.text(0.105,-644.75,r"$|-6\rangle |-3/2 \rangle$",fontweight="bold",fontsize=20,color = "blue",horizontalalignment='left', verticalalignment='center')
ax3.text(0.105,-644.9,r"$|-6\rangle |-1/2 \rangle$",fontweight="bold",fontsize=20,color = "blue",horizontalalignment='left', verticalalignment='center')
ax3.text(0.105,-645.05,r"$|-6\rangle |+1/2 \rangle$",fontweight="bold",fontsize=20,color = "blue",horizontalalignment='left', verticalalignment='center')
ax3.text(0.105,-645.2,r"$|-6\rangle |+3/2 \rangle$",fontweight="bold",fontsize=20,color = "blue",horizontalalignment='left', verticalalignment='center')

ax3.text(0.0,-643.9,r"$|J_z\rangle |I_z \rangle$",fontweight="bold",fontsize=20,color = "blue",horizontalalignment='center', verticalalignment='center')

r1 = Ellipse((-0.056,-644.55),0.02,0.02/0.197,facecolor="#C0C0C0")
ax3.add_patch(r1)
r1 = Ellipse((-0.019,-644.58),0.02,0.02/0.197,facecolor="#C0C0C0")
ax3.add_patch(r1)
r1 = Ellipse((+0.056,-644.55),0.02,0.02/0.197,facecolor="#C0C0C0")
ax3.add_patch(r1)
r1 = Ellipse((+0.019,-644.58),0.02,0.02/0.197,facecolor="#C0C0C0")
ax3.add_patch(r1)

################################
#figure 3.d
Fe = mpimg.imread("/home/hukadan/These/Manuscript/Resultats/TbPc2Mag/TbCycle.png")
Fe = Fe.tolist()
Fe.reverse()
ax4.imshow(Fe, extent = [-1.2,1.2,-1,1])
ax4.set_ylim(-1.1,1.1)


###########################
#Mise en page du plot
#compute scale multiplicator
xmin= ax1.get_xlim()
ymin= ax1.get_ylim()
a1 = 1.0 * abs((xmin[0]-xmin[1])/(ymin[0]-ymin[1]))

xmin= ax2.get_xlim()
ymin= ax2.get_ylim()
a2 = 1.0 * abs((xmin[0]-xmin[1])/(ymin[0]-ymin[1]))

xmin= ax3.get_xlim()
ymin= ax3.get_ylim()
a3 = 1.0 * abs((xmin[0]-xmin[1])/(ymin[0]-ymin[1]))
print a3

xmin= ax4.get_xlim()
ymin= ax4.get_ylim()
a4 = 1.0 * abs((xmin[0]-xmin[1])/(ymin[0]-ymin[1]))

ax1.set_aspect(a1*0.8,)
ax2.set_aspect(a2*0.8,)
ax3.set_aspect(a3*0.8,)
ax4.set_aspect(a4*0.8,)


#label des axes
#a
ax1.set_xlabel(r"$B$ (T)")
ax1.set_ylabel(r"$E$ (K)")
ax1.xaxis.set_ticks([-5,0,5])
ax1.yaxis.set_ticks([-600,-400,-200,0,200])

#b
ax2.set_xlabel(r"$B$ ($\mu$T)")
ax2.set_ylabel(r"$E$ ($\mu$K)")
ax2.xaxis.set_ticks([-0.25e-6,0,0.25e-6])
ax2.xaxis.set_ticklabels([-0.25,0,0.25])
ax2.yaxis.set_ticks([-2.5e-6,0,2.5e-6])
ax2.yaxis.set_ticklabels([-2.5,0,2.5])



#c
ax3.set_xlabel(r"$B$ (T)", position = (0.35,0))
ax3.set_ylabel(r"$E$ (K)")
ax3.xaxis.set_ticks([-0.05,0,0.05])
ax3.yaxis.set_ticks([-645,-644])

#d
ax4.set_xlabel(r"$B$ (T)")
ax4.set_ylabel(r"$M/M_{\rm{s}}$")
ax4.xaxis.set_ticks([-1,0,1])
ax4.yaxis.set_ticks([-1,0,1])

#label de la figure
fig.subplots_adjust(left=0.09,right=1,wspace=0.15,hspace=0.30, top = 0.95, bottom = 0.08)
fig.text(0.01,0.94,"a",fontsize=25,fontweight="bold")
fig.text(0.51,0.94,"b",fontsize=25,fontweight="bold")

fig.text(0.01,0.47,"c",fontsize=25,fontweight="bold")
fig.text(0.51,0.47,"d",fontsize=25,fontweight="bold")



fig.savefig("/home/hukadan/These/Manuscript/Resultats/TbPc2Mag/TbPc2Mag.pdf")
close(fig)

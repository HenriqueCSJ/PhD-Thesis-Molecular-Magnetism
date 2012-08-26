import matplotlib.image as mpimg #pour les images
from matplotlib.patches import Polygon, Circle
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
#loading script for Zeeman diagram
execfile("/home/hukadan/These/Manuscript/old/Theorie/MagMol/scripts/Fe8.py")

#on regle le style des fleches
arrowpropsleft=dict(arrowstyle='-|>',connectionstyle="arc3,rad=0.0",linewidth=3,color="blue")
arrowpropsright=dict(arrowstyle='-|>',connectionstyle="arc3,rad=-0.0",linewidth=3,color="blue")
arrowpropsboth=dict(arrowstyle='<|-|>',connectionstyle="arc3,rad=-0.0",linewidth=1,color="black")

#on fait les figures
fig = figure()
fig.set_size_inches(12,10)
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)
###########
#figure3.a
def f(x):
    return -x**2

x = linspace(-10,10,1000)

ax1.plot(x,f(x),'--',color="black")


M = linspace(-10,10,11)

for m in M :
    ax1.plot([M-1.7,M+1.7],[f(M),f(M)], color="red")
    if m == 0 :
        ax1.text(m,f(m)+5,r"$m_z = $"+str(int(m)),fontsize=20,horizontalalignment='center', verticalalignment='center')
    if( m < 0):
        ax1.text(m-2.2,f(m)-1,r"$m_z = $"+str(int(m)),fontsize=20,horizontalalignment='right', verticalalignment='center')
    if( m > 0):
        ax1.text(m+2.2,f(m)-1,r"$m_z = $"+str(int(m)),fontsize=20,horizontalalignment='left', verticalalignment='center')

ax1.set_ylim(-107,+15)
ax1.set_xlim(-25,25)


###########################
#figure3.b
R = Fe8_Zeeman(0,3,1000)
B = linspace(0,3,1000)
ax2.plot(B,R,linewidth=1.5,color="red")
ax2.set_ylim(-30,15)
r1 = Polygon([[0.3,-24],[0.3,-20],[0.5,-20],[0.5,-24]], color="#C0C0C0")
ax2.plot([0.3,0.3,0.5,0.5,0.3],[-24,-20,-20,-24,-24],color="black")
ax2.add_patch(r1)
Fe = mpimg.imread("/home/hukadan/These/Manuscript/Spintronique/FigureFe8/Fe8mol.png")
im = OffsetImage(Fe, zoom=0.2,alpha=0.95)
ab = AnnotationBbox(im,[2.95,-29.5],frameon=False,box_alignment=(1,0),bboxprops = dict(alpha=0.2))
ax2.add_artist(ab)
############################
#figure3.c
R = Fe8_Zeeman(-4e-3,4e-3,1000)
R = R - (R[500][8]+R[500][9])/2.
B = linspace(-4e-3,4e-3,1000)
ax3.plot(B,R,color="red",linewidth=1.5)
ax3.plot([-4e-3,4e-3],[0.03,-0.03],linewidth=1.5,linestyle='--',color="black")
ax3.plot([-4e-3,4e-3],[-0.03,0.03],linewidth=1.5,linestyle='--',color="black")
ax3.set_xlim(-4e-3,4e-3)
ax3.set_ylim(-0.03,0.03)

#on met m et m prime
ax3.text(-3e-3,0.018,r"$m^{\prime}$",fontsize=20,horizontalalignment='right', verticalalignment='bottom')
ax3.text(-3e-3,-0.022,r"$m$",fontsize=20,horizontalalignment='right', verticalalignment='bottom')
ax3.text(3e-3,-0.022,r"$m^{\prime}$",fontsize=20,horizontalalignment='left', verticalalignment='bottom')
ax3.text(3e-3,0.018,r"$m$",fontsize=20,horizontalalignment='left', verticalalignment='bottom')
#ensuite on met les fleche
#premiere
ax3.annotate("",(-1.5e-3,-0.0075),(-2.5e-3,-0.015),ha="center",va="center",arrowprops=arrowpropsleft)
ax3.text(-2.2e-3,-0.008,"1",fontweight="bold",fontsize=20,color = "blue",horizontalalignment='center', verticalalignment='center')
#deuxieme
ax3.annotate("",(2.5e-3, 0.015),(1.5e-3, 0.0075),ha="center",va="center",arrowprops=arrowpropsleft)
ax3.text(2.2e-3,0.008,"1-P",fontweight="bold",fontsize=20,color = "blue",horizontalalignment='center', verticalalignment='center')
#troisieme
ax3.annotate("",(2.5e-3, -0.015),(1.5e-3, -0.0075),ha="center",va="center",arrowprops=arrowpropsleft)
ax3.text(2.2e-3,-0.008,"P",fontweight="bold",fontsize=20,color = "blue",horizontalalignment='center', verticalalignment='center')
#Celle pour \Delta
ax3.annotate("",(0,-0.005),(0, 0.005),ha="center",va="center",arrowprops=arrowpropsboth)
ax3.text(-0.4e-3,0.0,r"$\Delta$",fontweight="bold",fontsize=25,horizontalalignment='center', verticalalignment='center')

################################
#figure 3.d
Fe = mpimg.imread("/home/hukadan/These/Manuscript/Spintronique/FigureFe8/Fe8Hysteresismodif.png")
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

xmin= ax4.get_xlim()
ymin= ax4.get_ylim()
a4 = 1.0 * abs((xmin[0]-xmin[1])/(ymin[0]-ymin[1]))

ax1.set_aspect(a1*0.8,)
ax2.set_aspect(a2*0.8,)
ax3.set_aspect(a3*0.8,)
ax4.set_aspect(a4*0.8,)


#label des axes
#a
ax1.set_xlabel(r"$m_z$")
ax1.set_ylabel(r"$Energie$")
ax1.xaxis.set_ticklabels([])
ax1.yaxis.set_ticklabels([])

#b
ax2.set_xlabel(r"$B$ (T)")
ax2.set_ylabel(r"$E$ (K)")
ax2.xaxis.set_ticks([0.5,1.5,2.5])
ax2.yaxis.set_ticks([-20,-10,0,10])

#c
ax3.set_xlabel(r"$B$ (T)")
ax3.set_ylabel(r"$Energie$")
ax3.xaxis.set_ticklabels([])
ax3.yaxis.set_ticklabels([])

#d
ax4.set_xlabel(r"$B$ (T)")
ax4.set_ylabel(r"$M/M_{\rm{s}}$")
ax4.xaxis.set_ticks([-1,0,1])
ax4.yaxis.set_ticks([-1,0,1])

#label de la figure
fig.subplots_adjust(left=0.09,right=0.97,wspace=0.30,hspace=0.00, top = 0.98, bottom = 0.05)
fig.text(0.01,0.94,"a",fontsize=25,fontweight="bold")
fig.text(0.51,0.94,"b",fontsize=25,fontweight="bold")

fig.text(0.01,0.47,"c",fontsize=25,fontweight="bold")
fig.text(0.51,0.47,"d",fontsize=25,fontweight="bold")



fig.savefig("/home/hukadan/These/Manuscript/Spintronique/FigureFe8/FigureFe8.pdf")
close(fig)

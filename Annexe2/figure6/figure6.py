#on fait d'abord 3 subplot
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.patches import Polygon



gs1 = gridspec.GridSpec(1,1)
gs1.update(left=0.09,right=0.49,bottom=0.2)
ax1 = plt.subplot(gs1[:,:])

gs2 = gridspec.GridSpec(1,1)
gs2.update(left=0.51, right=0.98,hspace=0.1,bottom=0)
ax2 = plt.subplot(gs2[0,0])

fig = gcf()
fig.set_size_inches(12,5.5)



def T(x):
    return exp(x*(x+1))

X = linspace(-1,0,100)
Y = T(X)





#ax3.set_axis_off()
##############################
#PANEL 1
#On commence par le pannel 1
ax1.plot(X,Y)
ax1.set_xlabel(r"$\epsilon_0 / E_{\rm{c}}$")
ax1.set_ylabel(r"$T_{\rm{K}}(u.a)$")
ax1.yaxis.set_ticks([0.8,1])
ax1.xaxis.set_ticks([-1,-0.5,0])


###############################
##PANEL 2 parametres du probleme
ax2.set_xlim(0,1.2)
ax2.set_ylim(0,1)
ax2.set_axis_off()
lwb = 4
lwu = 3


ax2.plot([0.4,0.4],[0.2,0.8],linewidth=lwb,color="black")#1er barriere
ax2.plot([0.8,0.8],[0.2,0.8],linewidth=lwb,color="black")#1er barriere
ax2.plot([0.1,0.4],[0.5,0.5],linewidth=lwu,color="black")#mus
ax2.plot([0.8,1.1],[0.5,0.5],linewidth=lwu,color="black")#mud
ax2.plot([0.45,0.75],[0.25,0.25],linewidth=lwu,color="black")#mu(1)
ax2.plot([0.45,0.75],[0.75,0.75],linewidth=lwu,color="black")#mu(2)
#epsilon_0
ax2.plot([0.4,0.5],[0.5,0.5],linewidth=lwu,color="black",linestyle="--")
ax2.annotate("",(0.5,0.26),(0.5,0.49),ha="right",va="center",arrowprops=dict(arrowstyle='<|-|>',connectionstyle="arc3,rad=0",linewidth=2,color="black"))
ax2.annotate(r"$\epsilon_0$",(0.46,0.375),ha="center",va="center",fontsize=25)
#E_c
ax2.annotate("",(0.7,0.26),(0.7,0.74),ha="right",va="center",arrowprops=dict(arrowstyle='<|-|>',connectionstyle="arc3,rad=0",linewidth=2,color="black"))
ax2.annotate(r"$E_c$",(0.75,0.5),ha="center",va="center",fontsize=25)
#mu_s
ax2.annotate(r"$\mu_s$",(0.25,0.53),ha="center",va="center",fontsize=25)
#mu_d
ax2.annotate(r"$\mu_d$",(0.95,0.53),ha="center",va="center",fontsize=25)
#mu_(1)
ax2.annotate(r"$\mu (1)$",(0.6,0.28),ha="center",va="center",fontsize=25)
#mu_(2)1
ax2.annotate(r"$\mu (2)$",(0.6,0.78),ha="center",va="center",fontsize=25)

#Mise en page du plot
fig.text(0.01,0.95,"a",fontsize=25,fontweight="bold")#,backgroundcolor="#FF0000")
fig.text(0.51,0.95,"b",fontsize=25,fontweight="bold")#,backgroundcolor="m")

#Et voila
fig.savefig("Theorie/Transport/figure6/figure6.pdf")

#close(fig)

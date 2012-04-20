#on fait d'abord 3 subplot
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

gs1 = gridspec.GridSpec(1,1)
gs1.update(left=0.08,right=0.6)
ax1 = plt.subplot(gs1[:,:])

gs2 = gridspec.GridSpec(2,1)
gs2.update(left=0.65, right=0.98,hspace=0.1,bottom=0)
ax2 = plt.subplot(gs2[0,0])
ax3 = plt.subplot(gs2[1,0])

#ax1 = plt.subplot2grid((7,5),(0,0),colspan=3,rowspan=7)
#ax2 = plt.subplot2grid((7,5),(0,3),colspan=2,rowspan=3)
#ax3 = plt.subplot2grid((7,5),(3,3),colspan=2,rowspan=4)
fig = gcf()
fig.set_size_inches(12,7)









#ax3.set_axis_off()
##############################
#PANEL 1
#On commence par le pannel 1
ax1.plot([0,1],[0,1],'b')#bord de diamant
ax1.plot([-1,0],[1,0],'b')#bord de diaman
ax1.plot([-0.5,0.25],[1,0.25],'r')#niveau excite
ax1.plot([0.25,0.5],[0.25,0],'r--')#sous l'etat fondamental
ax1.plot([0.5,1],[0,0.5],'r--')#sous l'etat fondamental


#delta Ez
ax1.plot([-0.5,0.25],[0.25,0.25],color="black",linestyle='--')
ax1.annotate("",(-0.5,0.25),(-0.5,0),ha="center",va="center",arrowprops=dict(arrowstyle='<|-|>',connectionstyle="arc3,rad=0",linewidth=2,color="black"))
ax1.text(-0.620,0.125,r"$\Delta E_Z$",va="center",ha="center",fontsize=25, color='black')



ax1.xaxis.set_ticks([0,0.5])
ax1.xaxis.set_ticklabels(["$\mu_+(B)$","$\mu_{\minus}(B)$"], fontsize = 25)
ax1.yaxis.set_ticks([0,1])
ax1.set_xlabel(r"$V_{\rm{g}}(u.a)$")
ax1.set_ylabel(r"$V_{\rm{ds}}(u.a)$")
#une fleche pour l'influence du champ magnetique
ax1.annotate("",(-0.5,0.5),(-0.7,0.5),ha="center",va="center",arrowprops=dict(arrowstyle='<|-',connectionstyle="arc3,rad=0",linewidth=4,color="b"))
ax1.text(-0.6,0.45,"B",va="center",ha="center",fontsize=25,color = 'b')
#une deuxieme
ax1.annotate("",(0.0,0.5),(0.2,0.5),ha="center",va="center",arrowprops=dict(arrowstyle='<|-',connectionstyle="arc3,rad=0",linewidth=4,color="r"))
ax1.text(0.1,0.55,"B",va="center",ha="center",fontsize=25,color = 'r')



###############################
##PANEL 2 (diagramme Zeeman

ax2.plot([0,2],[0,1],'r') #up
ax2.plot([0,2],[0,-1],'b') #down
ax2.set_xlim(-0.2,2.2)
ax2.set_ylim(-1.5,1.5)
ax2.yaxis.set_ticks([-1,0,1])
ax2.set_xlabel(r"$B(u.a.)$")
ax2.set_ylabel(r"$E(u.a.)$")
ax2.set_axis_off()
#on met l'echelle des energie
ax2.annotate("",(0,1.2),(0,-1.2),ha="right",va="center",arrowprops=dict(arrowstyle='-|>',connectionstyle="arc3,rad=0",linewidth=2,color="black"))
ax2.text(-0.15,0.90,"$E$",fontsize=20,va="center",ha="center")
#on met le champs magnetique
ax2.annotate("",(2.2,0),(0,0),ha="right",va="center",arrowprops=dict(arrowstyle='-|>',connectionstyle="arc3,rad=0",linewidth=2,color="black"))
ax2.text(2,-0.35,"$B$",fontsize=20,va="center",ha="center")

#on met Dela Ez
ax2.annotate("",(1.2,0.6),(1.2,-0.6),ha="right",va="center",arrowprops=dict(arrowstyle='<|-|>',connectionstyle="arc3,rad=0",linewidth=2,color="black"))
ax2.text(1.55,0.3,r"$\Delta E_Z$",va="center",ha="center",fontsize=25, color='black')



###############
##Panel 3
ax3.set_xlim(0,1)
ax3.set_ylim(0,1)
ax3.xaxis.set_ticks([])
ax3.yaxis.set_ticks([])
ax3.set_axis_off()
#On separe N=0 et N=1
ax3.text(0.1,0.35,"$N=0$",fontsize=20,va="center",ha="center")
ax3.text(0.1,0.55,"$N=1$",fontsize=20,va="center",ha="center")
ax3.plot([0.1,0.9],[0.45,0.45],'-.', color="black")

#on met l'echelle des energie
ax3.annotate("",(0.5,0.9),(0.5,0.1),ha="right",va="center",arrowprops=dict(arrowstyle='-|>',connectionstyle="arc3,rad=0",linewidth=2,color="black"))
ax3.text(0.45,0.90,"$E$",fontsize=20,va="center",ha="center")

#pour B=0
ax3.text(0.15,0.9,"$B=0$",fontsize=20,va="center",ha="center")
ax3.plot([0.2,0.4],[0.2,0.2],color="black") #N=0
ax3.plot([0.2,0.4],[0.7,0.7],color="black")

#puis on met les spins
#up
ax3.annotate("",(0.32,0.8),(0.32,0.65),ha="right",va="center",arrowprops=dict(arrowstyle='-|>',connectionstyle="arc3,rad=0",linewidth=2,color="black"))
#down
ax3.annotate("",(0.28,0.60),(0.28,0.75),ha="right",va="center",arrowprops=dict(arrowstyle='-|>',connectionstyle="arc3,rad=0",linewidth=2,color="black"))

#on relie les etats par des pointilles
ax3.plot([0.4,0.6],[0.7,0.8],color='black',linestyle='--')
ax3.plot([0.4,0.6],[0.7,0.6],color='black',linestyle='--')

#pour B>0
ax3.text(0.85,0.9,"$B>0$",fontsize=20,va="center",ha="center")
ax3.plot([0.6,0.8],[0.2,0.2],color="black") #N=0
ax3.plot([0.6,0.8],[0.6,0.6],'b') #down
ax3.plot([0.6,0.8],[0.8,0.8],'r') #up


#puis on met les spins
#up
ax3.annotate("",(0.7,0.9),(0.7,0.75),ha="right",va="center",arrowprops=dict(arrowstyle='-|>',connectionstyle="arc3,rad=0",linewidth=2,color="black"))
#down
ax3.annotate("",(0.7,0.50),(0.7,0.65),ha="right",va="center",arrowprops=dict(arrowstyle='-|>',connectionstyle="arc3,rad=0",linewidth=2,color="black"))


#Ensuite des transitions
ax3.annotate("",(0.8,0.2),(0.8,0.8),ha="right",va="center",arrowprops=dict(arrowstyle='<|-',connectionstyle="arc3,rad=-0.25",linewidth=2,color="red"))
ax3.annotate("",(0.8,0.2),(0.8,0.6),ha="right",va="center",arrowprops=dict(arrowstyle='<|-',connectionstyle="arc3,rad=-0.2",linewidth=2,color="blue"))
ax3.set_xlim(0,0.9)


#Mise en page du plot
fig.text(0.01,0.95,"a",fontsize=25,fontweight="bold")#,backgroundcolor="#FF0000")
fig.text(0.62,0.95,"b",fontsize=25,fontweight="bold")#,backgroundcolor="m")
fig.text(0.62,0.45,"c",fontsize=25,fontweight="bold")#,backgroundcolor="m")

#Et voila
fig.savefig("Theorie/Transport/figure4/figure4.pdf")

#close(fig)

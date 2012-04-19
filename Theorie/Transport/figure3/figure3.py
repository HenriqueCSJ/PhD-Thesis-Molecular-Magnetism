execfile("Transport/CB_classique.py")
fig =figure()
fig.set_size_inches(12,5.5)
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
ax1.set_aspect(0.9)
ax2.set_aspect(0.9)
ax = ax1
#on dessine le diamant
ax.plot([-1,1],[-1,1])
ax.plot([-1,1],[1,-1])
ax.set_xlabel(r"$V_{\rm{g}} (u.a.)$")
ax.set_ylabel(r"$V_{\rm{ds}} (u.a.)$")

#on regle le style des fleches
arrowpropsleft=dict(arrowstyle='->',connectionstyle="arc3,rad=0.5")
arrowpropsright=dict(arrowstyle='->',connectionstyle="arc3,rad=-0.5")

#on dessine le premier diagramme de potentiel chimique
ax.text(-0.6,0.25,"Situation 1",ha="center",va="center")
ax.plot([-0.89,-0.71],[0.,0.],'black') #mu source
ax.plot([-0.69,-0.51],[0.1,0.1],'black') #mu dot
ax.plot([-0.49,-0.31],[0.,0.],'black') #mu drain
ax.plot(linspace(-0.7,-0.7,10),linspace(-0.2,0.2,10),'black',linestyle='-') #left barrier
ax.plot(linspace(-0.5,-0.5,10),linspace(-0.2,0.2,10),'black',linestyle='-') #right barrier
ax.annotate("",(-0.8,0.05),(-0.61,0.15),arrowprops=arrowpropsleft)
ax.annotate("",(-0.4,0.05),(-0.59,0.15),arrowprops=arrowpropsright)


#on dessine le deuxieme diagramme de potentiel chimique
offset1 = 1.2
ax.text(-0.6+offset1,0.25,"Situation 2",ha="center",va="center")
ax.plot([-0.89+offset1,-0.71+offset1],[0.,0.],'black') #mu source
ax.plot([-0.69+offset1,-0.51+offset1],[-0.1,-0.1],'black') #mu dot
ax.plot([-0.49+offset1,-0.31+offset1],[0.,0.],'black') #mu drain
ax.plot(linspace(-0.7+offset1,-0.7+offset1,10),linspace(-0.2,0.2,10),'black',linestyle='-') #left barrier
ax.plot(linspace(-0.5+offset1,-0.5+offset1,10),linspace(-0.2,0.2,10),'black',linestyle='-') #right barrier
ax.annotate("",(-0.61+offset1,-0.05),(-0.8+offset1,0.05),arrowprops=arrowpropsright)
ax.annotate("",(-0.59+offset1,-0.05),(-0.4+offset1,0.05),arrowprops=arrowpropsleft)

#on dessine le troisieme diagramme de potentiel chimique
offset1 = 0.6
offset2 = 0.6
ax.text(-0.6+offset1,0.25+offset2,"Situation 4",ha="center",va="center")
ax.plot([-0.89+offset1,-0.71+offset1],[0.1+offset2,0.1+offset2],'black') #mu source
ax.plot([-0.69+offset1,-0.51+offset1],[0.0+offset2,0.0+offset2],'black') #mu dot
ax.plot([-0.49+offset1,-0.31+offset1],[-0.1+offset2,-0.1+offset2],'black') #mu drain
ax.plot(linspace(-0.7+offset1,-0.7+offset1,10),linspace(-0.2+offset2,0.2+offset2,10),'black',linestyle='-') #left barrier
ax.plot(linspace(-0.5+offset1,-0.5+offset1,10),linspace(-0.2+offset2,0.2+offset2,10),'black',linestyle='-') #right barrier
ax.annotate("",(-0.61+offset1,0.05+offset2),(-0.8+offset1,0.15+offset2),arrowprops=arrowpropsright)
ax.annotate("",(-0.4+offset1,-0.05+offset2),(-0.59+offset1,0.05+offset2),arrowprops=arrowpropsright)


#on dessine le quatrieme diagramme de potentiel chimique
offset1 = 0.6
offset2 = -0.6
ax.text(-0.6+offset1,0.25+offset2,"Situation 3",ha="center",va="center")
ax.plot([-0.89+offset1,-0.71+offset1],[-0.1+offset2,-0.1+offset2],'black') #mu source
ax.plot([-0.69+offset1,-0.51+offset1],[0.0+offset2,0.0+offset2],'black') #mu dot
ax.plot([-0.49+offset1,-0.31+offset1],[0.1+offset2,0.1+offset2],'black') #mu drain
ax.plot(linspace(-0.7+offset1,-0.7+offset1,10),linspace(-0.2+offset2,0.2+offset2,10),'black',linestyle='-') #left barrier
ax.plot(linspace(-0.5+offset1,-0.5+offset1,10),linspace(-0.2+offset2,0.2+offset2,10),'black',linestyle='-') #right barrier
ax.annotate("",(-0.8+offset1,-0.05+offset2),(-0.61+offset1,0.05+offset2),arrowprops=arrowpropsleft)
ax.annotate("",(-0.59+offset1,0.05+offset2),(-0.4+offset1, 0.15+offset2),arrowprops=arrowpropsleft)

################
##plot de droite
di = dI_Vg_dVds(-0.001,0.001,500,-0.002,0.002,500,1,2,1,20e9,20e9,0,0.4)
imdi = ax2.imshow(matrix(di).transpose().tolist(),extent=[-1,1,-1,1],aspect = 0.9,cmap='hot')
ax2.set_xlabel(r"$V_{\rm{g}} (a.u.)$")
ax2.set_ylabel(r"$V_{\rm{ds}} (a.u.)$")
ax2.text(-0.75,0,"N",fontsize=30,ha='center',va='center', color="white")
ax2.text(0.75,0,"N+1",fontsize=30,ha='center',va='center', color="white")
ax2.text(0,-0.75,"N/N+1",fontsize=30,ha='center',va='center', color="white")
ax2.text(0,0.75,"N/N+1",fontsize=30,ha='center',va='center', color="white")
#Mise en page du plot
fig.subplots_adjust(left=0.09,right=0.97,wspace=0.35)
fig.text(0.01,0.95,"a",fontsize=25,fontweight="bold",backgroundcolor="pink")
fig.text(0.51,0.95,"b",fontsize=25,fontweight="bold",backgroundcolor="pink")
#On trace le tout
draw()
fig.savefig("Theorie/Transport/figure3/figure3.pdf")

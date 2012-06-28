#figure 1 du resultat/chap1


fig = figure()
fig.set_size_inches(6,5)
ax = fig.add_subplot(111)
ax.set_axis_off()

#on regle le style des fleches
arrowpropsleft=dict(arrowstyle='-|>',connectionstyle="arc3,rad=0.0",linewidth=3,color="blue")
arrowpropsright=dict(arrowstyle='-|>',connectionstyle="arc3,rad=-0.0",linewidth=3,color="blue")
arrowpropsboth=dict(arrowstyle='<|-|>',connectionstyle="arc3,rad=-0.0",linewidth=1,color="black")
arrowpropsrightbis=dict(arrowstyle='-|>',connectionstyle="arc3,rad=-0.0",linewidth=3,color="black")



#Configuration generale
ax.plot([0,1],[0,1],'--',color='gray')
ax.set_xlim(-1,2)
ax.set_ylim(-2,1.5)
ax.annotate("",(-0.25,0.25),(0.25, -0.25),ha="center",va="center",arrowprops=arrowpropsright)
ax.annotate("",(0.1+1,0.25+1),(-0.1+1, -0.25+1),ha="center",va="center",arrowprops=arrowpropsright)
ax.annotate("",(0.65, 0.65),(0.35,0.35),ha="center",va="center",arrowprops=arrowpropsrightbis)


#Configuration anti-ferro
ax.annotate("",(-0.5,-1.1),(-0.5,-1.9),ha="center",va="center",arrowprops=arrowpropsright)
ax.annotate("",(0,-1.75),(0,-1.25),ha="center",va="center",arrowprops=arrowpropsright)

#Configuration ferro
ax.annotate("",(1.25,-1.1),(1.25,-1.9),ha="center",va="center",arrowprops=arrowpropsright)
ax.annotate("",(1.25,-0.35),(1.25,-0.85),ha="center",va="center",arrowprops=arrowpropsright)



fig.subplots_adjust(left=0.,right=1,wspace=0.,hspace=0.00, top = 1, bottom = 0)
fig.savefig("/home/hukadan/These/Manuscript/Resultats/Chap1/Figure1/figure1.pdf")
close(fig)
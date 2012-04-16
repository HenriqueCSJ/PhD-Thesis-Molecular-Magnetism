execfile("Transport/CB_classique.py")
fig = figure()
fig.set_size_inches(8.5,4.5)
###############
#creation de deux plots

ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
################
################
##plot de gauche
cur = I_Vg_Vds(-0.001,0.001,300,-0.002,0.002,250,1,2,1,20e9,20e9,0,0.4)
imcur = ax1.imshow(matrix(cur).transpose().tolist())
ax1.set_xlabel(r"$V_{\rm{g}} (a.u.)$")
ax1.set_ylabel(r"$V_{\rm{ds}} (a.u.)$")
ax1.xaxis.set_ticklabels([])
ax1.yaxis.set_ticklabels([])
#mise en forme de la colorbar
col1 = colorbar(imcur, ax=ax1,orientation = 'horizontal')
col1.ax.xaxis.set_label_position('top')
col1.ax.set_xlabel(r"$Current (a.u)$", size = 15, va = 'bottom')
posax = array(ax1.get_position())[0][0]
posay = array(ax1.get_position())[0][1]
col1.ax.set_aspect(0.08)
col1.ax.set_position([posax,posay-0.02,0.1,0.2])
col1.ax.xaxis.set_ticks([0,0.5,1])
col1.ax.xaxis.set_ticklabels(["$\minus$","","+"])
draw()
posax = array(ax1.get_position())[0][0]
posay = array(ax1.get_position())[0][1]
col1.ax.set_position([posax,posay-0.3,0.1,0.2])




################
##plot de droite
di = dI_Vg_dVds(-0.001,0.001,300,-0.002,0.002,250,1,2,1,20e9,20e9,0,0.4)
imdi = ax2.imshow(matrix(di).transpose().tolist())
ax2.set_xlabel(r"$V_{\rm{g}} (a.u.)$")
#ax2.set_ylabel(r"$V_{\rm{ds}} (a.u.)$")
ax2.xaxis.set_ticklabels([])
ax2.yaxis.set_ticklabels([])
#mise en forme de la colorbar
col2 = colorbar(imcur, ax=ax2,orientation = 'horizontal')
col2.ax.xaxis.set_label_position('top')
col2.ax.set_xlabel(r"$dI/dV (a.u)$", size = 15, va = 'bottom')
posax = array(ax2.get_position())[0][0]
col2.ax.set_aspect(0.08)
col2.ax.set_position([posax,0.08,0.1,0.2])
col2.ax.xaxis.set_ticks([0,1])
col2.ax.xaxis.set_ticklabels(["low","high"])
draw()

#test
col1.ax.xaxis.set_ticks([0,0.5,1])
col1.ax.xaxis.set_ticklabels(["$\minus$","","+"])
##set aspect of ax
ax1.set_aspect("auto")
ax2.set_aspect("auto")


##Mise en page de la figure
#fig.subplots_adjust(hspace=0.0)
#fig.subplots_adjust(top=0.98)
fig.subplots_adjust(bottom=0.21)
fig.subplots_adjust(left=0.08)
fig.subplots_adjust(right=0.99)
fig.subplots_adjust(wspace=0)

#ajsute les colorbar
posax = array(ax1.get_position())[0][0]
col1.ax.set_aspect(0.08)
col1.ax.set_position([posax,0,0.1,0.12])

posax = array(ax2.get_position())[0][0]
col2.ax.set_aspect(0.08)
col2.ax.set_position([posax,0,0.1,0.12])
#sauvegarde de la figure
fig.savefig("Theorie/Transport/figure4/figure4.pdf")

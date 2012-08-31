#from setproc.cycle_process.classes.cycle_process import CycleProcess
#Cyc16 = CycleProcess("G_B_trace.json","G_B_retrace.json",[0,1,2,3,4,5,6],"Json")

#Cyc16.GetStat(250,4)
Cyc16.SetPlotCalibration([10**1.4,10**4,[-0.2,0.2],-0.019])


fig =figure()
fig.set_size_inches(12,16)
ax1 = fig.add_subplot(321)
ax2 = fig.add_subplot(322)
ax3 = fig.add_subplot(323)
ax4 = fig.add_subplot(324)
ax5 = fig.add_subplot(325)
ax6 = fig.add_subplot(326)


#on fait la stat aller plus retour
stat_trace = []
stat_retrace =[]
seuil_stat = 10




for x in Cyc16["detection"] :
	if x.trace and x.Superior(seuil_stat) :
		stat_trace.append(x.field)
	elif x.Superior(seuil_stat) :
		stat_retrace.append(x.field)

t_offset = 0.025
r_offset = 0.0109
ax1.hist(array(stat_trace)-t_offset,200)
ax2.hist(array(stat_retrace)-r_offset,200)


#On analyse les doubles sauts
Cyc16.GetDouble(10**1.4,10**4,-0.019)
td0 = Cyc16["double"]["trace"][0]
td1 = Cyc16["double"]["trace"][1]

ax3.hist(array(td0) - t_offset, 150)  
ax5.hist(array(td1) - t_offset, 150)

rd0 = Cyc16["double"]["retrace"][0]
rd1 = Cyc16["double"]["retrace"][1]

ax4.hist(array(rd0) - r_offset, 150)  
ax6.hist(array(rd1) - r_offset, 150)


#Mise en page
ax1.set_xlim(-0.25,0.25)
ax1.set_ylim(0,600)
ax1.xaxis.set_ticks([])
ax1.yaxis.set_ticks([100,300,500])

ax2.set_xlim(-0.25,0.25)
ax2.set_ylim(0,600)
ax2.xaxis.set_ticks([])
ax2.yaxis.set_ticks([])

ax3.set_xlim(-0.25,0.25)
ax3.set_ylim(0,140)
ax3.xaxis.set_ticks([])
ax3.yaxis.set_ticks([40,80,120])

ax4.set_xlim(-0.25,0.25)
ax4.set_ylim(0,140)
ax4.xaxis.set_ticks([])
ax4.yaxis.set_ticks([])

ax5.set_xlim(-0.25,0.25)
ax5.set_ylim(0,80)
ax5.xaxis.set_ticks([-0.15,-0.05,0.05,0.15])
ax5.yaxis.set_ticks([20,40,60])

ax6.set_xlim(-0.25,0.25)
ax6.set_ylim(0,80)
ax6.xaxis.set_ticks([-0.15,-0.05,0.05,0.15])
ax6.yaxis.set_ticks([])

ax3.set_ylabel(r"Counts")
ax5.set_xlabel(r"$B$ (T)")
ax6.set_xlabel(r"$B$ (T)")

ax1.text(0.05, 0.95,'a', fontsize = 30, horizontalalignment='center', verticalalignment='center', transform = ax1.transAxes)
ax2.text(0.05, 0.95,'b', fontsize = 30, horizontalalignment='center', verticalalignment='center', transform = ax2.transAxes)
ax3.text(0.05, 0.95,'c', fontsize = 30, horizontalalignment='center', verticalalignment='center', transform = ax3.transAxes)
ax4.text(0.05, 0.95,'d', fontsize = 30, horizontalalignment='center', verticalalignment='center', transform = ax4.transAxes)
ax5.text(0.05, 0.95,'e', fontsize = 30, horizontalalignment='center', verticalalignment='center', transform = ax5.transAxes)
ax6.text(0.05, 0.95,'f', fontsize = 30, horizontalalignment='center', verticalalignment='center', transform = ax6.transAxes)

fig.subplots_adjust(left=0.09,right=0.97,wspace=0, hspace=0,top=0.99,bottom=0.05)
fig.savefig("/home/hukadan/These/Manuscript/Resultats/TransInd/Scripts/cyc16ext.pdf")
close(fig)
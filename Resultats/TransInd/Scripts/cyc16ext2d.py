#from setproc.cycle_process.classes.cycle_process import CycleProcess
#Cyc16 = CycleProcess("G_B_trace.json","G_B_retrace.json",[0,1,2,3,4,5,6],"Json")

#Cyc16.GetStat(250,4)
Cyc16.SetPlotCalibration([10**1.4,10**4,[-0.2,0.2],-0.019])


fig =figure()
fig.set_size_inches(12,16.8)
ax1 = fig.add_subplot(321)
ax2 = fig.add_subplot(322)
ax3 = fig.add_subplot(323)
ax4 = fig.add_subplot(324)
ax5 = fig.add_subplot(325)
ax6 = fig.add_subplot(326)


t_offset = 0.025
r_offset = 0.0109


#On analyse les doubles sauts
Cyc16.GetDouble(10**1.4,10**4,-0.019)

td0 = Cyc16["double"]["trace"][0]
td1 = Cyc16["double"]["trace"][1]

ax1.hist(array(td0) - t_offset, 150)  
ax3.hist(array(td1) - t_offset, 150)

rd0 = Cyc16["double"]["retrace"][0]
rd1 = Cyc16["double"]["retrace"][1]

ax2.hist(array(rd0) - r_offset, 150)  
ax4.hist(array(rd1) - r_offset, 150)

HT = histogram2d(array(td1)-t_offset, array(td0)-t_offset, 200, range = [[-0.195,0.195],[-0.195,0.195]])
HR = histogram2d(array(rd1)-r_offset, array(rd0)-r_offset, 200, range = [[-0.195,0.195],[-0.195,0.195]])

ax5.imshow(HT[0],extent=[-0.195,0.195,-0.195,0.195])
ax6.imshow(HR[0],extent=[-0.195,0.195,-0.195,0.195])
ax5.set_aspect("auto")
ax6.set_aspect("auto")





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

xmin= ax5.get_xlim()
ymin= ax5.get_ylim()
a5 = 1.0 * abs((xmin[0]-xmin[1])/(ymin[0]-ymin[1]))

xmin= ax6.get_xlim()
ymin= ax6.get_ylim()
a6 = 1.0 * abs((xmin[0]-xmin[1])/(ymin[0]-ymin[1]))
"""
ax1.set_aspect(a1)
ax2.set_aspect(a2)
ax3.set_aspect(a3)
ax4.set_aspect(a4)
ax5.set_aspect(a5)
ax6.set_aspect(a6)
"""

ax1.set_xlim(-0.195,0.195)
ax1.set_ylim(0,140)
ax1.xaxis.set_ticklabels([])
ax1.yaxis.set_ticks([40,80,120])

ax2.set_xlim(-0.195,0.195)
ax2.set_ylim(0,140)
ax2.xaxis.set_ticklabels([])
ax2.yaxis.set_ticks([])

ax3.set_xlim(-0.195,0.195)
ax3.set_ylim(0,80)
ax3.xaxis.set_ticklabels([])
ax3.yaxis.set_ticks([20,40,60])

ax4.set_xlim(-0.195,0.195)
ax4.set_ylim(0,80)
ax4.xaxis.set_ticklabels([])
ax4.yaxis.set_ticks([])

ax5.set_xlim(-0.195,0.195)
ax5.set_ylim(-0.195,0.195)
#ax5.xaxis.set_ticks([])
#ax5.yaxis.set_ticks([])

ax6.set_ylim(-0.195,0.195)
ax6.set_xlim(-0.195,0.195)
#ax5.xaxis.set_ticks([])
ax6.yaxis.set_ticks([])

ax1.set_ylabel(r"Counts")
ax3.set_ylabel(r"Counts")
ax5.set_ylabel(r"$B$ (T)")
ax5.set_xlabel(r"$B$ (T)")
ax6.set_xlabel(r"$B$ (T)")


fig.subplots_adjust(left=0.09,right=0.97,wspace=0, hspace=0,top=0.99,bottom=0.05)


fig.savefig("/home/hukadan/These/Manuscript/Resultats/TransInd/Scripts/cyc16ext2d.pdf")
close(fig)
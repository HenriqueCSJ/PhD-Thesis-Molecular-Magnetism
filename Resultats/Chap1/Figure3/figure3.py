#On charge les librairies
import matplotlib.gridspec as gridspec
import os
#locale
sys.path.append("/home/hukadan/These/")
from setproc.cycle_process.classes.cycle_process import CycleProcess
from setproc.sweep_set.functions.filter import filter
execfile("/home/hukadan/These/Manuscript/Theorie/MagMol/scripts/TbPc2Nuclear.py")

#On prepare les figures
#premiere grid pour step et pics
gs1 = gridspec.GridSpec(2,1)
gs1.update(left=0.015, right=0.45,hspace=0,bottom=0.55, top=1)
ax1 = plt.subplot(gs1[0,0])
ax2 = plt.subplot(gs1[1,0])
#Pour la stat des sauts
gs2 = gridspec.GridSpec(2,1)
gs2.update(left=0.015, right=0.45,hspace=0.1,bottom=0.1, top=0.45)
ax3 = plt.subplot(gs2[:,:])
#Pour les resonances
gs3 = gridspec.GridSpec(2,1)
gs3.update(left=0.55, right=0.95,hspace=0,bottom=0.1, top=1)
ax4 = plt.subplot(gs3[0,0])
ax5 = plt.subplot(gs3[1,0])

fig = gcf()
fig.set_size_inches(12,7)


#On charge les donnee
os.chdir("/media/Iomega_HDD/Measures/Tb2C/sample3/6R/J9/Cycle/Cycle16/")
#Cyc16 = CycleProcess("G_B_trace.json","G_B_retrace.json",[0,1,2,3,4,5,6],"Json")
#Cyc16.GetStat(150,4)


#panel a et b
#coube exemple
p1 = Cyc16.trace["data"][17]
p2 = Cyc16.trace["data"][76]
bias = Cyc16.trace['bias']
p1f = filter(array(p1),4,1,1)
p2f = filter(array(p2),4,1,1)
biasf = bias[6:]

ax1.plot(bias, p1)
ax1.plot(bias, p2)
ax2.plot(biasf, p1f)
ax2.plot(biasf, p2f)
ax1.set_xlim(-0.1,0.1)
ax1.set_ylim(1.88e-6,1.91e-6)
ax2.set_xlim(-0.1,0.1)
ax2.set_ylim(-2e-29,1e-29)

#panel c
#stat des sauts
statvalue = []
for x in Cyc16['detection'] :
	statvalue.append(log10(abs(x.value)))
tr0 = Polygon([[-29.5,0],[-31.5,0],[-31.5,700],[-29.5,700]], color="#C0C0C0")
ax3.add_patch(tr0)
ax3.hist(statvalue,200)
ax3.plot([-29.5,-29.5],[0,700],'--',color='gray')

#panel d
#Zeeman
#R = Tb_Pc2_ZeemanNuclear(-0.1,0.1,250,0,0)
#B = linspace(-0.1,0.1,250)
ax4.plot(B,R,color="red")
ax4.set_xlim(-0.05,0.05)
ax4.set_ylim(-645.1,-644)

#panel e
stat_tr = []
for x in Cyc16["detection"] :
    if x.trace :
        stat_tr.append(x.field-0.0234) #on compense l'offset lockin

ax5.hist(stat_tr,700)
ax5.set_xlim(-0.05,0.05)
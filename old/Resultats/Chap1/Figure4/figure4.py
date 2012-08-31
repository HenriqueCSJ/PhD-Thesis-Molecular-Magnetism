#On charge les librairies
import matplotlib.gridspec as gridspec
import os
#locale
sys.path.append("/home/hukadan/These/")
from setproc.cycle_process.classes.cycle_process import CycleProcess

#on charge les donnees
os.chdir("/media/Iomega_HDD/Measures/Tb2C/sample3/6R/J9/Cycle/Cycle30/")
#Cyc15 = CycleProcess("G_B_trace.json","G_B_retrace.json",[0,1,2,3,4,5,6,7,8,9],"Json")
#Cyc15.GetStat(250,4)
Cyc15.SetPlotCalibration([10**-30,10**-25,[-0.1,0.1],0.3])
Cyc15.SortData()

#pour les courbes
bias = Cyc15.trace["bias"]
cup = Cyc15.trace["data"][9]
cdo = Cyc15.trace["data"][1]
#pour la stat
tup = []
tdo = []
for x in Cyc15["sort"]["trace"]["up"][1]:
    tup.append(x-0.02)
    
for x in Cyc15["sort"]["trace"]["down"][1]:
    tdo.append(x-0.02)
    

#on preprare les figure
fig = figure()
fig.set_size_inches(12,8)
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

#panel des courbes
ax1.plot(bias,cup,"b")
ax3.plot(bias,cdo,"g")
ax1.set_xlim(-0.075,0.075)
ax3.set_xlim(-0.075,0.075)

#panel stat
nbr=120
ax2.hist(tup,nbr)
ax2.set_xlim(-0.075,0.075)
figure()
ax4.hist(tdo,nbr)
ax4.set_xlim(-0.075,0.075)



#A la fin on met en page
fig.subplots_adjust(left=0.09,right=0.97,wspace=0.2,hspace=0.0,bottom=0.1,top=0.95)

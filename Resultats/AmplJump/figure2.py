#On charge la librarie
import os
os.chdir("/media/Iomega_HDD/Measures/Tb2C/sample3/5R/J9/Cycle17/")
sys.path.append("/home/hukadan/These")

from setproc.cycle_process.classes.cycle_process import CycleProcess
Cyc16 = CycleProcess("G_B_trace.json","G_B_retrace.json",[""],"Json")




#on fait les figures
fig = figure()
fig.set_size_inches(12,10)
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

bias = Cyc16.trace["bias"]

#figure a
y = Cyc16.trace["data"][102]
ax1.plot(bias,y)
ax1.set_xlim(-0.4,0.4)
ax1.set_ylim(1.26e-6,1.44e-6)
ax1.plot([-0.05,-0.05],[1.26e-6,1.44e-6],'--', color="green")
ax1.plot([0.05,0.05],[1.26e-6,1.44e-6],'--', color="green")
ax1.text(-0.225,1.42e-6,r"$\frac{\partial G}{\partial B} = cst$",fontsize=25,va="center",ha="center")
ax1.text(0.225,1.42e-6,r"$\frac{\partial G}{\partial B} = cst$",fontsize=25,va="center",ha="center")
tr0 = Polygon([[-0.05,1.26e-6],[-0.05,1.44e-6],[0.05,1.44e-6],[0.05,1.26e-6]], color="#C0C0C0")
ax1.add_patch(tr0)

#figure b

y1 = Cyc16.trace["data"][123]
y2 = Cyc16.trace["data"][128]
y3 = Cyc16.trace["data"][131]
ax2.plot(bias,y1)
ax2.plot(bias,y2)
ax2.plot(bias,y3)
ax2.set_xlim(-0.4,0.4)
ax2.set_ylim(1.26e-6,1.44e-6)


#figure c
#en attente

#figure d
extent = [-3,3,-1-0.034,1-0.034] #compensation de l'offset
os.chdir("/media/Iomega_HDD/Measures/Tb2C/sample3/7R/J9/MapB_Kondo_1/Hy2")
from setproc.map.classes.map import Map
Map1 = Map("Map_B_angle.json","Vds","Vds")
data = Map1["data"]
ax4.contour(data,100,extent=extent)
ax4.plot([-0.35,3],[0,0.376],"--", color="black")
ax4.plot([-0.35,3],[0,-0.376],"--", color="black")
ax4.plot([-0.35,-.35],[0,-0.5],"--", color="black")
ax4.set_ylim(-0.5,0.5)
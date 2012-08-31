#On charge la librarie
import os
os.chdir("/media/Iomega_HDD/Measures/Tb2C/sample3/6R/J9/Cycle/Cycle16/")
sys.path.append("/home/hukadan/These")

from setproc.cycle_process.classes.cycle_process import CycleProcess
Cyc16 = CycleProcess("G_B_trace.json","G_B_retrace.json",[0,1,2,3,4,5,6],"Json")
Cyc16.GetStat(150,4)
















#panel c
stat_value = []
for x in Cyc16["detection"] :
	stat_value.append(abs(x.value))
stat_value = array(stat_value)
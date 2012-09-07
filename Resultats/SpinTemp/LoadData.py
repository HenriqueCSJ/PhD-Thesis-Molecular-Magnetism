# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

sys.path.append("/home/hukadan/These/")
from setproc.cycle_process.classes.cycle_process import CycleProcess
from setproc.common.functions.local_extrema import local_extrema
import os

# <codecell>

os.chdir("/media/Iomega_HDD/Measures/Tb2C/sample3/6R/J9/Cycle/Second_Dege/second_VG/Cycle1/");
#Cyc1 = CycleProcess("G_B_trace.json","G_B_retrace.json",[0,1,2,3,4,5,6,7,8,9],"Json");
Cyc1 = CycleProcess("Cyc1fig.bin")
Cyc1.LoadSweeps()

# <codecell>

#Cyc1.GetStat(150,4)
Cyc1.GetValueStat()

# <codecell>

Cyc1.SetPlotCalibration([10**-32,10**-28,[-0.085,0.085],-0.019])
#Cyc1.SaveAll("tracefigure","retracefigure","Cyc1fig.bin")

# <codecell>

os.chdir("/media/Iomega_HDD/Measures/Tb2C/sample3/6R/J9/Cycle/Second_Dege/second_VG/Cycle2/");
#Cyc2 = CycleProcess("G_B_trace.json","G_B_retrace.json",[0,1,2,3,4,5,6,7,8,9,10],"Json");
Cyc2 = CycleProcess("Cyc2fig.bin")
Cyc2.LoadSweeps()

# <codecell>

Cyc2.GetStat(150,4)
Cyc2.GetValueStat()

# <codecell>

Cyc2.SetPlotCalibration([10**-32,10**-28,[-0.085,0.085],-0.019])
#Cyc2.SaveAll("tracefigure","retracefigure","Cyc2fig.bin")

# <codecell>

os.chdir("/media/Iomega_HDD/Measures/Tb2C/sample3/6R/J9/Cycle/Second_Dege/second_VG/Cycle3/");
#Cyc3 = CycleProcess("G_B_trace.json","G_B_retrace.json",[0,1,2,3,4,5,6,7,8,9],"Json");
Cyc3 = CycleProcess("Cyc3fig.bin")
Cyc3.LoadSweeps()

# <codecell>

#Cyc3.GetStat(150,4)
Cyc3.GetValueStat()

# <codecell>

Cyc3.SetPlotCalibration([10**-32,10**-28,[-0.085,0.085],-0.019])
#Cyc3.SaveAll("tracefigure","retracefigure","Cyc3fig.bin")

# <codecell>

os.chdir("/media/Iomega_HDD/Measures/Tb2C/sample3/6R/J9/Cycle/Second_Dege/second_VG/Cycle4/");
#Cyc4 = CycleProcess("G_B_trace.json","G_B_retrace.json",[0,1,2,3,4,5,6,7,8,9,10],"Json");
Cyc4 = CycleProcess("Cyc4fig.bin")
Cyc4.LoadSweeps()

# <codecell>

Cyc4.GetStat(150,4)
Cyc4.GetValueStat()

# <codecell>

Cyc4.SetPlotCalibration([10**-32,10**-28,[-0.085,0.085],-0.019])
#Cyc4.SaveAll("tracefigure","retracefigure","Cyc4fig.bin")

# <codecell>

os.chdir("/media/Iomega_HDD/Measures/Tb2C/sample3/6R/J9/Cycle/Second_Dege/second_VG/Cycle5/");
#Cyc5 = CycleProcess("G_B_trace.json","G_B_retrace.json",[0,1,2,3,4,5,6,7,8,9,10],"Json");
Cyc5 = CycleProcess("Cyc5fig.bin")
Cyc5.LoadSweeps()

# <codecell>

#Cyc5.GetStat(150,4)
Cyc5.GetValueStat()

# <codecell>

Cyc5.SetPlotCalibration([10**-32,10**-28,[-0.085,0.085],-0.019])
#Cyc5.SaveAll("tracefigure","retracefigure","Cyc5fig.bin")

# <codecell>

Cyc1.SortData()
Cyc2.SortData()
Cyc3.SortData()
Cyc4.SortData()
Cyc5.SortData()

# <codecell>

os.chdir("/media/Iomega_HDD/Measures/Tb2C/sample3/6R/J9/Cycle/Second_Dege/second_VG/etud_temp/T_200mK/Cycle1");
#CycT200 = CycleProcess("G_B_trace.json","G_B_retrace.json",[0,1,2,3,4,5,6,7,8,9,10],"Json");
CycT200 = CycleProcess("CycT200fig.bin")
CycT200.LoadSweeps()

# <codecell>

CycT200.GetStat(250,4)
CycT200.GetValueStat()

# <codecell>

CycT200.SetPlotCalibration([10**-32,10**-28,[-0.085,0.085],-0.019])
CycT200.SaveAll("tracefigure","retracefigure","CycT200fig.bin")

# <codecell>

os.chdir("/media/Iomega_HDD/Measures/Tb2C/sample3/6R/J9/Cycle/Second_Dege/second_VG/etud_temp/T_300mK/Cycle1");
#CycT300 = CycleProcess("G_B_trace.json","G_B_retrace.json",[0,1,2,3,4,5,6,7,8,9,10],"Json");
CycT300 = CycleProcess("CycT300fig.bin")
CycT300.LoadSweeps()

# <codecell>

CycT300.GetStat(250,4)
CycT300.GetValueStat()

# <codecell>

CycT300.SetPlotCalibration([10**-32,10**-28,[-0.085,0.085],-0.019])
CycT300.SaveAll("tracefigure","retracefigure","CycT300fig.bin")

# <codecell>

os.chdir("/media/Iomega_HDD/Measures/Tb2C/sample3/6R/J9/Cycle/Second_Dege/second_VG/etud_temp/T_500mK/Cycle1");
#CycT500 = CycleProcess("G_B_trace.json","G_B_retrace.json",[0,1,2,3,4,5,6,7,8,9,10],"Json");
CycT500 = CycleProcess("CycT500fig.bin")
CycT500.LoadSweeps()

# <codecell>

CycT500.GetStat(250,4)
CycT500.GetValueStat()

# <codecell>

CycT500.SetPlotCalibration([10**-32,10**-28,[-0.085,0.085],-0.019])
CycT500.SaveAll("tracefigure","retracefigure","CycT500fig.bin")

# <codecell>

os.chdir("/media/Iomega_HDD/Measures/Tb2C/sample3/6R/J9/Cycle/Second_Dege/second_VG/etud_temp/T_700mK/Cycle1");
#CycT700 = CycleProcess("G_B_trace.json","G_B_retrace.json",[0,1,2,3,4,5,6,7,8,9,10],"Json");
CycT700 = CycleProcess("CycT700fig.bin")
CycT700.LoadSweeps()

# <codecell>

#CycT700.GetStat(250,4)
CycT700.GetValueStat()

# <codecell>

CycT700.SetPlotCalibration([10**-32,10**-28,[-0.085,0.085],-0.019])
CycT700.SaveAll("tracefigure","retracefigure","CycT700fig.bin")

# <codecell>

CycT200.SortData()
CycT300.SortData()
CycT500.SortData()
CycT700.SortData()


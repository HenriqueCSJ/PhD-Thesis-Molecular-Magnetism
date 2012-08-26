execfile("Transport/CB_classique.py")
fig = figure()
fig.set_size_inches(12,5.5)
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)



#trace du p(\mu)
x = linspace(0,2,1500)
ax1.plot(x,fer(x-1,0,1,0.001))
ax1.plot(x,fer(x-1,0,1,0.01))
ax1.plot(x,fer(x-1,0,1,0.05))
ax1.plot(x,fer(x-1,0,1,0.1))
ax1.set_xlabel(r"$\mu / \mu_{\rm{F}}$")
ax1.set_ylabel(r"$p(\mu)$")
ax1.yaxis.set_ticks([0,0.5,1])



l1 = ax1.lines[0]
l2 = ax1.lines[1]
l3 = ax1.lines[2]
l4 = ax1.lines[3]
l1.set_label(r"$T = 0.001\mu_{\rm{F}}$")
l2.set_label(r"$T = 0.01\mu_{\rm{F}}$")
l3.set_label(r"$T = 0.05\mu_{\rm{F}}$")
l4.set_label(r"$T = 0.1\mu_{\rm{F}}$")
ax1.legend()





#trace de U(N) en fonction de Vg
def U(N,Vg):
	return 1*(-N + Vg)**2

VG = linspace(-3.5,3.5,500)
N = range(-3,4)
for X in N :
	ax2.plot(VG,2*U(X,VG),'black',linewidth=1)

for X in N :
	temp = linspace(X-0.5,X+0.5,500)
	ax2.plot(temp,2*U(X,temp),'black')
ax2.set_xlabel(r"$q/e$")
ax2.set_ylabel(r"$E/E_c$")
ax2.set_xlim(-1.5,1.5)
ax2.set_ylim(0,2.2)
ax2.yaxis.set_ticks([0,1,2])
ax2.xaxis.set_ticklabels(['-3/2','-1','-1/2','0','1/2','1','3/2'])
ax2.text(-1,0.25,"-1",fontsize = 25,va="center",ha="center")
ax2.text(0,0.25,"0",fontsize = 25,va="center",ha="center")
ax2.text(1,0.25,"1",fontsize = 25,va="center",ha="center")
#Mise en page du plot
#compute scale multiplicator
xmin= ax1.get_xlim()
ymin= ax1.get_ylim()
a1 = 1.0 * abs((xmin[0]-xmin[1])/(ymin[0]-ymin[1]))

xmin= ax2.get_xlim()
ymin= ax2.get_ylim()
a2 = 1.0 * abs((xmin[0]-xmin[1])/(ymin[0]-ymin[1]))
#scale graphs
ax1.set_aspect(a1*0.9,)
ax2.set_aspect(a2*0.9,)
fig.subplots_adjust(left=0.09,right=0.97,wspace=0.35)
fig.text(0.01,0.95,"a",fontsize=25,fontweight="bold",backgroundcolor="pink")
fig.text(0.51,0.95,"b",fontsize=25,fontweight="bold",backgroundcolor="pink")
fig.savefig("Theorie/Transport/figure2/figure2.pdf")
#close(fig)

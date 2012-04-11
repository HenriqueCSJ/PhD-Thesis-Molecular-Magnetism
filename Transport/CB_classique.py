import numpy as np

e = -1.6e-19
kb = 1.38e-23

def fer(mu_dot,mu,T,kb):
	return 1./(1+np.exp((mu_dot-mu)/(kb*T)))

def mu_dot(Cg,Cs,Cd,Vg,Vs,Vd,N,e=e):
	Ctot = Cg + Cs + Cd
	return (N-0.5)*e**2/Ctot + e/Ctot * (Cg*Vg + Cd*Vd + Cs*Vs)


def Gamma_01_s(mu_dot,Vs,gamma_s,T=4,kb=kb):
	return 2*gamma_s*fer(mu_dot,e*Vs,T,kb)

def Gamma_01_d(mu_dot,Vd,gamma_d,T=4,kb=kb):
	return 2*gamma_d*fer(mu_dot,e*Vd,T,kb)

def Gamma_01(mu_dot,Vs,Vd,gamma_s,gamma_d,T=4,kb=kb):
	return Gamma_01_s(mu_dot,Vs,gamma_s,T,kb) +  Gamma_01_d(mu_dot,Vd,gamma_d,T,kb)




def Gamma_10_s(mu_dot,Vs,gamma_s,T=4,kb=kb):
	return gamma_s * (1 - fer(mu_dot,e*Vs,T,kb))

def Gamma_10_d(mu_dot,Vd,gamma_d,T=4,kb=kb):
	return gamma_d * (1 - fer(mu_dot,e*Vd,T,kb))

def Gamma_10(mu_dot,Vs,Vd,gamma_s,gamma_d,T=4,kb=kb):
	return Gamma_10_s(mu_dot,Vs,gamma_s,T,kb) +  Gamma_10_d(mu_dot,Vd,gamma_d,T,kb)




def P1(mu_dot,Vs,Vd,gamma_s,gamma_d,T=4,kb=kb):
	denom = Gamma_01(mu_dot,Vs,Vd,gamma_s,gamma_d,T,kb) + Gamma_10(mu_dot,Vs,Vd,gamma_s,gamma_d,T,kb)
	return Gamma_01(mu_dot,Vs,Vd,gamma_s,gamma_d,T,kb)/denom

def P0(mu_dot,Vs,Vd,gamma_s,gamma_d,T=4,kb=kb):
	denom = Gamma_01(mu_dot,Vs,Vd,gamma_s,gamma_d,T,kb) + Gamma_10(mu_dot,Vs,Vd,gamma_s,gamma_d,T,kb)
	return Gamma_10(mu_dot,Vs,Vd,gamma_s,gamma_d,T,kb)/denom

def current(Vs,Vd,Vg,Cs,Cd,Cg,gamma_s,gamma_d,T=1,kb=kb,N=1):
	mu_DOT = mu_dot(Cg,Cd,Cs,Vg,Vd,Vs,N)
	curplus = Gamma_01_d(mu_DOT,Vd,gamma_d,T,kb) * P0(mu_DOT,Vs,Vd,gamma_s,gamma_d,T,kb)
	curmoins = Gamma_10_d(mu_DOT,Vd,gamma_d,T,kb) * P1(mu_DOT,Vs,Vd,gamma_s,gamma_d,T,kb)
	return e * (curplus - curmoins)


def I_Vds(Vmin,Vmax,nbr,Vg,Cs,Cd,Cg,gamma_s,gamma_d,T=4,kb=kb):
	VDS = linspace(Vmin,Vmax,nbr)
	temp = []
	for x in VDS:
		I = current(0,x,Vg,Cs,Cd,Cg,gamma_s,gamma_d,T,kb)
		temp.append(I)
	return [VDS,temp]

def dI_dVds(Vmin,Vmax,nbr,Vg,Cs,Cd,Cg,gamma_s,gamma_d,T=4,kb=kb):
	VDS = linspace(Vmin,Vmax,nbr)
	temp = []
	for x in VDS:
		I = current(0,x,Vg,Cs,Cd,Cg,gamma_s,gamma_d,T,kb)
		temp.append(I)
	temp = np.diff(temp)
	return [VDS[1:],temp]



def I_Vg_Vds(Vdmin,Vdmax,nvds,Vgmin,Vgmax,nvg,Cs,Cd,Cg,gamma_s,gamma_d,T=4,kb=kb):
	VG = linspace(Vgmin,Vgmax,nvg)
	result = []
	for v in VG:
		result.append(I_Vds(Vdmin,Vdmax,nvds,v,Cs,Cd,Cg,gamma_s,gamma_d,T,kb)[1])
	return result


def dI_Vg_dVds(Vdmin,Vdmax,nvds,Vgmin,Vgmax,nvg,Cs,Cd,Cg,gamma_s,gamma_d,T=4,kb=kb):
	VG = linspace(Vgmin,Vgmax,nvg)
	result = []
	for v in VG:
		result.append(dI_dVds(Vdmin,Vdmax,nvds,v,Cs,Cd,Cg,gamma_s,gamma_d,T,kb)[1])
	return result

"""
Vds = linspace(-20e-3,20e-3,5000)
Vg = linspace(-0.04,0.04,1000)
tot_current = []



for x in Vg:
	temp = []
	for y in Vds :
		I = current(0,y,x,1,1,1,200e6,200e6)
		temp.append(I)
	tot_current.append(temp)

temp = []
for y in Vds :
	I = current(0,y,0.001,1,1,1,200e6,200e6)
	temp.append(I)


figure()
plot(Vds,temp)
result = matrix(tot_current).transpose().tolist()
im = imshow(result, interpolation ="nearest")
im.set_extent([Vg[0],Vg[-1],Vds[0],Vds[-1]])
ax = gca()
ax.set_aspect("auto")
draw()
"""

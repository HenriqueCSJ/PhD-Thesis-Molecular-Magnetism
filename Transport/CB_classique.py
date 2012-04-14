import numpy as np

e = -1.6e-19
kb = 1.38e-23
mub = 9.27e-24
g = 2


#p(mu)
def fer(mu_dot,mu,T,kb):
	return 1./(1+np.exp((mu_dot-mu)/(kb*T)))

#spin down
def mu_dot_p(Cg,Cs,Cd,Vg,Vs,Vd,B,N,e=e):
	Ctot = Cg + Cs + Cd
	return (N-0.5)*e**2/Ctot + e/Ctot * (Cg*Vg + Cd*Vd + Cs*Vs) + 0.5* g * mub * B

#spin down
def mu_dot_n(Cg,Cs,Cd,Vg,Vs,Vd,B,N,e=e):
	Ctot = Cg + Cs + Cd
	return (N-0.5)*e**2/Ctot + e/Ctot * (Cg*Vg + Cd*Vd + Cs*Vs) - 0.5 * g * mub * B

#Gamma 0 -> 1
def Gamma_01_s(mu_dot,Vs,gamma_s,T=4,kb=kb):
	return gamma_s*fer(mu_dot,e*Vs,T,kb)

def Gamma_01_d(mu_dot,Vd,gamma_d,T=4,kb=kb):
	return gamma_d*fer(mu_dot,e*Vd,T,kb)

def Gamma_01(mu_dot,Vs,Vd,gamma_s,gamma_d,T=4,kb=kb):
	return Gamma_01_s(mu_dot,Vs,gamma_s,T,kb) +  Gamma_01_d(mu_dot,Vd,gamma_d,T,kb)

#Gamme 1->0
def Gamma_10_s(mu_dot,Vs,gamma_s,T=4,kb=kb):
	return gamma_s * (1 - fer(mu_dot,e*Vs,T,kb))

def Gamma_10_d(mu_dot,Vd,gamma_d,T=4,kb=kb):
	return gamma_d * (1 - fer(mu_dot,e*Vd,T,kb))

def Gamma_10(mu_dot,Vs,Vd,gamma_s,gamma_d,T=4,kb=kb):
	return Gamma_10_s(mu_dot,Vs,gamma_s,T,kb) +  Gamma_10_d(mu_dot,Vd,gamma_d,T,kb)



#P1+
def P1(p0,mu_dot,Vs,Vd,gamma_s,gamma_d,T=4,kb=kb):
	denom = Gamma_10(mu_dot,Vs,Vd,gamma_s,gamma_d,T,kb) 
	return p0 * Gamma_01(mu_dot,Vs,Vd,gamma_s,gamma_d,T,kb)/denom
#P0
def P0(mu_dot_p,mu_dot_n,Vs,Vd,gamma_s,gamma_d,T=4,kb=kb):
	denom = 1.  
	denom = denom + Gamma_01(mu_dot_p,Vs,Vd,gamma_s,gamma_d,T,kb) / Gamma_10(mu_dot_p,Vs,Vd,gamma_s,gamma_d,T,kb)
	denom = denom + Gamma_01(mu_dot_n,Vs,Vd,gamma_s,gamma_d,T,kb) / Gamma_10(mu_dot_n,Vs,Vd,gamma_s,gamma_d,T,kb)
	return 1/denom

#Courant
def current(Vs,Vd,Vg,Cs,Cd,Cg,gamma_s,gamma_d,B,T=1,kb=kb,N=1):
	mu_DOT_P = mu_dot_p(Cg,Cd,Cs,Vg,Vd,Vs,B,N)
	mu_DOT_N = mu_dot_n(Cg,Cd,Cs,Vg,Vd,Vs,B,N)
	p0 = P0(mu_DOT_P,mu_DOT_N,Vs,Vd,gamma_s,gamma_d,T,kb)
	curplus = Gamma_01_d(mu_DOT_P,Vd,gamma_d,T,kb) * p0 
	curplus = curplus + Gamma_01_d(mu_DOT_N,Vd,gamma_d,T,kb) * p0
	curmoins = Gamma_10_d(mu_DOT_P,Vd,gamma_d,T,kb) * P1(p0,mu_DOT_P,Vs,Vd,gamma_s,gamma_d,T,kb)
	curmoins = curmoins + Gamma_10_d(mu_DOT_N,Vd,gamma_d,T,kb) * P1(p0,mu_DOT_N,Vs,Vd,gamma_s,gamma_d,T,kb)
	return e * (curplus - curmoins)


def I_Vds(Vmin,Vmax,nbr,Vg,Cs,Cd,Cg,gamma_s,gamma_d,B,T=4,kb=kb):
	VDS = linspace(Vmin,Vmax,nbr)
	temp = []
	for x in VDS:
		I = current(0,x,Vg,Cs,Cd,Cg,gamma_s,gamma_d,B,T,kb)
		temp.append(I)
	return [VDS,temp]

def dI_dVds(Vmin,Vmax,nbr,Vg,Cs,Cd,Cg,gamma_s,gamma_d,B,T=4,kb=kb):
	VDS = linspace(Vmin,Vmax,nbr)
	temp = []
	for x in VDS:
		I = current(0,x,Vg,Cs,Cd,Cg,gamma_s,gamma_d,B,T,kb)
		temp.append(I)
	temp = np.diff(temp)
	return [VDS[1:],temp]



def I_Vg_Vds(Vdmin,Vdmax,nvds,Vgmin,Vgmax,nvg,Cs,Cd,Cg,gamma_s,gamma_d,B,T=4,kb=kb):
	VG = linspace(Vgmin,Vgmax,nvg)
	result = []
	for v in VG:
		result.append(I_Vds(Vdmin,Vdmax,nvds,v,Cs,Cd,Cg,gamma_s,gamma_d,B,T,kb)[1])
	return result


def dI_Vg_dVds(Vdmin,Vdmax,nvds,Vgmin,Vgmax,nvg,Cs,Cd,Cg,gamma_s,gamma_d,B,T=4,kb=kb):
	VG = linspace(Vgmin,Vgmax,nvg)
	result = []
	for v in VG:
		result.append(dI_dVds(Vdmin,Vdmax,nvds,v,Cs,Cd,Cg,gamma_s,gamma_d,B,T,kb)[1])
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

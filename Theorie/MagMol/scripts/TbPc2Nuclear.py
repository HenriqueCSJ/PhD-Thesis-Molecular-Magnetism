
def MPauli(J) :
    """Compute the Pauli matrices for a given system. It returns them in the following order : Sx,Sy,Sz,S+,S-"""
    
    """This part creates the different matrices filled with zeros"""
    sigmaX = matrix( zeros((2*J+1,2*J+1)) )
    sigmaY = matrix( zeros((2*J+1,2*J+1)) )
    sigmaZ = matrix( zeros((2*J+1,2*J+1)) )
    sigmaPlus = matrix( zeros((2*J+1,2*J+1)) )
    sigmaMoins = matrix( zeros((2*J+1,2*J+1)) )
    n = int(2*J+1)
        
    """Sigma Z """
    for i in range(n) :
        for j in range(n) :
            if i == j :
                sigmaZ[i,j] = J - i          

        """SigmaPlus"""
    for i in range(n) :
        for j in range(n) :
            if j == i + 1 :
                sigmaPlus[i,j] = sqrt(J * (J+1) - (sigmaZ[j,j] * (sigmaZ[j,j] + 1)))          

    """SigmaMoins"""
    for i in range(n) :
        for j in range(n) :
            if j == i - 1 :
                sigmaMoins[i,j] = sqrt(J * (J + 1) - (sigmaZ[j,j] * (sigmaZ[j,j] - 1)))          
                
    
    """SigmaX"""
    sigmaX = (sigmaPlus+sigmaMoins) / 2.
    
    """SigmaY"""
    sigmaY=1j * (sigmaMoins-sigmaPlus) / 2.
    
    
    return [sigmaX, sigmaY, sigmaZ, sigmaPlus, sigmaMoins] 



def tensorProduct(J):
    """For a given matrix J=[J1,J2,...,Jn] this function return the same operateur but in the new space obtained using the kroenecker product"""
    n = len(J)
    result = []
    for i in range(n) :
        Temp1 = 1
        Temp2 = 1
        for j in range(i) :
            Temp1 = kron(Temp1, eye(len(J[j])))
        for j in range((i+1), n):
            Temp2 = kron(Temp2, eye(len(J[j])))
        result.append(kron(Temp1, kron(J[i], Temp2)))
    return result




def sysPau(J) :
    """This function compute the different Sx,Sy,Sz,S+,S- for all the particles of the system and return them in a single array in the same order than given in argument."""
    n = len(J)
    sysPau = []
    for i in range(n) :
        sysPau.append(MPauli(J[i]))
    
    return sysPau   


def extractData(J, N):
    """This function is helpful extracting data from the matrix returned sysPau and using tensorProduct, construct the quantum operators in the new space"""
    n = len(J)
    temp = []
    for i in range(n):
        temp.append(J[i][N])
    result = tensorProduct(temp)
    return result

def O_02(S) :
	""""
	S is given such that
	S[0] = Sx
	S[1] = Sy
	S[2] = Sz
	S[3] = S+
	S[4] = S-
	which is the case if you use the MPauli function
	"""
	J = 6  #j 
	m = size(S[0][0])
	alpha = J*(J+1) * matrix(eye(m))
	result = matrix( zeros((m,m))) 
	result =  3*S[2]**2 - alpha
	return result

def O_04(S) :
	""""
	S is given such that
	S[0] = Sx
	S[1] = Sy
	S[2] = Sz
	S[3] = S+
	S[4] = S-
	which is the case if you use the MPauli function
	"""
	J = 6  #j 
	m = size(S[0][0])
	alpha = J*(J+1) * matrix(eye(m))
	result = matrix( zeros((m,m))) 
	result = 35 * S[2]**4 - 30 * alpha *S[2]**2 + 25 * S[2]**2 - 6*alpha + 3*alpha**2 
	return result

def O_44(S) :
	""""
	S is given such that
	S[0] = Sx
	S[1] = Sy
	S[2] = Sz

	S[3] = S+
	S[4] = S-
	which is the case if you use the MPauli function
	"""
	m = size(S[0])
	result = matrix( zeros((m,m))) 
	result = 0.5 * (S[3]**4 + S[4]**4)
	return result


def O_06(S) :
	""""
	S is given such that
	S[0] = Sx
	S[1] = Sy
	S[2] = Sz
	S[3] = S+
	S[4] = S-
	which is the case if you use the MPauli function
	"""
	J = 6 #j 
	m = size(S[0][0])
	alpha = J*(J+1) * matrix(eye(m))
	result = matrix( zeros((m,m))) 
	result = 231*S[2]**6 - 315*alpha* S[2]**4 + 735*S[2]**4 + 105*(alpha**2)*S[2]**2 - 525*alpha*S[2]**2 + 294*S[2]**2 -5*alpha**3 + 40*(alpha**2) - 60*alpha
	return result


#On calcule les elements de matrice pour nucleaire
Sys = sysPau([6,1.5])
J = Sys[0]
I = Sys[1]
Jp = []
Ip = []
for i in range(5):
	Jp.append(kron(J[i],eye(4)))
	Ip.append(kron(eye(13),I[i]))
J = Jp
I = Ip


#On calcule les elements de matrice pour spin 1/2
Sys2 = sysPau([6,0.5])
J1 = Sys2[0]
I1 = Sys2[1]
Jp1 = []
Ip1 = []
for i in range(5):
    Jp1.append(kron(J1[i],eye(2)))
    Ip1.append(kron(eye(13),I1[i]))
J1 = Jp1
I1 = Ip1



def Tb_Pc2(B,Bx,By):
    g = 3/2.
    muB = 0.465 #en cm-1
    J = MPauli(6)
    alpha=  1/(99.)
    beta=  2/(11*1485.)
    gamma =  1/(13*33*2079.)
    A_02 = -414  #cm-1
    A_04 = -228 #cm-1
    A_44 = -10 #cm-1
    A_06 = -33 #cm-1
    HB = g * muB * J[2] * B + g * muB * (J[1] * Bx + J[0] * By)
    HL = A_02 * alpha *O_02(J) + A_04 * beta * O_04(J) +  A_06 * gamma * O_06(J) + A_44 * beta * O_44(J)
    E,V = linalg.eig(HL+HB)
    order = E.argsort()
    V = V.transpose()
    Vf = []
    for x in order :
        Vf.append(V[x])
    E =list(E/0.695) #convert Kelvin11
    E.sort()
    return E,Vf


def Tb_Pc2_spin12(B,Bx,By):
    I = I1
    J = J1
    g = 3/2
    gn=2
    muB = 0.465 #en cm-1
    muN = muB
    alpha=  1/(99.)
    beta=  2/(11*1485.)
    gamma =  1/(13*33*2079.)
    A_02 = -414  #cm-1
    A_04 = -228 #cm-1
    A_44 = -10 #cm-1
    A_06 = -33 #cm-1
    Ahf = 0.163 #cm-1 ~ 350mT
    HB = g * muB * J[2] * B + g * muB * (J[0] * Bx + J[1] * By)
    HBn = gn * muN * I[2] * B + gn * muN * (I[0] * Bx + I[1] * By)
    HL = A_02 * alpha *O_02(J) + A_04 * beta * O_04(J) +  A_06 * gamma * O_06(J) + A_44 * beta * O_44(J)
    Hhf =  Ahf * (J[0]*I[0] + J[1]*I[1] + J[2]*I[2])
    E = linalg.eigvals(HL+HB+Hhf+HBn)
    E =list(E/0.695) #convert Kelvin
    E.sort()
    return E    


def Tb_Pc2Nuclear(B,Bx,By):
	g = 3/2
	gn=2
	muB = 0.465 #en cm-1
	muN = muB*1e-3
	alpha=  1/(99.)
	beta=  2/(11*1485.)
	gamma =  1/(13*33*2079.)
	A_02 = -414  #cm-1
	A_04 = -228 #cm-1
	A_44 = -10 #cm-1
	A_06 = -33 #cm-1
	Ahf = 0.0173
	Phf = 0.01
	HB = g * muB * J[2] * B + g * muB * (J[0] * Bx + J[1] * By)
	HBn = gn * muN * I[2] * B + gn * muN * (I[0] * Bx + I[1] * By)
	HL = A_02 * alpha *O_02(J) + A_04 * beta * O_04(J) +  A_06 * gamma * O_06(J) + A_44 * beta * O_44(J)
	Hhf =  Ahf * (J[0]*I[0] + J[1]*I[1] + J[2]*I[2]) + Phf * (I[2]**2 - 1/3. * eye(52) * 1.5*2.5 )
	E = linalg.eigvals(HL+HB+Hhf+HBn)
	E =list(E/0.695) #convert Kelvin
	E.sort()
	return E	



def Tb_Pc2_Zeeman(bmin,bmax,nbr,Bx,By) :
    B = linspace(bmin,bmax,nbr)		
    resultE = []
    resultV = []
    for i in range(size(B)) :
        R, V = Tb_Pc2(B[i],Bx,By)
        resultE.append(real(R))
        resultV.append(V)
    return resultE, resultV

def Tb_Pc2_ZeemanNuclear(bmin,bmax,nbr,Bx,By) :
    B = linspace(bmin,bmax,nbr)		
    result = []
    for i in range(size(B)) :
        R = Tb_Pc2Nuclear(B[i],Bx,By)
        result.append(real(R))
    return result

def Tb_Pc2_Zeemanspin12(bmin,bmax,nbr,Bx,By) :
    B = linspace(bmin,bmax,nbr)     
    result = []
    for i in range(size(B)) :
        R = Tb_Pc2_spin12(B[i],Bx,By)
        result.append(real(R))
    return result

def Tb_Pc2_split(bmin,bmax,nbr,phi):
    B = linspace(bmin,bmax,nbr)
    result = []
    for i in range(size(B)):
        R = Tb_Pc2(0,B[i]*cos(phi),B[i]*sin(phi))
        result.append(abs(R[0]-R[1]))
    return result


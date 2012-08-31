
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
	J = (size(S[0][0]) -1 )/2.  #j 
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
	J = (size(S[0][0]) -1 )/2.  #j 
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
	J = (size(S[0][0]) -1 )/2.  #j 
	m = size(S[0][0])
	alpha = J*(J+1) * matrix(eye(m))
	result = matrix( zeros((m,m))) 
	result = 231*S[2]**6 - 315*alpha* S[2]**4 + 735*S[2]**4 + 105*(alpha**2)*S[2]**2 - 525*alpha*S[2]**2 + 294*S[2]**2 -5*alpha**3 + 40*(alpha**2) - 60*alpha
	return result

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
    E = linalg.eigvals(HL+HB)
    E =list(E/0.695) #convert Kelvin11
    E.sort()
    return E


def Tb_Pc2_Zeeman(bmin,bmax,nbr,Bx,By) :
    B = linspace(bmin,bmax,nbr)		
    result = []
    for i in range(size(B)) :
        R = Tb_Pc2(B[i],Bx,By)
        result.append(real(R))
    return result

def Tb_Pc2_split(bmin,bmax,nbr,phi):
    B = linspace(bmin,bmax,nbr)
    result = []
    for i in range(size(B)):
        R = Tb_Pc2(0,B[i]*cos(phi),B[i]*sin(phi))
        result.append(abs(R[0]-R[1]))
    return result

 

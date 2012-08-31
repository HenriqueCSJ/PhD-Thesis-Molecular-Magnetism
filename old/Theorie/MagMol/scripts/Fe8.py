g = 2
muB = 0.67 

#Matrice de Pauli
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
    
    
    return [sigmaX,  sigmaY, sigmaZ , sigmaPlus, sigmaMoins] 


def Fe8(B,g=2) :
	J = MPauli(10)
	D = 0.275
	E = 0.046
	HB =  g * muB * J[2] * B
	HA = - D * J[2]**2 + E * (J[0]**2 - J[1]**2)
	E = linalg.eigvals(HB+HA)
	E = list(E)
	E.sort()
	return E


def Fe8_Zeeman(bmin,bmax,nbr = 100,g=2) :
	B = linspace(bmin,bmax,nbr)
	result = []
	for i in range(size(B)) :
		R = Fe8(B[i])
		result.append(real(R))
	return result

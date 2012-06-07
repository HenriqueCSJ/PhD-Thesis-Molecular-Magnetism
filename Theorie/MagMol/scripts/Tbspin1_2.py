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
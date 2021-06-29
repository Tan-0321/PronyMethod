# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 10:18:43 2021

@author: Tan Bingyang
"""

import numpy as np
import math as mt
import scipy.linalg as sl


def MPM(phi,p,Ts):
    
    end=len(phi)-1
    Y=sl.hankel(phi[:end-p],phi[end-p:])
    Y1=Y[:,:-1]
    Y2=Y[:,1:]
    Y1p=np.linalg.pinv(Y1)
    EV=np.linalg.eigvals(np.dot(Y1p, Y2))
    EL=len(EV)
    

    #Damping factor and frequency as Prony's method
    alpha=np.empty([p])
    frequency=np.empty([p])
    for i in range(p):
        alpha[i]=mt.log(abs(EV[i]))/Ts
        frequency[i]=mt.atan2(EV[i].imag, EV[i].real)/(2*mt.pi*Ts)
    
    #complex residues (amplitudes and angle phases)as Prony's method
    Z=np.zeros([EL,EL],dtype=complex)
    rZ=np.empty([EL,EL])
    iZ=np.empty([EL,EL])
    for i in range(EL):
        for j in range(EL):
            Z[i,j]=EV[j]**i
            rZ[i,j]=Z[i,j].real
            iZ[i,j]=Z[i,j].imag
    
    h=np.linalg.solve(Z,phi[0:EL])
    theta=np.empty([EL])
    amp=abs(h)
    for i in range(EL):
        theta[i]=mt.atan2(h[i].imag, h[i].real)

    answer=np.c_[amp,theta,alpha,frequency]
    return answer


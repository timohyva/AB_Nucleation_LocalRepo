






# import Module_SC_CorrectionObject_V01 as SC # strong coupling correction module
import Module_SC_Beta_V01 as SC_beta_gaps # all SC beta and gaps of A&B in SI unit
# import Module_plot_TAB_line as TAB_line
import Module_Lotynk_pT_parameter as Lotynk

import matplotlib.pyplot as plot1
import matplotlib
import numpy as np

from math import pi
import math
from matplotlib import ticker, cm
import csv

# main code starts from here

m = 1;s = 1; J = 1; Kelvin = 1; kg =1; bar = 1;# Length unit, Time unit, Energy unit, mass unit, pressure unit 
zeta3 = 1.2020569;
# kb = 8.617333262145*(10**(-5)) #Boltzmann ev.K^-1
kb = 1.380649*(10**(-23)) # Boltzmann constant J.K^-1
c = 2.99792458*(10**(8)) # speed of light, m.s^-1

# hbar = 6.582119569*(10**(-16)) #plank constant, eV.s
hbar = 1.054571817*(10**(-34)) # planck constant, J.s
# u = 9.3149410242*(10**(8))*eV*(c**(-2)) # atomic mass unit, Dalton, eV.c^-2
u = 1.66053906660*(10**(-27)) # atomic mass unit, Dalton, kg

m3 = 3.016293*u #mass of helium3 atom

# ##########################################################################################################
# ############  define the numpy elementwise function for \lambdabar, M2, \delta, \lambda ##################
# ##########################################################################################################
def calculator_of_lambdabar(d11, d12, d13, d21, d22, d23, d31, d32, d33,
                            psi11, psi12, psi13, psi21, psi22, psi23, psi31, psi32, psi33,
                            alpha, beta1, beta2, beta3, beta4, beta5,
                            gapA):
    
    M2_MonteCarlo = 2*(alpha - (-2*(beta2 + beta3 + beta4 + beta5) 
            + 2*beta3*(d13**2) 
            + 2*beta5*(d21**2 + d22**2 + d23**2 + d31**2 + d32**2 + d33**2)  
            + 2*beta1*(-1 + d13**2 + d21**2 + d22**2 + d23**2 + d31**2 + d32**2 + d33**2) 
            + (beta3 + beta4)*(d21**2 + d22**2 + 2*d23**2 + d31**2 + d32**2 + 2*d33**2))*(gapA**2) 
           + 2*(beta2 + beta4 + beta5)*(d11**2)*(gapA**2)*(np.cos(psi11))*(np.cos(psi11)) 
           + 4*(beta2 + beta4 + beta5)*d11*d12*(gapA**2)*(np.cos(psi11))*(np.sin(psi12))  
           - (gapA**2)*(-(beta5*(d21**2)*(np.cos(2*psi21))) 
                       + beta5*(d22**2)*(np.cos(2*psi22)) 
                       - beta5*(d31**2)*(np.cos(2*psi31)) 
                       + beta5*(d32**2)*(np.cos(2*psi32))
                       - 4*(beta1 + beta3)*d11*d12*(np.sin(psi11 - psi12)) 
                       - 2*(beta2 + beta4 + beta5)*(d12**2)*(np.sin(psi12))*(np.sin(psi12))  
                       + 2*d21*d22*((-beta3 + beta4)*(np.sin(psi21 - psi22)) - beta5*(np.sin(psi21 + psi22))) 
                       + 2*d31*d32*((-beta3 + beta4)*(np.sin(psi31 - psi32)) - beta5*(np.sin(psi31 + psi32)))))

    delta_MonteCarlo = 6*(np.sqrt(2))*gapA*(- (beta1*d11*(d22**2)*(np.cos(psi11 - 2*psi22)))  
                     - d12*d21*d22*(beta5*(np.cos(psi12 - psi21 - psi22)) + beta4*(np.cos(psi12 + psi21 - psi22)) + beta3*(np.cos(psi12 - psi21 + psi22)))  
                     - beta1*d11*(d23**2)*(np.cos(psi11 - 2*psi23)) 
                     - d13*d21*d23*(beta5*(np.cos(psi13 - psi21 - psi23)) + beta4*(np.cos(psi13 + psi21 - psi23)) + beta3*(np.cos(psi13 - psi21 + psi23))) 
                     - beta1*d11*(d32**2)*(np.cos(psi11 - 2*psi32)) 
                     - d12*d31*d32*(beta5*(np.cos(psi12 - psi31 - psi32)) + beta4*(np.cos(psi12 + psi31 - psi32)) + beta3*(np.cos(psi12 - psi31 + psi32)))  
                     - beta1*d11*(d33**2)*(np.cos(psi11 - 2*psi33)) 
                     - d13*d31*d33*(beta5*(np.cos(psi13 - psi31 - psi33)) + beta4*(np.cos(psi13 + psi31 - psi33)) + beta3*(np.cos(psi13 - psi31 + psi33))) 
                     + (np.cos(psi11))*(d11*(-beta2 + beta1*(-1 + d22**2 + d23**2 + d32**2 + d33**2)  
                                             +(beta3 + beta4 + beta5)*(-1 + d22**2 + d23**2 + d32**2 + d33**2)) 
                                        + 2*(beta1 + beta3)*(d12**3)*(np.sin(psi11 - psi12)))  
                     - (beta1 + beta3)*d12*(np.sin(2*psi11 - psi12)) 
                     - (beta2 + beta4 + beta5)*d12*(np.sin(psi12)) 
                     - 2*(beta1 + beta3)*d11*(d12**2)*(np.sin(psi11 - psi12))*(np.sin(psi12))  
                     + 2*(beta1 + beta3)*d12*(d13**2)*(np.cos(psi11 - psi12 + psi13))*(np.sin(psi11 - psi13)) 
                     - 2*(beta1 + beta3)*d11*(d13**2)*(np.sin(psi11 - psi13))*(np.sin(psi13))  
                     + d12*(d21**2)*((beta1 + beta3)*(np.sin(2*psi11 - psi12)) + (beta4 + beta5)*(np.sin(psi12)) + beta1*(np.sin(psi12 - 2*psi21)))  
                     - 2*(beta1 + beta5)*d11*(d21**2)*(np.sin(psi11 - psi21))*(np.sin(psi21))  
                     + d12*(d22**2)*((beta1 + beta3)*(np.sin(2*psi11 - psi12)) + (-beta3 + beta5)*(np.sin(psi12)) + (beta1 + beta5)*(np.sin(psi12 - 2*psi22)))  
                     + d11*d21*d22*(beta5*(np.sin(psi11 - psi21 - psi22)) - beta3*(np.sin(psi11 + psi21 - psi22)) - beta4*(np.sin(psi11 - psi21 + psi22)))  
                     + d12*(d23**2)*((beta1 + beta3)*(np.sin(2*psi11 - psi12)) + (beta4 + beta5)*(np.sin(psi12)) + beta1*(np.sin(psi12 - 2*psi23)))  
                     + d13*d22*d23*(beta5*(np.sin(psi13 - psi22 - psi23)) - beta4*(np.sin(psi13 + psi22 - psi23)) - beta3*(np.sin(psi13 - psi22 + psi23)))  
                     + d12*(d31**2)*((beta1 + beta3)*(np.sin(2*psi11 - psi12)) + (beta4 + beta5)*(np.sin(psi12)) + beta1*(np.sin(psi12 - 2*psi31)))  
                     - 2*(beta1 + beta5)*d11*(d31**2)*(np.sin(psi11 - psi31))*(np.sin(psi31))  
                     + d12*(d32**2)*((beta1 + beta3)*(np.sin(2*psi11 - psi12)) + (-beta3 + beta5)*(np.sin(psi12)) + (beta1 + beta5)*(np.sin(psi12 - 2*psi32)))  
                     + d11*d31*d32*(beta5*(np.sin(psi11 - psi31 - psi32)) - beta3*(np.sin(psi11 + psi31 - psi32)) - beta4*(np.sin(psi11 - psi31 + psi32)))  
                     + d12*(d33**2)*((beta1 + beta3)*(np.sin(2*psi11 - psi12)) + (beta4 + beta5)*(np.sin(psi12)) + beta1*(np.sin(psi12 - 2*psi33)))  
                     + d13*d32*d33*(beta5*(np.sin(psi13 - psi32 - psi33)) - beta4*(np.sin(psi13 + psi32 - psi33)) - beta3*(np.sin(psi13 - psi32 + psi33))))

    delta2_MonteCarlo = np.square(delta_MonteCarlo)

    lambda_MonteCarlo = 4*(beta2 + beta4 
   + (beta1 + beta3 + beta5)*(d11**4) + (beta1 + beta3 + beta5)*(d12**4) + (beta1 + beta3 + beta5)*(d13**4) 
   - 2*beta4*(d13**2)*(d21**2) + (beta1 + beta3 + beta5)*(d21**4) 
   - 2*beta4*(d22**2) + 2*(beta4 + beta5)*(d21**2)*(d22**2) 
   + (beta1 + beta3 + 2*beta4 + beta5)*(d22**4) 
   - 2*beta4*(d23**2) + 2*(beta3 + beta4)*(d13**2)*(d23**2) 
   + 2*(beta4 + beta5)*(d21**2)*(d23**2) + 2*(2*beta4 + beta5)*(d22**2)*(d23**2) 
   + (beta1 + beta3 + 2*beta4 + beta5)*(d23**4) 
   - 2*beta4*(d13**2)*(d31**2) + 2*beta3*(d21**2)*(d31**2) + (beta1 + beta3 + beta5)*(d31**4) + 2*(d11**2)*(beta5*(d12**2 + d13**2) + beta3*(d21**2 + d31**2)) 
   - 2*beta4*(d32**2) + 2*(beta3 + 2*beta4)*(d22**2)*(d32**2) + 2*beta4*(d23**2)*(d32**2) + 2*(beta4 + beta5)*(d31**2)*(d32**2) + (beta1 + beta3 + 2*beta4 + beta5)*(d32**4) 
   + 2*(d12**2)*(beta5*(d13**2) + (beta3 + beta4)*(d22**2) - beta4*(d21**2 + d31**2) + (beta3 + beta4)*(d32**2)) 
   - 2*beta4*(d33**2) + 2*(beta3 + beta4)*(d13**2)*(d33**2) + 2*beta4*(d22**2)*(d33**2) + 2*(beta3 + 2*beta4)*(d23**2)*(d33**2) 
   + 2*(beta4 + beta5)*(d31**2)*(d33**2) + 2*(2*beta4 + beta5)*(d32**2)*(d33**2) 
   + (beta1 + beta3 + 2*beta4 + beta5)*(d33**4) 
   + 2*((beta1 + beta3)*(d11**2)*(d12**2)*(np.cos(2*psi11 - 2*psi12)) + (beta1 + beta3)*(d11**2)*(d13**2)*(np.cos(2*psi11 - 2*psi13)) 
        + beta1*(d12**2)*(d13**2)*(np.cos(2*psi12 - 2*psi13)) + beta3*(d12**2)*(d13**2)*(np.cos(2*psi12 - 2*psi13)) + beta1*(d11**2)*(d21**2)*(np.cos(2*psi11 - 2*psi21)) 
        + beta5*(d11**2)*(d21**2)*(np.cos(2*psi11 - 2*psi21)) + beta1*(d12**2)*(d21**2)*(np.cos(2*psi12 - 2*psi21)) + beta1*(d13**2)*(d21**2)*(np.cos(2*psi13 - 2*psi21)) 
        + beta1*(d11**2)*(d22**2)*(np.cos(2*psi11 - 2*psi22)) + beta1*(d12**2)*(d22**2)*(np.cos(2*psi12 - 2*psi22)) + beta5*(d12**2)*(d22**2)*(np.cos(2*psi12 - 2*psi22)) 
        + beta1*(d13**2)*(d22**2)*(np.cos(2*psi13 - 2*psi22)) + beta1*(d21**2)*(d22**2)*(np.cos(2*psi21 - 2*psi22)) + beta3*(d21**2)*(d22**2)*(np.cos(2*psi21 - 2*psi22)) 
        + 2*beta5*d11*d12*d21*d22*(np.cos(psi11 + psi12 - psi21 - psi22)) + 2*beta3*d11*d12*d21*d22*(np.cos(psi11 - psi12 + psi21 - psi22)) 
        + 2*beta4*d11*d12*d21*d22*(np.cos(psi11 - psi12 - psi21 + psi22)) + beta1*(d11**2)*(d23**2)*(np.cos(2*psi11 - 2*psi23)) + beta1*(d12**2)*(d23**2)*(np.cos(2*psi12 - 2*psi23)) 
        + beta1*(d13**2)*(d23**2)*(np.cos(2*psi13 - 2*psi23)) + beta5*(d13**2)*(d23**2)*(np.cos(2*psi13 - 2*psi23)) + beta1*(d21**2)*(d23**2)*(np.cos(2*psi21 - 2*psi23)) 
        + beta3*(d21**2)*(d23**2)*(np.cos(2*psi21 - 2*psi23)) + beta1*(d22**2)*(d23**2)*(np.cos(2*psi22 - 2*psi23)) + beta3*(d22**2)*(d23**2)*(np.cos(2*psi22 - 2*psi23)) 
        + 2*beta5*d11*d13*d21*d23*(np.cos(psi11 + psi13 - psi21 - psi23)) + 2*beta3*d11*d13*d21*d23*(np.cos(psi11 - psi13 + psi21 - psi23)) 
        + 2*beta5*d12*d13*d22*d23*(np.cos(psi12 + psi13 - psi22 - psi23)) + 2*beta3*d12*d13*d22*d23*(np.cos(psi12 - psi13 + psi22 - psi23)) 
        + 2*beta4*d11*d13*d21*d23*(np.cos(psi11 - psi13 - psi21 + psi23)) + 2*beta4*d12*d13*d22*d23*(np.cos(psi12 - psi13 - psi22 + psi23)) 
        + beta1*(d11**2)*(d31**2)*(np.cos(2*psi11 - 2*psi31)) + beta5*(d11**2)*(d31**2)*(np.cos(2*psi11 - 2*psi31)) + beta1*(d12**2)*(d31**2)*(np.cos(2*psi12 - 2*psi31)) 
        + beta1*(d13**2)*(d31**2)*(np.cos(2*psi13 - 2*psi31)) + beta1*(d21**2)*(d31**2)*(np.cos(2*psi21 - 2*psi31)) + beta5*(d21**2)*(d31**2)*(np.cos(2*psi21 - 2*psi31)) 
        + beta1*(d22**2)*(d31**2)*(np.cos(2*psi22 - 2*psi31)) + beta1*(d23**2)*(d31**2)*(np.cos(2*psi23 - 2*psi31)) + beta1*(d11**2)*(d32**2)*(np.cos(2*psi11 - 2*psi32)) 
        + beta1*(d12**2)*(d32**2)*(np.cos(2*psi12 - 2*psi32)) + beta5*(d12**2)*(d32**2)*(np.cos(2*psi12 - 2*psi32)) + beta1*(d13**2)*(d32**2)*(np.cos(2*psi13 - 2*psi32)) 
        + beta1*(d21**2)*(d32**2)*(np.cos(2*psi21 - 2*psi32)) + beta1*(d22**2)*(d32**2)*(np.cos(2*psi22 - 2*psi32)) + beta5*(d22**2)*(d32**2)*(np.cos(2*psi22 - 2*psi32)) 
        + beta1*(d23**2)*(d32**2)*(np.cos(2*psi23 - 2*psi32)) + beta1*(d31**2)*(d32**2)*(np.cos(2*psi31 - 2*psi32)) + beta3*(d31**2)*(d32**2)*(np.cos(2*psi31 - 2*psi32)) 
        + 2*beta5*d11*d12*d31*d32*(np.cos(psi11 + psi12 - psi31 - psi32)) + 2*beta5*d21*d22*d31*d32*(np.cos(psi21 + psi22 - psi31 - psi32)) 
        + 2*beta3*d11*d12*d31*d32*(np.cos(psi11 - psi12 + psi31 - psi32)) + 2*beta3*d21*d22*d31*d32*(np.cos(psi21 - psi22 + psi31 - psi32)) 
        + 2*beta4*d11*d12*d31*d32*(np.cos(psi11 - psi12 - psi31 + psi32)) + 2*beta4*d21*d22*d31*d32*(np.cos(psi21 - psi22 - psi31 + psi32)) 
        + beta1*(d11**2)*(d33**2)*(np.cos(2*psi11 - 2*psi33)) + beta1*(d12**2)*(d33**2)*(np.cos(2*psi12 - 2*psi33)) + beta1*(d13**2)*(d33**2)*(np.cos(2*psi13 - 2*psi33)) 
        + beta5*(d13**2)*(d33**2)*(np.cos(2*psi13 - 2*psi33)) + beta1*(d21**2)*(d33**2)*(np.cos(2*psi21 - 2*psi33)) + beta1*(d22**2)*(d33**2)*(np.cos(2*psi22 - 2*psi33)) 
        + beta1*(d23**2)*(d33**2)*(np.cos(2*psi23 - 2*psi33)) + beta5*(d23**2)*(d33**2)*(np.cos(2*psi23 - 2*psi33)) + beta1*(d31**2)*(d33**2)*(np.cos(2*psi31 - 2*psi33)) 
        + beta3*(d31**2)*(d33**2)*(np.cos(2*psi31 - 2*psi33)) + beta1*(d32**2)*(d33**2)*(np.cos(2*psi32 - 2*psi33)) + beta3*(d32**2)*(d33**2)*(np.cos(2*psi32 - 2*psi33)) 
        + 2*beta5*d11*d13*d31*d33*(np.cos(psi11 + psi13 - psi31 - psi33)) + 2*beta5*d21*d23*d31*d33*(np.cos(psi21 + psi23 - psi31 - psi33)) 
        + 2*beta3*d11*d13*d31*d33*(np.cos(psi11 - psi13 + psi31 - psi33)) + 2*beta3*d21*d23*d31*d33*(np.cos(psi21 - psi23 + psi31 - psi33)) 
        + 2*beta5*d12*d13*d32*d33*(np.cos(psi12 + psi13 - psi32 - psi33)) + 2*beta5*d22*d23*d32*d33*(np.cos(psi22 + psi23 - psi32 - psi33)) 
        + 2*beta3*d12*d13*d32*d33*(np.cos(psi12 - psi13 + psi32 - psi33)) + 2*beta3*d22*d23*d32*d33*(np.cos(psi22 - psi23 + psi32 - psi33)) 
        + 2*beta4*d11*d13*d31*d33*(np.cos(psi11 - psi13 - psi31 + psi33)) + 2*beta4*d21*d23*d31*d33*(np.cos(psi21 - psi23 - psi31 + psi33)) 
        + 2*beta4*d12*d13*d32*d33*(np.cos(psi12 - psi13 - psi32 + psi33)) + 2*beta4*d22*d23*d32*d33*(np.cos(psi22 - psi23 - psi32 + psi33))))

    lambda_bar_MonteCarlo = (9/2)*lambda_MonteCarlo*(M2_MonteCarlo / delta2_MonteCarlo)

    return M2_MonteCarlo, delta_MonteCarlo, lambda_MonteCarlo, lambda_bar_MonteCarlo

#############################################################################################################
#########################        the np.array shaphe for all 18 + 1 elements      ###########################
#############################################################################################################
    
# the common array shape
# shape = (2,2)
array_shape = (333,333)
# array_shape = (8,8)
# array_shape = (1, 1)
net_No_samples = 0
No_filtered_samples = 0

######################################################
# net filtered np.array for saving lambda_bar D_alphai
######################################################

net_lambda_bar_filtered = np.array([])

net_d11_array_filtered = np.array([])
net_d12_array_filtered = np.array([])
net_d13_array_filtered = np.array([])
net_d21_array_filtered = np.array([])
net_d22_array_filtered = np.array([])
net_d23_array_filtered = np.array([])
net_d31_array_filtered = np.array([])
net_d32_array_filtered = np.array([])
net_d33_array_filtered = np.array([])

net_psi11_array_filtered = np.array([])
net_psi12_array_filtered = np.array([])
net_psi13_array_filtered = np.array([])
net_psi21_array_filtered = np.array([])
net_psi22_array_filtered = np.array([])
net_psi23_array_filtered = np.array([])
net_psi31_array_filtered = np.array([])
net_psi32_array_filtered = np.array([])
net_psi33_array_filtered = np.array([])


#########################################################
'''
pressure and Thenperature on p-T plane  #################
'''
#########################################################
p = 32.0*bar
Temperature = 0.1*(10**(-3))*Kelvin

#########################################################
# build the first plot object with 3*3 polar coordinate
#########################################################
# fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8), (ax9, ax10)) = plot1.subplots(5, 2, subplot_kw=dict(projection='polar'))
# plot1.figure(1)
fig1, ((ax1, ax2, ax3), (ax4, ax5, ax6), (ax7, ax8, ax9)) = plot1.subplots(3, 3, subplot_kw=dict(projection='polar'))

# build the second plot object for lambda_bar after filter
# plot1.figure(2)
fig2, ax_almbda_bar = plot1.subplots(1, 1)

# marker size of scatter plot
markersaize = 5

No_loops = 50

for i in range(0, No_loops, 1):

    print("\n now i is : ", i)

    d11_array = np.random.random_sample(array_shape)
    psi11_array = 2*pi*(np.random.random_sample(array_shape))

    d12_array = np.random.random_sample(array_shape)
    psi12_array = 2*pi*(np.random.random_sample(array_shape))

    d13 = np.random.random_sample(array_shape)
    psi13 = 2*pi*(np.random.random_sample(array_shape))

    d21 = np.random.random_sample(array_shape)
    psi21 = 2*pi*(np.random.random_sample(array_shape))

    d22_array = np.random.random_sample(array_shape)
    psi22_array = 2*pi*(np.random.random_sample(array_shape))

    d23 = np.random.random_sample(array_shape)
    psi23 = 2*pi*(np.random.random_sample(array_shape))

    d31 = np.random.random_sample(array_shape)
    psi31 = 2*pi*(np.random.random_sample(array_shape))

    d32 = np.random.random_sample(array_shape)
    psi32 = 2*pi*(np.random.random_sample(array_shape))

    d33_array = np.random.random_sample(array_shape)
    psi33_array = 2*pi*(np.random.random_sample(array_shape))
    
    # d33_array = np.sqrt(1.0 - (d11_array**2 + d12_array**2 + d13**2 + d21**2 + d22_array**2 + d23**2 + d31**2 + d32**2))
    normalizationIndex_array = 1/np.sqrt((d11_array**2 + d12_array**2 + d13**2 + d21**2 + d22_array**2 + d23**2 + d31**2 + d32**2 + d33_array**2))

    # print(" \n\n let's see the normalizationIndex_array: \n ", normalizationIndex_array)

    '''
      multipy d_alphai with normalizationIndex
    '''
    d11_array = normalizationIndex_array * d11_array

    d12_array = normalizationIndex_array * d12_array

    d13 = normalizationIndex_array * d13

    d21 = normalizationIndex_array * d21

    d22_array = normalizationIndex_array * d22_array

    d23 = normalizationIndex_array * d23

    d31 = normalizationIndex_array * d31

    d32 = normalizationIndex_array * d32

    d33_array = normalizationIndex_array * d33_array

    print(" \n\n now let's check the squre sum : \n ", d11_array**2 + d12_array**2 + d13**2 + d21**2 + d22_array**2 + d23**2 + d31**2 + d32**2 + d33_array**2)
    
    # normalization_filter = ((d11_array**2 + d12_array**2 + d13**2 + d21**2 + d22_array**2 + d23**2 + d31**2 + d32**2 + d33_array**2) - 1.0) <= 0.01
    # print(" \n\n normalization_filter is : \n", normalization_filter)

    # call the SC_beta_gaps object
    alpha, beta1, beta2, beta3, beta4, beta5, betaA, betaB, DeltaA, DeltaB, phi0, Tcp, xitp, xi0p, t = SC_beta_gaps.calculate_SC_beta_gaps_etc(p,Temperature)

    print(" \n\n t = T/Tcp is ",t," Tcp is : ",Tcp)

    # print(" \n\n T/Tc is : ", t/Tcp)
    

    # print(" d11_array is :\n ",d11_array, "\n\n psi11_array is :\n ", psi11_array)
    
    # plot1.polar(psi11_array, d11_array, 'g.')

    # call the function for calculating M2, \delta, \lambda and \lambda_bar
    M2_array, delta_array, lambda_array, lambda_bar_array = calculator_of_lambdabar(d11_array, d12_array, d13, d21, d22_array, d23, d31, d32, d33_array,
                            psi11_array, psi12_array, psi13, psi21, psi22_array, psi23, psi31, psi32, psi33_array,
                            alpha, beta1, beta2, beta3, beta4, beta5,
                            DeltaA)

    # print(" \n\n M2 numpy array is : ", M2_array, "\n\n delta numpy array is :", delta_array, " \n\n lambda numpy array is : ", lambda_array, "\n\n lambdaBar numpy array is : ", lambda_bar_array)

    # lambda_bar_arrayFlatten = lambda_bar_array.flatten()

    # print(" \n\n lambda bar after normalizaton filter is : \n ", lambda_bar_arrayFlatten)

    ###################################################################################################
    ###########################    generate the Boolen logic np.array       ###########################
    ###################################################################################################

    logic_filter = lambda_bar_array < (1.0)
  
    print(" \n\n the logic filter is :\n ", logic_filter)

    lambda_bar_filtered = lambda_bar_array[logic_filter]

    net_lambda_bar_filtered = np.append(net_lambda_bar_filtered, lambda_bar_filtered)

    ######################################################

    d11_array_filtered = d11_array[logic_filter]
    psi11_array_filtered = psi11_array[logic_filter]

    d12_array_filtered = d12_array[logic_filter]
    psi12_array_filtered = psi12_array[logic_filter]

    d13_array_filtered = d13[logic_filter]
    psi13_array_filtered = psi13[logic_filter]

    d21_array_filtered = d21[logic_filter]
    psi21_array_filtered = psi21[logic_filter]

    d22_array_filtered = d22_array[logic_filter]
    psi22_array_filtered = psi22_array[logic_filter]

    d23_array_filtered = d23[logic_filter]
    psi23_array_filtered = psi23[logic_filter]

    d31_array_filtered = d31[logic_filter]
    psi31_array_filtered = psi31[logic_filter]

    d32_array_filtered = d32[logic_filter]
    psi32_array_filtered = psi32[logic_filter]

    d33_array_filtered = d33_array[logic_filter]
    psi33_array_filtered = psi33_array[logic_filter]

    '''
       append the filtered array to the net one
    '''

    net_d11_array_filtered = np.append(net_d11_array_filtered, d11_array_filtered)
    net_d12_array_filtered = np.append(net_d12_array_filtered, d12_array_filtered)
    net_d13_array_filtered = np.append(net_d13_array_filtered, d13_array_filtered)
    net_d21_array_filtered = np.append(net_d21_array_filtered, d21_array_filtered)
    net_d22_array_filtered = np.append(net_d22_array_filtered, d22_array_filtered)
    net_d23_array_filtered = np.append(net_d23_array_filtered, d23_array_filtered)
    net_d31_array_filtered = np.append(net_d31_array_filtered, d31_array_filtered)
    net_d32_array_filtered = np.append(net_d32_array_filtered, d32_array_filtered)
    net_d33_array_filtered = np.append(net_d33_array_filtered, d33_array_filtered)

    net_psi11_array_filtered = np.append(net_psi11_array_filtered, psi11_array_filtered)
    net_psi12_array_filtered = np.append(net_psi12_array_filtered, psi12_array_filtered)
    net_psi13_array_filtered = np.append(net_psi13_array_filtered, psi13_array_filtered)
    net_psi21_array_filtered = np.append(net_psi21_array_filtered, psi21_array_filtered)
    net_psi22_array_filtered = np.append(net_psi22_array_filtered, psi22_array_filtered)
    net_psi23_array_filtered = np.append(net_psi23_array_filtered, psi23_array_filtered)
    net_psi31_array_filtered = np.append(net_psi31_array_filtered, psi31_array_filtered)
    net_psi32_array_filtered = np.append(net_psi32_array_filtered, psi32_array_filtered)
    net_psi33_array_filtered = np.append(net_psi33_array_filtered, psi33_array_filtered)

    
    ###################################################################################################
    ##########################              account some number           #############################
    ###################################################################################################

    net_No_samples += (lambda_bar_array.flatten()).size

    No_filtered_samples += d11_array_filtered.size

    print(" \n\n now the number of filted in this loop is : ",  d11_array_filtered.size, " and the number of total filtered lambda_bar is : ", No_filtered_samples )

    ###################################################################################################

    # plot1.matshow(lambda_bar_array)
    # plot1.scatter(np.random.random_sample(array_shape),lambda_bar_array);plot1.ylim([0.0, 1.25])

    # multi
    # plot1.scatter(np.arange(0,lambda_bar_arrayFlatten.size,1), lambda_bar_arrayFlatten, c = "green", s = 1.5);
    
    ###################################################################################################
    ##########################      plot the filted D_alphai elements       ###########################
    ###################################################################################################
    
    # fig, ((ax1, ax2, ax3),(ax4, ax5, ax6),(ax7, ax8, ax9)) = plot1.subplots(3, 3, subplot_kw=dict(projection='polar'))
    ax1.scatter(psi11_array_filtered, d11_array_filtered, s = markersaize)
    ax2.scatter(psi12_array_filtered, d12_array_filtered, s = markersaize)
    ax3.scatter(psi13_array_filtered, d13_array_filtered, s = markersaize)
    ax4.scatter(psi21_array_filtered, d21_array_filtered, s = markersaize)
    ax5.scatter(psi22_array_filtered, d22_array_filtered, s = markersaize)
    ax6.scatter(psi23_array_filtered, d23_array_filtered, s = markersaize)
    ax7.scatter(psi31_array_filtered, d31_array_filtered, s = markersaize)
    ax8.scatter(psi32_array_filtered, d32_array_filtered, s = markersaize)
    ax9.scatter(psi33_array_filtered, d33_array_filtered, s = markersaize)

    ###################################################################################################
    ##########################      plot the filted lambda_bar              ###########################
    ###################################################################################################

    ax_almbda_bar.scatter(np.arange(0,lambda_bar_filtered.size,1), lambda_bar_filtered, c = "green")
    
 

'''
# saving the 19 filtered np.array 
'''
np.savez('filtered_lambdaBar_Dalphai.npz', lambdaBar = net_lambda_bar_filtered,
                                           d11 = net_d11_array_filtered, d12 = net_d12_array_filtered, d13 = net_d13_array_filtered,
                                           d21 = net_d21_array_filtered, d22 = net_d22_array_filtered, d23 = net_d23_array_filtered,
                                           d31 = net_d31_array_filtered, d32 = net_d32_array_filtered, d33 = net_d33_array_filtered,
                                           psi11 = net_psi11_array_filtered, psi12 = net_psi12_array_filtered, psi13 = net_psi13_array_filtered,
                                           psi21 = net_psi21_array_filtered, psi22 = net_psi22_array_filtered, psi23 = net_psi23_array_filtered,
                                           psi31 = net_psi31_array_filtered, psi32 = net_psi32_array_filtered, psi33 = net_psi33_array_filtered)


########################################################################################################
##################                    plot and save the plots                     ######################
########################################################################################################
    
print("\n\n the total samples number is : ", net_No_samples, " filtered samples number is : ", No_filtered_samples)
# print(" \n\n the net_lambda_bar_filtered looks like : \n ", net_lambda_bar_filtered, " \n the net_lambda_bar_filtered looks like : \n ", net_d13_array_filtered)
# plot1.ylim([0.0, 1.15]);plot1.grid() 
# plot1.savefig("elements_distribution_exthutive_searching_on_hypersphere.png")

# plot1.ylim([0.0, 1.15]);plot1.grid()

# save the filtered lambda_bar plot
ax_almbda_bar.grid()
fig2.savefig("motherfuker.pdf")

# save the filtered elements of D_alphai 
fig1.savefig("motherfuker2.pdf")



plot1.show()

#!/usr/bin/env python
import numpy as np

class GRAFS:
    '''
    Class to implement the GRadient Ascent in Function Space protocol. This implementation
    is based off the reference:

    http://arxiv.org/pdf/1611.00188.pdf

    referring to equation numbers where able. Additional functionality has been
    added to allow for different fidelity measures.
    '''

    def __init__(self):
        '''
        Initializer for GRAFS class.
        '''


    def optimize_pulse_sequence(self, sequence,fitting_threshold=100.):
        '''
        Given an input pulse sequence, optimizes sequence relative to class fidelity.
        '''
        #Find initial parameters in function space
        def objective_function(alphas):
            #Construct eig_solve objects
            #Construct unitary objects
            #loop through fidelities & gradients
            #return net fidelity & gradient
            return None
        #minimize objective_function
        return None

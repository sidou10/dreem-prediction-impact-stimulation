#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import pandas as pd
import numpy as np

from numpy.fft import fft
from pywt import wavedec

def compute_wavelets_mean_coeffs(signal, feature_types = 
    ["mean_abs", "sum_abs", "std", "mean_squared"], n_segments=1, 
    signal_length=1, eeg_frequency=250, wavelet="db4", level=4, keep_approximation=True):
    """Perform Discrete Wavelet Transform on a eeg signal after dividing it 
    in segments. The eeg signal corresponds to a row of a DataFrame.
    """

    n = signal_length*eeg_frequency
    signal_segments = np.split(signal, n_segments)

    # Store the coefficients for all the segments
    features_segments = {"mean_abs": [], "sum_abs": [], "std": [], "mean_squared": []}
    
    for eeg_signal_segment in signal_segments:

        decomps_coeffs_segment = wavedec(eeg_signal_segment, wavelet=wavelet, level=level)

        if not keep_approximation:
            decomps_coeffs_segment = decomps_coeffs_segment[1:]

        if "mean_abs" in feature_types:
            mean_abs_coeffs_segment = [np.mean(np.abs(decomp_coeffs)) 
                                       for decomp_coeffs 
                                       in decomps_coeffs_segment]
            features_segments["mean_abs"] += mean_abs_coeffs_segment
        
        if "sum_abs" in feature_types:
            sum_abs_coeffs_segment = [np.sum(np.abs(decomp_coeffs)) 
                                      for decomp_coeffs 
                                      in decomps_coeffs_segment]
            features_segments["sum_abs"] += sum_abs_coeffs_segment

        if "std" in feature_types:
            std_coeffs_segment = [np.std(decomp_coeffs) 
                                  for decomp_coeffs 
                                  in decomps_coeffs_segment]
            features_segments["std"] += std_coeffs_segment
        
        if "mean_squared" in feature_types:
            mean_squared_coeffs_segment = [np.mean(np.square(decomp_coeffs)) 
                                           for decomp_coeffs 
                                           in decomps_coeffs_segment]
            features_segments["mean_squared"] += mean_squared_coeffs_segment
        
    # List to Series in order to create multiple columns when applying this
    # function on the rows of the DataFrame
    features = pd.Series(sum([features_segments[feature_type] for feature_type 
                              in features_segments if features_segments[feature_type]], []))
    
    return features


def compute_FFT_magnitudes(signal, n_segments=1, n_components=5):
    """Compute the magnitudes of the first components a FFT of a signal.
    """
    signal_segments = np.split(signal, n_segments)
    magnitudes_segments = []
    for signal_segment in signal_segments:
        magnitudes_segment = list(np.abs(fft(signal))[:n_components])
        magnitudes_segments += magnitudes_segment

    # List to Series in order to create multiple columns when applying this
    # function on the rows of the DataFrame
    features = pd.Series(sum([magnitudes_segments], []))

    return features
    
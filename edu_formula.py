"""
Core EDU Formula Implementation

The revolutionary EDU Formula: EDU(A,X) = (A/255·π), (406.4/X)
Universal signal modulation for AI, biology, physics, and beyond.

Author: Eduard Terre (ASCII-EDU)
Location: Offenburg, Germany
Year: 2024
"""

import math
from typing import Tuple, Union, List
import numpy as np


class EDUConstants:
    """Mathematical constants for the EDU Formula"""
    
    PI = math.pi
    NORMALIZATION_FACTOR = 255.0
    SCALING_CONSTANT = 406.4  # 16 × 25.4 (inch to mm conversion)
    
    # Fibonacci frequencies for biological applications
    FIBONACCI_FREQUENCIES = {
        'DNA_A': 144,    # Adenine
        'DNA_T': 233,    # Thymine  
        'DNA_G': 377,    # Guanine
        'DNA_C': 610     # Cytosine
    }
    
    # Neural frequency bands
    NEURAL_BANDS = {
        'delta': (0.5, 4.0),
        'theta': (4.0, 8.0),
        'alpha': (8.0, 13.0),
        'beta': (13.0, 30.0),
        'gamma': (30.0, 100.0)
    }


class EDUFormula:
    """
    The EDU Formula implementation
    
    EDU(A,X) = (A/255·π), (406.4/X)
    
    Where:
    - A: Amplitude/Intensity (0-255)
    - X: Frequency/Wavelength (must be > 0)
    
    Returns:
    - Tuple of (modulation, scaling) components
    """
    
    def __init__(self):
        self.constants = EDUConstants()
        
    def calculate(self, A: float, X: float) -> Tuple[float, float]:
        """
        Calculate EDU formula components
        
        Args:
            A: Amplitude/Intensity (0-255)
            X: Frequency/Wavelength (> 0)
            
        Returns:
            Tuple of (modulation, scaling)
            
        Raises:
            ValueError: If X <= 0 or A < 0
        """
        if X <= 0:
            raise ValueError("X must be positive")
        if A < 0:
            raise ValueError("A must be non-negative")
            
        # Clamp A to valid range
        A = min(A, self.constants.NORMALIZATION_FACTOR)
        
        # EDU Formula components
        modulation = (A / self.constants.NORMALIZATION_FACTOR) * self.constants.PI
        scaling = self.constants.SCALING_CONSTANT / X
        
        return modulation, scaling
    
    def calculate_combined(self, A: float, X: float) -> float:
        """
        Calculate combined EDU value (modulation × scaling)
        
        Args:
            A: Amplitude/Intensity (0-255)
            X: Frequency/Wavelength (> 0)
            
        Returns:
            Combined EDU value
        """
        modulation, scaling = self.calculate(A, X)
        return modulation * scaling
    
    def calculate_batch(self, A_values: List[float], X_values: List[float]) -> List[Tuple[float, float]]:
        """
        Calculate EDU formula for multiple input pairs
        
        Args:
            A_values: List of amplitude values
            X_values: List of frequency values
            
        Returns:
            List of (modulation, scaling) tuples
        """
        if len(A_values) != len(X_values):
            raise ValueError("A_values and X_values must have same length")
            
        results = []
        for A, X in zip(A_values, X_values):
            results.append(self.calculate(A, X))
        return results
    
    def calculate_numpy(self, A: np.ndarray, X: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        Vectorized EDU calculation using NumPy
        
        Args:
            A: Array of amplitude values
            X: Array of frequency values
            
        Returns:
            Tuple of (modulation_array, scaling_array)
        """
        # Input validation
        if np.any(X <= 0):
            raise ValueError("All X values must be positive")
        if np.any(A < 0):
            raise ValueError("All A values must be non-negative")
            
        # Clamp A values
        A = np.clip(A, 0, self.constants.NORMALIZATION_FACTOR)
        
        # Vectorized EDU calculation
        modulation = (A / self.constants.NORMALIZATION_FACTOR) * self.constants.PI
        scaling = self.constants.SCALING_CONSTANT / X
        
        return modulation, scaling
    
    def analyze_signal(self, signal: np.ndarray, sampling_rate: float) -> dict:
        """
        Analyze a signal using EDU formula
        
        Args:
            signal: Input signal array
            sampling_rate: Sampling rate in Hz
            
        Returns:
            Dictionary with EDU analysis results
        """
        # Signal statistics
        amplitude = np.max(np.abs(signal)) * self.constants.NORMALIZATION_FACTOR
        
        # Dominant frequency (simplified)
        fft = np.fft.fft(signal)
        freqs = np.fft.fftfreq(len(signal), 1/sampling_rate)
        dominant_freq = freqs[np.argmax(np.abs(fft[:len(fft)//2]))]
        
        if dominant_freq <= 0:
            dominant_freq = 1.0  # Avoid division by zero
            
        # EDU analysis
        modulation, scaling = self.calculate(amplitude, dominant_freq)
        combined = modulation * scaling
        
        # Classify neural band if applicable
        neural_band = self._classify_neural_band(dominant_freq)
        
        return {
            'amplitude': amplitude,
            'dominant_frequency': dominant_freq,
            'edu_modulation': modulation,
            'edu_scaling': scaling,
            'edu_combined': combined,
            'neural_band': neural_band,
            'signal_length': len(signal),
            'sampling_rate': sampling_rate
        }
    
    def _classify_neural_band(self, frequency: float) -> str:
        """Classify frequency into neural bands"""
        for band, (low, high) in self.constants.NEURAL_BANDS.items():
            if low <= frequency < high:
                return band
        return 'unknown'
    
    def get_formula_string(self) -> str:
        """Return the EDU formula as a string"""
        return "EDU(A,X) = (A/255·π), (406.4/X)"
    
    def get_info(self) -> dict:
        """Return information about the EDU formula"""
        return {
            'formula': self.get_formula_string(),
            'author': 'Eduard Terre (ASCII-EDU)',
            'location': 'Offenburg, Germany',
            'year': 2024,
            'constants': {
                'pi': self.constants.PI,
                'normalization_factor': self.constants.NORMALIZATION_FACTOR,
                'scaling_constant': self.constants.SCALING_CONSTANT
            },
            'applications': [
                'Neural Network Architectures',
                'Signal Processing',
                'Data Compression',
                'Biological Signal Analysis',
                'Brain-Computer Interfaces',
                'Fractal Mathematics'
            ]
        }


# Convenience functions
def edu(A: float, X: float) -> Tuple[float, float]:
    """Convenience function for EDU calculation"""
    formula = EDUFormula()
    return formula.calculate(A, X)


def edu_combined(A: float, X: float) -> float:
    """Convenience function for combined EDU value"""
    formula = EDUFormula()
    return formula.calculate_combined(A, X)


if __name__ == "__main__":
    # Demo the EDU Formula
    print("🧠 EDU Formula Demonstration")
    print("=" * 50)
    
    formula = EDUFormula()
    print(f"Formula: {formula.get_formula_string()}")
    print()
    
    # Example calculations
    test_cases = [
        (128, 440),   # Musical note A4
        (255, 10),    # High amplitude, low frequency
        (50, 1000),   # Low amplitude, high frequency
        (200, 144),   # DNA Adenine frequency
    ]
    
    for A, X in test_cases:
        mod, scal = formula.calculate(A, X)
        combined = mod * scal
        print(f"EDU({A:>3}, {X:>4}) = ({mod:.3f}, {scal:.2f}) → {combined:.2f}")
    
    print(f"\n📍 Discovered in Offenburg, Germany, 2024")
    print("🚀 Ready to revolutionize AI and signal processing!")
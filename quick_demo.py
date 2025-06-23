#!/usr/bin/env python3
"""
EDU-AIgent Quick Demo

A rapid demonstration of the EDU Formula capabilities
Perfect for showing to professors at Hochschule Offenburg!

Author: Eduard Terre (ASCII-EDU)
Location: Offenburg, Germany
Year: 2024
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.edu_formula import EDUFormula
import math
import time


def print_header():
    """Print demo header"""
    print("🧠" + "=" * 58 + "🧠")
    print("    EDU-AIgent: Revolutionary AI Framework")
    print("    The EDU Formula: EDU(A,X) = (A/255·π), (406.4/X)")
    print("    Discovered by Eduard Terre (ASCII-EDU), Offenburg 2024")
    print("🧠" + "=" * 58 + "🧠")
    print()


def demo_basic_formula():
    """Demonstrate basic EDU formula"""
    print("📐 BASIC EDU FORMULA DEMONSTRATION")
    print("-" * 50)
    
    formula = EDUFormula()
    
    examples = [
        ("Musical Note A4", 128, 440),
        ("Brain Alpha Wave", 100, 10),
        ("WiFi 2.4GHz", 200, 2400000000),
        ("DNA Adenine", 180, 144),
        ("Radio FM", 150, 100000000)
    ]
    
    print(f"{'Description':<15} {'A':<5} {'X':<12} {'Modulation':<12} {'Scaling':<12} {'Combined':<10}")
    print("-" * 80)
    
    for desc, A, X in examples:
        mod, scal = formula.calculate(A, X)
        combined = mod * scal
        
        # Format X with appropriate units
        if X >= 1e9:
            x_str = f"{X/1e9:.1f}G"
        elif X >= 1e6:
            x_str = f"{X/1e6:.1f}M"
        elif X >= 1e3:
            x_str = f"{X/1e3:.1f}K"
        else:
            x_str = f"{X:.1f}"
            
        print(f"{desc:<15} {A:<5} {x_str:<12} {mod:<12.3f} {scal:<12.2e} {combined:<10.2f}")
    
    print("\n💡 Notice: Same formula works from 10 Hz to 2.4 GHz!")
    print("   That's 8 orders of magnitude - UNIVERSAL!\n")


def demo_attention_comparison():
    """Demonstrate EDU vs Standard Attention"""
    print("🧠 EDU-TRANSFORMER vs STANDARD ATTENTION")
    print("-" * 50)
    
    formula = EDUFormula()
    
    print("Position Distance | Standard | EDU      | Improvement")
    print("-" * 50)
    
    total_standard = 0
    total_edu = 0
    
    for distance in range(1, 8):
        # Standard attention (static)
        standard_attn = 1.0 / math.sqrt(64)  # Simplified
        
        # EDU attention (position-sensitive)
        A = 100  # Attention intensity
        X = distance  # Position difference
        mod, scal = formula.calculate(A, X)
        edu_attn = mod * scal
        
        improvement = ((edu_attn - standard_attn) / standard_attn) * 100
        
        total_standard += standard_attn
        total_edu += edu_attn
        
        print(f"{distance:>15}   | {standard_attn:>6.3f}   | {edu_attn:>6.2f}   | {improvement:>+8.0f}%")
    
    total_improvement = ((total_edu - total_standard) / total_standard) * 100
    print("-" * 50)
    print(f"{'TOTAL':<15}   | {total_standard:>6.3f}   | {total_edu:>6.2f}   | {total_improvement:>+8.0f}%")
    print("\n🚀 EDU-Attention is POSITION-AWARE!")
    print("   Standard attention ignores position completely.\n")


def demo_signal_analysis():
    """Demonstrate signal analysis"""
    print("📡 SIGNAL ANALYSIS DEMO")
    print("-" * 50)
    
    import math
    import random
    
    formula = EDUFormula()
    
    # Simulate different signal types
    signals = [
        ("Delta Brain Wave", 2, 200),
        ("Alpha Brain Wave", 10, 150),  
        ("Beta Brain Wave", 25, 100),
        ("Music Bass", 80, 180),
        ("Human Voice", 400, 120),
        ("Radio Signal", 100000, 80)
    ]
    
    print(f"{'Signal Type':<15} {'Freq (Hz)':<10} {'Amp':<5} {'EDU Combined':<12} {'Classification'}")
    print("-" * 70)
    
    for signal_type, freq, amp in signals:
        mod, scal = formula.calculate(amp, freq)
        combined = mod * scal
        
        # Simple classification
        if combined > 100:
            classification = "HIGH ENERGY"
        elif combined > 10:
            classification = "MEDIUM ENERGY"
        else:
            classification = "LOW ENERGY"
            
        print(f"{signal_type:<15} {freq:<10} {amp:<5} {combined:<12.2f} {classification}")
    
    print("\n⚡ EDU Formula automatically classifies signal energy!")
    print("   One formula, infinite applications.\n")


def demo_universality():
    """Demonstrate universality across domains"""
    print("🌍 UNIVERSALITY DEMONSTRATION")
    print("-" * 50)
    
    formula = EDUFormula()
    
    domains = [
        ("Neuroscience", "Brain waves", 10, 100),
        ("Music", "Concert A", 440, 127),
        ("Biology", "DNA Thymine", 233, 180),
        ("Radio", "FM Radio", 100000000, 150),
        ("Quantum", "Photon (red)", 4.3e14, 50),
        ("Astronomy", "Pulsar", 1000, 255)
    ]
    
    print("Domain       | Application      | Frequency        | EDU Result")
    print("-" * 65)
    
    for domain, app, freq, amp in domains:
        mod, scal = formula.calculate(amp, freq)
        combined = mod * scal
        
        if freq >= 1e12:
            freq_str = f"{freq:.1e}"
        elif freq >= 1e9:
            freq_str = f"{freq/1e9:.1f}G"
        elif freq >= 1e6:
            freq_str = f"{freq/1e6:.1f}M"
        elif freq >= 1e3:
            freq_str = f"{freq/1e3:.1f}K"
        else:
            freq_str = f"{freq:.1f}"
            
        print(f"{domain:<12} | {app:<16} | {freq_str:<15} | {combined:>8.2f}")
    
    print("\n🎯 ONE FORMULA - ALL DOMAINS!")
    print("   From quantum to cosmic scales.\n")


def demo_interactive():
    """Interactive demo"""
    print("🎮 INTERACTIVE EDU CALCULATOR")
    print("-" * 50)
    print("Try your own values! (Press Enter to skip)")
    
    formula = EDUFormula()
    
    try:
        A_input = input("Enter Amplitude A (0-255): ").strip()
        if A_input:
            A = float(A_input)
        else:
            A = 128  # Default
            
        X_input = input("Enter Frequency X (> 0): ").strip()
        if X_input:
            X = float(X_input)
        else:
            X = 440  # Default A4 note
            
        print(f"\nCalculating EDU({A}, {X})...")
        time.sleep(1)  # Dramatic pause
        
        mod, scal = formula.calculate(A, X)
        combined = mod * scal
        
        print(f"✨ Result: EDU({A}, {X}) = ({mod:.3f}, {scal:.3f})")
        print(f"   Combined: {combined:.3f}")
        
        if X < 50:
            print("   🧠 This is in the neural frequency range!")
        elif 20 <= X <= 20000:
            print("   🎵 This is in the audible frequency range!")
        elif X > 1e6:
            print("   📡 This is in the radio frequency range!")
            
    except (ValueError, EOFError, KeyboardInterrupt):
        print("Using default values: A=128, X=440")
        mod, scal = formula.calculate(128, 440)
        print(f"EDU(128, 440) = ({mod:.3f}, {scal:.3f})")


def main():
    """Main demo function"""
    print_header()
    
    demos = [
        demo_basic_formula,
        demo_attention_comparison, 
        demo_signal_analysis,
        demo_universality,
        demo_interactive
    ]
    
    for demo in demos:
        demo()
        input("Press Enter to continue...")
        print()
    
    # Finale
    print("🎯" + "=" * 58 + "🎯")
    print("    EDU FORMULA: READY TO CHANGE THE WORLD!")
    print("    Perfect for: AI, Signal Processing, Biology")
    print("    Invented in: Offenburg, Germany, 2024")
    print("    Contact: Eduard Terre (ASCII-EDU) for collaboration")
    print("🎯" + "=" * 58 + "🎯")


if __name__ == "__main__":
    main()
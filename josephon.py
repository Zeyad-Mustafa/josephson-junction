import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from argparse import ArgumentParser

class JosephsonJunction:
    def __init__(self, Ic=1.0, Rn=1.0, C=1.0, Vn=0.001):
        """
        Initialize Josephson junction parameters
        :param Ic: Critical current (μA)
        :param Rn: Normal resistance (Ω)
        :param C: Capacitance (pF)
        :param Vn: Noise voltage (μV)
        """
        self.Ic = Ic * 1e-6  # Convert to A
        self.Rn = Rn
        self.C = C * 1e-12   # Convert to F
        self.Vn = Vn * 1e-6  # Convert to V
        self.phi0 = 2.068e-15  # Magnetic flux quantum (Wb)

    def dc_characteristic(self, V):
        """
        DC Josephson effect - supercurrent through junction
        :param V: Voltage across junction
        :return: Current through junction
        """
        if np.abs(V) < self.Vn:
            return self.Ic * np.sin(0)  # No voltage -> constant supercurrent
        else:
            return 0  # Voltage -> no supercurrent (only normal current)

    def iv_curve(self, V_range=(0, 5, 500)):
        """
        Generate I-V characteristic curve
        :param V_range: Voltage range (start, stop, num_points)
        :return: V, I arrays
        """
        V = np.linspace(*V_range)
        I = np.zeros_like(V)
        
        for i, v in enumerate(V):
            if v < self.Vn:
                # DC Josephson effect region
                I[i] = self.dc_characteristic(v) + v/self.Rn
            else:
                # Normal conduction + AC Josephson effect
                I[i] = v/self.Rn
        
        return V, I

    def phase_dynamics(self, I_bias, t_max=100e-9, dt=1e-11):
        """
        Simulate phase dynamics under constant bias current
        :param I_bias: Bias current (A)
        :param t_max: Simulation time (s)
        :param dt: Time step (s)
        :return: t, phi, V arrays
        """
        t = np.arange(0, t_max, dt)
        
        def dphi_dt(phi, t):
            return 2*np.pi/self.phi0 * (I_bias*self.Rn - self.Ic*self.Rn*np.sin(phi))
        
        phi0 = 0  # Initial phase
        phi = odeint(dphi_dt, phi0, t)
        V = self.phi0/(2*np.pi) * dphi_dt(phi.T[0], t)
        
        return t, phi, V

def plot_iv_curve(V, I):
    """Plot I-V characteristic curve"""
    plt.figure(figsize=(10, 6))
    plt.plot(V*1e6, I*1e6)  # Convert to μV and μA
    plt.title('Josephson Junction I-V Characteristic')
    plt.xlabel('Voltage (μV)')
    plt.ylabel('Current (μA)')
    plt.grid(True)
    plt.savefig('josephson_iv.png')
    plt.show()

def plot_phase_dynamics(t, phi, V):
    """Plot phase and voltage dynamics"""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    
    ax1.plot(t*1e9, phi)  # Convert to ns
    ax1.set_title('Phase Dynamics')
    ax1.set_ylabel('Phase (rad)')
    ax1.grid(True)
    
    ax2.plot(t*1e9, V*1e6)  # Convert to ns and μV
    ax2.set_title('Voltage Dynamics')
    ax2.set_xlabel('Time (ns)')
    ax2.set_ylabel('Voltage (μV)')
    ax2.grid(True)
    
    plt.tight_layout()
    plt.savefig('josephson_dynamics.png')
    plt.show()

def main():
    parser = ArgumentParser(description='Josephson Junction Simulator')
    parser.add_argument('--Ic', type=float, default=1.0, help='Critical current (μA)')
    parser.add_argument('--Rn', type=float, default=1.0, help='Normal resistance (Ω)')
    parser.add_argument('--C', type=float, default=1.0, help='Capacitance (pF)')
    parser.add_argument('--Vn', type=float, default=0.001, help='Noise voltage (μV)')
    parser.add_argument('--I_bias', type=float, default=1.5, help='Bias current for dynamics (μA)')
    
    args = parser.parse_args()
    
    jj = JosephsonJunction(Ic=args.Ic, Rn=args.Rn, C=args.C, Vn=args.Vn)
    
    # Plot I-V characteristic
    V, I = jj.iv_curve((0, 5, 500))  # 0-5 μV
    plot_iv_curve(V, I)
    
    # Simulate phase dynamics
    t, phi, V = jj.phase_dynamics(I_bias=args.I_bias*1e-6)  # Convert to A
    plot_phase_dynamics(t, phi, V)

if __name__ == "__main__":
    main()
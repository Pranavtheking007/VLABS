import numpy as np
import matplotlib.pyplot as plt

def BFSK_PLOT1(user_input,sample_rate,bit_rate,freq1,freq2,duration,amplitude,pulse_code):
    if user_input == 'Binary':
        bits = str(pulse_code)
        bitss = str(bits)
        t_bit = np.arange(0, len(bitss) / bit_rate, 1 / sample_rate)

        square=[]

        print(bits)

        print(len(t_bit))

        for i in bitss:
            for j in range(len(t_bit)):
                square.append(int(i))
                
        signal = np.array([])
        for bit in bitss:
            if bit == '0':
                signal = np.append(signal, amplitude * np.cos(2 * np.pi * freq1 * t_bit))
            else:
                signal = np.append(signal, amplitude * np.cos(2 * np.pi * freq2 * t_bit))
        
        # Generate time vector for the entire signal
        t = np.arange(0, len(signal) / sample_rate, 1 / sample_rate)

        # Plot the BFSK signal
        plt.plot(t, square)
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.suptitle('Square_Wave Pulses')
        plt.grid(True)
        plt.show()

    
    else:
        bits = np.random.randint(0, 2, int(bit_rate * duration))
        t_bit = np.arange(0, len(bits) / bit_rate, 1 / sample_rate)

        square=[]

        print(bits)

        print(len(t_bit))

        for i in bits:
            for j in range(len(t_bit)):
                square.append(i)

        # Generate BFSK signal
        signal = np.array([])
        for bit in bits:
            if bit == 0:
                signal = np.append(signal, amplitude * np.cos(2 * np.pi * freq1 * t_bit))
            else:
                signal = np.append(signal, amplitude * np.cos(2 * np.pi * freq2 * t_bit))

        # Generate time vector for the entire signal
        t = np.arange(0, len(signal) / sample_rate, 1 / sample_rate)



        # Plot the BFSK signal
        plt.plot(t, square)
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.suptitle('Sqaure-Wave Pulses')
        plt.grid(True)
        plt.show()

def BFSK_PLOT2(user_input,sample_rate,bit_rate,freq1,freq2,duration,amplitude,pulse_code):
    if user_input == 'Binary':
        bits = str(pulse_code)
        bitss = str(bits)
        t_bit = np.arange(0, len(bitss) / bit_rate, 1 / sample_rate)

        square=[]

        print(bits)

        print(len(t_bit))

        for i in bitss:
            for j in range(len(t_bit)):
                square.append(int(i))
                
        signal = np.array([])
        for bit in bitss:
            if bit == '0':
                signal = np.append(signal, amplitude * np.cos(2 * np.pi * freq1 * t_bit))
            else:
                signal = np.append(signal, amplitude * np.cos(2 * np.pi * freq2 * t_bit))
        
        # Generate time vector for the entire signal
        t = np.arange(0, len(signal) / sample_rate, 1 / sample_rate)

        plt.plot(t, signal)
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.title('Binary Frequency Shift Keying (BFSK) Signal')
        plt.grid(True)
        plt.show()
    
    else:
        bits = np.random.randint(0, 2, int(bit_rate * duration))
        t_bit = np.arange(0, len(bits) / bit_rate, 1 / sample_rate)

        square=[]

        print(bits)

        print(len(t_bit))

        for i in bits:
            for j in range(len(t_bit)):
                square.append(i)

        # Generate BFSK signal
        signal = np.array([])
        for bit in bits:
            if bit == 0:
                signal = np.append(signal, amplitude * np.cos(2 * np.pi * freq1 * t_bit))
            else:
                signal = np.append(signal, amplitude * np.cos(2 * np.pi * freq2 * t_bit))

        # Generate time vector for the entire signal
        t = np.arange(0, len(signal) / sample_rate, 1 / sample_rate)

        plt.plot(t, signal)
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.suptitle('Binary Frequency Shift Keying (BFSK) Signal')
        plt.grid(True)
        plt.show()
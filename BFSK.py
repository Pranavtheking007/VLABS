import numpy as np
import matplotlib.pyplot as plt

def plot_2(F2,user_input,amplitude,freq1,freq2,bit_rate,duration,sample_rate):
   if user_input == 'Binary':
        print('Binary')
        # Binary data inputs
        binary_data=[]
        F2 = int(F2)
        print('******************************')
        print('F2',F2)
        s = str(F2)
        for i in range(0,len(s)):
            binary_data.append(int(s[i]))
        print('************************')
        print('Binary Data:-')
        print(binary_data)
        # Convert binary data to a square wave
        square_wave = np.repeat(binary_data, 2)
        square_wave = np.concatenate(([square_wave[0]], square_wave))

        print("*********************")
        print('Square Wave')
        print(square_wave)
        print('********************')
        # Create time axis
        t1 = np.linspace(0, len(binary_data), len(square_wave), endpoint=False)
        print(t1)
        t2=np.arange(0,len(binary_data),0.001)
        print('FFFFFF')
        squares = list(square_wave)
        temp = 0
        waves = []
        for i in range(len(t1)):
            print('NP')
            times=np.arange(temp,t1[i],0.001)

            for j in range(len(times)):
                waves.append(squares[i])
            temp = t1[i]
        t2=np.arange(0,temp,0.001)
        print("*******************************************************")
        print('\n')
        print('\n')
        print(t2)
        print('\n')
        print(len(t2))
        print('\n')
        print(waves)
        print('\n')
        print(len(waves))
        print('\n')
        print('\n')
        # Adjust the length of waves to match the length of t2
        waves = waves[:len(t2)]

        # Plot square wave
        plt.plot(t2, waves, drawstyle='steps-post')
        plt.ylim(-0.1, 1.1)
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        plt.show()
    
   else:
        bits = np.random.randint(0, 2, int(bit_rate * duration))
        t_bit = np.arange(0, len(bits) / bit_rate, 1 / sample_rate)

        # Generate BFSK signal
        signal = np.array([])
        for bit in bits:
            if bit == 0:
                signal = np.append(signal, amplitude * np.cos(2 * np.pi * freq1 * t_bit))
            else:
                signal = np.append(signal, amplitude * np.cos(2 * np.pi * freq2 * t_bit))

        # Generate time vector for the entire signal
        t = np.arange(0, len(signal) / sample_rate, 1 / sample_rate)
   
        plt.plot(t, t_bit)
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.title('Binary Frequency Shift Keying (BFSK) Signal')
        plt.grid(True)
        plt.show()



def Plot3(sample_rate,bit_rate,freq1,freq2,duration,amplitude,user_input):
    if user_input =='Binary':
        print('Binary')
        # Binary data inputs
        binary_data=[]
        F2 = int(F2)
        print('******************************')
        print('F2',F2)
        s = str(F2)
        for i in range(0,len(s)):
            binary_data.append(int(s[i]))
        print('************************')
        print('Binary Data:-')
        print(binary_data)
        # Convert binary data to a square wave
        square_wave = np.repeat(binary_data, 2)
        square_wave = np.concatenate(([square_wave[0]], square_wave))

        print("*********************")
        print('Square Wave')
        print(square_wave)
        print('********************')
        # Create time axis
        t1 = np.linspace(0, len(binary_data), len(square_wave), endpoint=False)
        print(t1)
        t2=np.arange(0,len(binary_data),0.001)
        print('FFFFFF')
        squares = list(square_wave)
        temp = 0
        waves = []
        for i in range(len(t1)):
            print('NP')
            times=np.arange(temp,t1[i],0.001)

            for j in range(len(times)):
                waves.append(squares[i])
            temp = t1[i]
        t2=np.arange(0,temp,0.001)

        signal = np.array([])
        for bit in waves:
            if bit == 0:
                signal = np.append(signal, amplitude * np.cos(2 * np.pi * freq1 * t_bit))
            else:
                signal = np.append(signal, amplitude * np.cos(2 * np.pi * freq2 * t_bit))
        
        plt.plot(t2, signal)
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.title('Binary Frequency Shift Keying (BFSK) Signal')
        plt.grid(True)
        plt.show()



    else:
        # Generate bit stream
        bits = np.random.randint(0, 2, int(bit_rate * duration))
        t_bit = np.arange(0, len(bits) / bit_rate, 1 / sample_rate)
        print(t_bit)
        print(len(t_bit))

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
        plt.plot(t, signal)
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.title('Binary Frequency Shift Keying (BFSK) Signal')
        plt.grid(True)
        plt.show()
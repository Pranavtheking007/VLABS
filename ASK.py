import matplotlib
matplotlib.use('Agg',force=True)

import matplotlib.pyplot as plt
import numpy as num
from matplotlib.figure import Figure
import base64
from io import BytesIO

t=num.arange(0,1,0.001)

def ASK_Simulate1(A,F1,F2,user_input):
    if user_input == 'Binary':
        print("Binary Inputs")
        # Binary data inputs
        binary_data=[]
        F2 = int(F2)
        s = str(F2)
        for i in range(0,len(s)):
            binary_data.append(int(s[i]))

        # Create time axis
        # Convert binary data to a square wave
        square_wave = num.repeat(binary_data, 2)
        square_wave = num.concatenate(([square_wave[0]], square_wave))
        t1 = num.linspace(0, len(binary_data), len(square_wave), endpoint=False)
        t2=num.arange(0,len(binary_data),0.001)

        x=A*num.sin(2*num.pi*F1*t2)#Carrier Sine wave
        u=[]#Message signal
        b=[0.2,0.4,0.6,0.8,1.0]
        
         
        # fig = Figure()
        # ax = fig.subplots()
        # ax.plot(t2,x)
        # # Save it to a temporary buffer.
        # buf = BytesIO()
        # fig.savefig(buf, format="png")
        # # Embed the result in the html output.
        # data = base64.b64encode(buf.getbuffer()).decode("ascii")
        # print(data)
        # return f"<img src='data:image/png;base64,{data}'/>"
        plt.plot(t2,x);
        plt.xlabel('Time');
        plt.ylabel('Amplitude');
        plt.title('Carrier');
        plt.grid(True)
        plt.show()

       
    else:
        x=A*num.sin(2*num.pi*F1*t)#Carrier Sine wave
        u=[]#Message signal
        b=[0.2,0.4,0.6,0.8,1.0]
      

        plt.plot(t,x);
        plt.xlabel('Time');
        plt.ylabel('Amplitude');
        plt.title('Carrier');
        plt.grid(True)
        plt.show()

    return 'I will dance dance dance with my hands hands hands above my head'



def ASK_Simulate2(A,F1,F2,user_input):

    if user_input == 'Binary':
        # Binary data inputs
        binary_data=[]
        
        s = str(F2)
        for i in range(0,len(s)):
            binary_data.append(int(s[i]))
        
        # Convert binary data to a square wave
        square_wave = num.repeat(binary_data, 2)
        square_wave = num.concatenate(([square_wave[0]], square_wave))

      
        # Create time axis
        t1 = num.linspace(0, len(binary_data), len(square_wave), endpoint=False)
        t2=num.arange(0,len(binary_data),0.001)
        squares = list(square_wave)
        temp = 0
        waves = []
        for i in range(len(t1)):
            times=num.arange(temp,t1[i],0.001)

            for j in range(len(times)):
                waves.append(squares[i])
            temp = t1[i]
        t2=num.arange(0,temp,0.001)
       
        # Adjust the length of waves to match the length of t2
        waves = waves[:len(t2)]

        # Plot square wave
        plt.plot(t2, waves, drawstyle='steps-post')
        plt.ylim(-0.1, 1.1)
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        plt.show()

    else:
        #Plot square wave
        x=A*num.sin(2*num.pi*F1*t)#Carrier Sine wave
        u=[]#Message signal
        b=[0.2,0.4,0.6,0.8,1.0]
        s=1
        for i in t:
            if(i==b[0]):
                b.pop(0)
                if(s==0):
                    s=1
                else:
                    s=0
            u.append(s)
        v=[]#Sine wave multiplied with square wave
        for i in range(len(t)):
            v.append(A*num.sin(2*num.pi*F1*t[i])*u[i])
        
        plt.plot(t,u)
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        plt.title('Square wave Pulses')
        plt.grid(True)
        plt.show()

        return 'I will dance dance dance with my hands hands hands above my head'


def ASK_Simulate3(A, F1, F2, user_input):
    if user_input == 'Binary':
        # Binary data inputs
        binary_data = []
        s = str(F2)
        for i in range(0, len(s)):
            binary_data.append(int(s[i]))

        # Convert binary data to a square wave
        square_wave = num.repeat(binary_data, 2)
        square_wave = num.concatenate(([square_wave[0]], square_wave))
        t1 = num.linspace(0, len(binary_data), len(square_wave), endpoint=False)
        t2 = num.arange(0, len(binary_data), 0.001)

        # Create waves for each square pulse
        squares = list(square_wave)
        temp = 0
        waves = []
        for i in range(len(t1)):
            times = num.arange(temp, t1[i], 0.001)
            for j in range(len(times)):
                waves.append(squares[i])
            temp = t1[i]
        t2 = num.arange(0, temp, 0.001)

        # Adjust the length of waves to match the length of t2
        waves = waves[:len(t2)]

        # Multiply the carrier signal with square wave
        v = A * num.sin(2 * num.pi * F1 * t2) * waves
        x=A*num.sin(2*num.pi*F1*t2)#Carrier Sine wave
        u=[]#Message signal
        b=[0.2,0.4,0.6,0.8,1.0]
        fig , axs = plt.subplots(3,1,figsize=(50,100))
        fig.subplots_adjust(hspace=0.7,wspace=0.7)
        # Plot the ASK signal
        axs[0].plot(t2, waves, drawstyle='steps-post')
        axs[0].set_title('Amplitude')
        axs[0].set_xlabel('yo')
        axs[0].set_ylabel('Hi')

        axs[1].plot(t2, v)
        axs[1].set_title('Sqquare Plot')
        axs[1].set_xlabel('yo')
        axs[1].set_ylabel('Hi')

        axs[2].plot(t2,x)
        axs[2].set_title('ASK WavePlot')
        axs[2].set_xlabel('yo')
        axs[2].set_ylabel('Hi')

        plt.grid(True)
        plt.show()

    else:
        # Generate message signal
        t = num.arange(0, 1, 0.001)
        u = []
        b = [0.2, 0.4, 0.6, 0.8, 1.0]
        s = 1
        for i in t:
            if len(b) > 0 and i == b[0]:
                b.pop(0)
                s = 1 - s
            u.append(s)

        # Multiply the carrier signal with message signal
        v = A * num.sin(2 * num.pi * F1 * t) * u

        # Plot the ASK signal
        plt.plot(t, v)
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        plt.title('ASK Signal')
        plt.grid(True)
        plt.show()

    return 'I will dance dance dance with my hands hands hands above my head'

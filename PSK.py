import matplotlib.pyplot as plt
import numpy as num
t=num.arange(0,1,0.001)

def PSK_Simulate1(A,f1,F2,User_Input):

    if User_Input=='Binary':
        if User_Input == 'Binary':
            print('Binary')
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

            x=A*num.sin(2*num.pi*f1*t2)#Carrier Sine wave
                

            plt.plot(t2,x);
            plt.xlabel('Time');
            plt.ylabel('Amplitude');
            plt.title('Carrier');
            plt.grid(True)
            plt.show()

    else:
    
        print('Simulating Now!!!!!!!')
        x=A*num.sin(2*num.pi*f1*t)

        plt.plot(t,x);
        plt.xlabel("time");
        plt.ylabel("Amplitude");
        plt.title("Carrier");
        plt.grid(True)
        plt.show()


def PSK_Simulate2(A,f1,F2,User_Input):

    if User_Input=='Binary': 
        print('Binary')
        # Binary data inputs
        binary_data=[]
        print('******************************')
        print('F2',F2)
        s = str(F2)
        for i in range(0,len(s)):
            binary_data.append(int(s[i]))
        print('************************')
        print('Binary Data:-')
        print(binary_data)
        # Convert binary data to a square wave
        square_wave = num.repeat(binary_data, 2)
        square_wave = num.concatenate(([square_wave[0]], square_wave))

        print("*********************")
        print('Square Wave')
        print(square_wave)
        print('********************')
        # Create time axis
        t1 = num.linspace(0, len(binary_data), len(square_wave), endpoint=False)
        print(t1)
        t2=num.arange(0,len(binary_data),0.001)
        print('FFFFFF')
        squares = list(square_wave)
        temp = 0
        waves = []
        for i in range(len(t1)):
            print('NP')
            times=num.arange(temp,t1[i],0.001)

            for j in range(len(times)):
                waves.append(squares[i])
            temp = t1[i]
        t2=num.arange(0,temp,0.001)
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
                #print(s,i,b)
            u.append(s)

        plt.plot(t,u)
        plt.xlabel('time')
        plt.ylabel('Amplitude')
        plt.title('Message Signal')
        plt.grid(True)
        plt.show()

def PSK_Simulate3(A,f1,F2,User_Input):
    if User_Input == 'Binary':
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

        v=[]#Sine wave multiplied with square wave
        for i in range(len(t2)):
            if(waves[i]==1):
                v.append(A*num.sin(2*num.pi*f1*t2[i]))
            else:
                v.append(A*num.sin(2*num.pi*f1*t2[i])*-1)


        # Plot the ASK signal
        plt.plot(t2, v)
        plt.xlabel('Time')
        plt.ylabel('y')
        plt.title('Phase Shift Key')
        plt.grid(True)
        plt.show()


    else:

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
                #print(s,i,b)
            u.append(s)
        v=[]#Sine wave multiplied with square wave
        for i in range(len(t)):
            if(u[i]==1):
                v.append(A*num.sin(2*num.pi*f1*t[i]))
            else:
                v.append(A*num.sin(2*num.pi*f1*t[i])*-1)

        plt.plot(t,v);
        #plt.axis([0 1 -6 6]);
        plt.xlabel("t");
        plt.ylabel("y");
        plt.title("PSK");
        plt.grid(True)
        plt.show()
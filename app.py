#Imports
import sqlite3
from flask import Flask, render_template, request, session, redirect, flash
import pyrebase
import ASK
import PSK
import BFSK
#Setup
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index1():
        return render_template('index.html')

#Routes
@app.route('/loginPage.html')
def index2():
        return render_template('loginPage.html')

@app.route('/register.html')
def index3():
        return render_template('loginPage.html')

@app.route('/logout')
def logout():
        return render_template('index.html') 

config = {
    "apiKey": "AIzaSyAXFkvFb4dGvbedTeK92AMe0-tX7__J19w",
    "authDomain": "vlabs-4d54a.firebaseapp.com",
    "projectId": "vlabs-4d54a",
    "storageBucket": "vlabs-4d54a.appspot.com",
    "messagingSenderId": "773645748479",
    "appId": "1:773645748479:web:b11b5347cec6b6882864ca",
    "measurementId": "G-PJ4V7D84NC",
    "databaseURL": ""
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

app.secret_key = "secret_invasion"


@app.route('/register.html', methods=["POST"])
def register():
  if request.method == 'POST':    

        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirmPassword = request.form['confirm password']
        try:
           user = auth.create_user_with_email_and_password(email, password)
        except:
            flash("Registration Failed! Fill the details correctly", "danger")
            return render_template('loginPage.html')
        #   print(user)

        auth.send_email_verification(user['idToken'])
  flash("Registered Successfully", "success")
  return render_template('loginPage.html')

@app.route('/loginPage.html', methods=['GET','POST'])
def index():
        if (request.method == 'POST'):
            email = request.form['email']
            password = request.form['password']    
            try:
              user = auth.sign_in_with_email_and_password(email, password)
              session['user'] = email
            except:
              flash("Invalid Credentials", "danger")
              return render_template('loginPage.html')
        flash("Login Successful", "success")
        return render_template('extc.html')

@app.route('/experiments.html')
def experiment_page():
        return render_template('experiments.html')

@app.route('/quiz1.html')
def quiz1():
        return render_template('quiz1.html')

@app.route('/quiz1.html', methods=['POST'])
def quiz1_submit():
    score = 0
    if request.method == 'POST':
        q1 = request.form['q1']
        q2 = request.form['q2']
        q3 = request.form['q3']
        q4 = request.form['q4']
        q5 = request.form['q5']
        q6 = request.form['q6']
        q7 = request.form['q7']
        q8 = request.form['q8']
        q9 = request.form['q9']
        q10 = request.form['q10']

        if q1 == 'a':
            score += 1
        if q2 == 'b':
            score += 1
        if q3 == 'c':
            score += 1
        if q4 == 'a':
            score += 1
        if q5 == 'b':
            score += 1
        if q6 == 'c':
            score += 1
        if q7 == 'a':
            score += 1
        if q8 == 'b':
            score += 1
        if q9 == 'c':
            score += 1
        if q10 == 'a':
            score += 1
    return render_template('quiz1.html', score=score)

@app.route('/quiz2.html')
def quiz2():
        return render_template('quiz2.html')

@app.route('/quiz2.html', methods=['POST'])
def quiz2_submit():
        score = 0
        if request.method == 'POST':
            score = 0
        if request.method == 'POST':
            answer1 = request.form['answer1']
            answer2 = request.form['answer2']
            answer3 = request.form['answer3']
            answer4 = request.form['answer4']
            answer5 = request.form['answer5']
            answer6 = request.form['answer6']
            answer7 = request.form['answer7']
            answer8 = request.form['answer8']
            answer9 = request.form['answer9']
            answer10 = request.form['answer10']

            if answer1 == 'a':
                score += 1
            if answer2 == 'b':
                score += 1
            if answer3 == 'c':
                score += 1
            if answer4 == 'a':
                score += 1
            if answer5 == 'b':
                score += 1
            if answer6 == 'c':
                score += 1
            if answer7 == 'a':
                score += 1
            if answer8 == 'b':
                score += 1
            if answer9 == 'c':
                score += 1
            if answer10 == 'a':
                score += 1
        return render_template('quiz2.html', score=score)

@app.route('/quiz3.html')
def quiz3():
        return render_template('quiz3.html')

@app.route('/quiz3.html', methods=['POST'])
def quiz3_submit():
        score = 0
        if request.method == 'POST':
            score = 0
        if request.method == 'POST':
            answer1 = request.form['answer1']
            answer2 = request.form['answer2']
            answer3 = request.form['answer3']
            answer4 = request.form['answer4']
            answer5 = request.form['answer5']
            answer6 = request.form['answer6']
            answer7 = request.form['answer7']
            answer8 = request.form['answer8']
            answer9 = request.form['answer9']
            answer10 = request.form['answer10']

            if answer1 == 'a':
                score += 1
            if answer2 == 'b':
                score += 1
            if answer3 == 'c':
                score += 1
            if answer4 == 'a':
                score += 1
            if answer5 == 'b':
                score += 1
            if answer6 == 'c':
                score += 1
            if answer7 == 'a':
                score += 1
            if answer8 == 'b':
                score += 1
            if answer9 == 'c':
                score += 1
            if answer10 == 'a':
                score += 1
        return render_template('quiz3.html', score=score)

@app.route('/quiz4.html')
def quiz4():
        return render_template('quiz4.html')

@app.route('/quiz4.html', methods=['POST'])
def quiz4_submit():
        score = 0
        if request.method == 'POST':
            score = 0
        if request.method == 'POST':
            answer1 = request.form['answer1']
            answer2 = request.form['answer2']
            answer3 = request.form['answer3']
            answer4 = request.form['answer4']
            answer5 = request.form['answer5']
            answer6 = request.form['answer6']
            answer7 = request.form['answer7']
            answer8 = request.form['answer8']
            answer9 = request.form['answer9']
            answer10 = request.form['answer10']

            if answer1 == 'a':
                score += 1
            if answer2 == 'b':
                score += 1
            if answer3 == 'c':
                score += 1
            if answer4 == 'a':
                score += 1
            if answer5 == 'b':
                score += 1
            if answer6 == 'c':
                score += 1
            if answer7 == 'a':
                score += 1
            if answer8 == 'b':
                score += 1
            if answer9 == 'c':
                score += 1
            if answer10 == 'a':
                score += 1
        return render_template('quiz4.html', score=score)

@app.route('/quiz5.html')
def quiz5():
        return render_template('quiz5.html')

@app.route('/quiz5.html', methods=['POST'])
def quiz5_submit():
        score = 0
        if request.method == 'POST':
            score = 0
        if request.method == 'POST':
            answer1 = request.form['answer1']
            answer2 = request.form['answer2']
            answer3 = request.form['answer3']
            answer4 = request.form['answer4']
            answer5 = request.form['answer5']
            answer6 = request.form['answer6']
            answer7 = request.form['answer7']
            answer8 = request.form['answer8']
            answer9 = request.form['answer9']
            answer10 = request.form['answer10']

            if answer1 == 'a':
                score += 1
            if answer2 == 'b':
                score += 1
            if answer3 == 'c':
                score += 1
            if answer4 == 'a':
                score += 1
            if answer5 == 'b':
                score += 1
            if answer6 == 'c':
                score += 1
            if answer7 == 'a':
                score += 1
            if answer8 == 'b':
                score += 1
            if answer9 == 'c':
                score += 1
            if answer10 == 'a':
                score += 1
        return render_template('quiz5.html', score=score)

@app.route('/quiz6.html')
def quiz6():
        return render_template('quiz6.html')

@app.route('/quiz6.html', methods=['POST'])
def quiz6_submit():
        score = 0
        if request.method == 'POST':
            score = 0
        if request.method == 'POST':
            answer1 = request.form['answer1']
            answer2 = request.form['answer2']
            answer3 = request.form['answer3']
            answer4 = request.form['answer4']
            answer5 = request.form['answer5']
            answer6 = request.form['answer6']
            answer7 = request.form['answer7']
            answer8 = request.form['answer8']
            answer9 = request.form['answer9']
            answer10 = request.form['answer10']

            if answer1 == 'a':
                score += 1
            if answer2 == 'b':
                score += 1
            if answer3 == 'c':
                score += 1
            if answer4 == 'a':
                score += 1
            if answer5 == 'b':
                score += 1
            if answer6 == 'c':
                score += 1
            if answer7 == 'a':
                score += 1
            if answer8 == 'b':
                score += 1
            if answer9 == 'c':
                score += 1
            if answer10 == 'a':
                score += 1
        return render_template('quiz6.html', score=score)

@app.route('/quiz7.html')
def quiz7():
        return render_template('quiz7.html')

@app.route('/quiz7.html', methods=['POST'])
def quiz7_submit():
        score = 0
        if request.method == 'POST':
            score = 0
        if request.method == 'POST':
            answer1 = request.form['answer1']
            answer2 = request.form['answer2']
            answer3 = request.form['answer3']
            answer4 = request.form['answer4']
            answer5 = request.form['answer5']
            answer6 = request.form['answer6']
            answer7 = request.form['answer7']
            answer8 = request.form['answer8']
            answer9 = request.form['answer9']
            answer10 = request.form['answer10']

            if answer1 == 'a':
                score += 1
            if answer2 == 'b':
                score += 1
            if answer3 == 'c':
                score += 1
            if answer4 == 'a':
                score += 1
            if answer5 == 'b':
                score += 1
            if answer6 == 'c':
                score += 1
            if answer7 == 'a':
                score += 1
            if answer8 == 'b':
                score += 1
            if answer9 == 'c':
                score += 1
            if answer10 == 'a':
                score += 1
        return render_template('quiz7.html', score=score)

@app.route('/quiz8.html')
def quiz8():
        return render_template('quiz8.html')

@app.route('/quiz8.html', methods=['POST'])
def quiz8_submit():
        score = 0
        if request.method == 'POST':
            score = 0
        if request.method == 'POST':
            answer1 = request.form['answer1']
            answer2 = request.form['answer2']
            answer3 = request.form['answer3']
            answer4 = request.form['answer4']
            answer5 = request.form['answer5']
            answer6 = request.form['answer6']
            answer7 = request.form['answer7']
            answer8 = request.form['answer8']
            answer9 = request.form['answer9']
            answer10 = request.form['answer10']

            if answer1 == 'a':
                score += 1
            if answer2 == 'b':
                score += 1
            if answer3 == 'c':
                score += 1
            if answer4 == 'a':
                score += 1
            if answer5 == 'b':
                score += 1
            if answer6 == 'c':
                score += 1
            if answer7 == 'a':
                score += 1
            if answer8 == 'b':
                score += 1
            if answer9 == 'c':
                score += 1
            if answer10 == 'a':
                score += 1
        return render_template('quiz8.html', score=score)

@app.route('/quiz9.html')
def quiz9():
        return render_template('quiz9.html')

@app.route('/quiz9.html', methods=['POST'])
def quiz9_submit():
        score = 0
        if request.method == 'POST':
            score = 0
        if request.method == 'POST':
            answer1 = request.form['answer1']
            answer2 = request.form['answer2']
            answer3 = request.form['answer3']
            answer4 = request.form['answer4']
            answer5 = request.form['answer5']
            answer6 = request.form['answer6']
            answer7 = request.form['answer7']
            answer8 = request.form['answer8']
            answer9 = request.form['answer9']
            answer10 = request.form['answer10']

            if answer1 == 'a':
                score += 1
            if answer2 == 'b':
                score += 1
            if answer3 == 'c':
                score += 1
            if answer4 == 'a':
                score += 1
            if answer5 == 'b':
                score += 1
            if answer6 == 'c':
                score += 1
            if answer7 == 'a':
                score += 1
            if answer8 == 'b':
                score += 1
            if answer9 == 'c':
                score += 1
            if answer10 == 'a':
                score += 1
        return render_template('quiz9.html', score=score)

@app.route('/quiz10.html')
def quiz10():
        return render_template('quiz10.html')

@app.route('/quiz10.html', methods=['POST'])
def quiz10_submit():
        score = 0
        if request.method == 'POST':
            score = 0
        if request.method == 'POST':
            answer1 = request.form['answer1']
            answer2 = request.form['answer2']
            answer3 = request.form['answer3']
            answer4 = request.form['answer4']
            answer5 = request.form['answer5']
            answer6 = request.form['answer6']
            answer7 = request.form['answer7']
            answer8 = request.form['answer8']
            answer9 = request.form['answer9']
            answer10 = request.form['answer10']

            if answer1 == 'a':
                score += 1
            if answer2 == 'b':
                score += 1
            if answer3 == 'c':
                score += 1
            if answer4 == 'a':
                score += 1
            if answer5 == 'b':
                score += 1
            if answer6 == 'c':
                score += 1
            if answer7 == 'a':
                score += 1
            if answer8 == 'b':
                score += 1
            if answer9 == 'c':
                score += 1
            if answer10 == 'a':
                score += 1
        return render_template('quiz10.html', score=score)

from flask import send_file

@app.route("/get_images")
def get_image():
        if request.args.get('type')=='1':
                filename = ''
        else:
                return("correct h")        

@app.route('/index.html')
def login():
    return render_template("index.html")
#extc page to experiments page...........
@app.route('/extc.html')
def exteriments():
    return render_template("extc.html")


#experiments avaliablle with simulation: expt2 ,expt4 ,expt7 ,expt9
#experiments avaliablle without simulation: expt1 ,expt3 ,expt5 ,expt6 ,expt8 ,expt10

#flow for expt:

#experiments page ---------> expt1 ---------->sim1 --------> form entry -------->output/results



@app.route('/exp1.html')
def exp1():
    return render_template("exp1.html")

@app.route('/sim1.html')
def sim1():
    return render_template("sim1.html")


#experiments page ---------> expt2 ---------->sim2 --------> form entry -------->output/results



@app.route('/exp2.html')
def exp2():
    return render_template("exp2.html") 

@app.route('/sim2.html')
def sim2():
    return render_template("sim2.html") 

@app.route('/sim2.html' ,methods = ["GET" , 'POST'])
def outform():
# -------------------------->       function to display form and get inputs from user
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        Amplitude_of_carrier_signal = float(request.form["Amplitude_of_carrier_signal"])
        frequency_of_carrier_signal = float(request.form["frequency_of_carrier_signal"])      
        frequency_of_Pulse_Signal   = str(request.form["frequency_of_Pulse_Signal"])
        print('*****************************')
        print('User Input')
        print(Amplitude_of_carrier_signal)
        print(frequency_of_carrier_signal)
        print(frequency_of_Pulse_Signal)
        print("***********************************")
        print('\n')
            #print(frequency_of_carrier_signal)
        print(user_input, "POST")
        ASK.ASK_Simulate1(Amplitude_of_carrier_signal,frequency_of_carrier_signal,frequency_of_Pulse_Signal,user_input), ASK.ASK_Simulate2(Amplitude_of_carrier_signal,frequency_of_carrier_signal,frequency_of_Pulse_Signal,user_input), ASK.ASK_Simulate3(Amplitude_of_carrier_signal,frequency_of_carrier_signal,frequency_of_Pulse_Signal,user_input)
        return render_template('sim2.html')
    else:
        user_input = request.form.get('user_input')
        print(user_input, "123456789")
        return 'fail'
    
#experiments page ---------> expt3 ---------->sim3 --------> form entry -------->output/results

@app.route('/exp3.html')
def exp3():
    return render_template("exp3.html")

@app.route('/sim3.html')
def sim3():
    return render_template("sim3.html")

@app.route('/sim3.html',methods=["GET","POST"])
def sim3_1():
     if request.method == "POST":
        User_input = request.form.get('user_input')
        Samples = float(request.form['Sample'])
        Bit_Rate = float(request.form['Bit_Rate'])
        frequency_1 = float(request.form['frequency_1'])
        frequency_2 = float(request.form['frequency_2'])
        Duration = float(request.form['Duration'])
        Amplitude = float(request.form['Amplitude'])
        Pulse_Code = str(request.form['Pulse Code'])

        print('___________________________________________________________________')
        print(User_input)
        print('___________________________________________________________________')
        print('\n')
        print('\n')

        BFSK.BFSK_PLOT1(User_input,Samples,Bit_Rate,frequency_1,frequency_2,Duration,Amplitude,Pulse_Code),BFSK.BFSK_PLOT2(User_input,Samples,Bit_Rate,frequency_1,frequency_2,Duration,Amplitude,Pulse_Code)

        return render_template('sim3.html')

  
#experiments page ---------> expt4 ---------->sim4 --------> form entry -------->output/results

@app.route('/exp4.html')
def exp4():
    return render_template("exp4.html")

@app.route('/sim4.html')
def sim4():
    return render_template("sim4.html")  

@app.route('/sim4.html' ,methods = ["GET" , 'POST'])
# -------------------------->       function to display form and get inputs from user
def outform1():   
    if request.method == 'POST':  
        user_input = request.form.get('user_input')
        Amplitude_of_carrier_signal = float(request.form["Amplitude_of_carrier_signal"])     
        frequency_of_carrier_signal = float(request.form["frequency_of_carrier_signal"])      
        frequency_of_Pulse_Signal   = str(request.form["frequency_of_Pulse_Signal"])
        print('*****************************')
        print('User Input')
        print(user_input)
        print(frequency_of_carrier_signal)
        print(frequency_of_Pulse_Signal)
        print("**********************************")
        print('\n')
            #print(frequency_of_carrier_signal)
        print(user_input, "POST")
        PSK.PSK_Simulate1(Amplitude_of_carrier_signal,frequency_of_carrier_signal,frequency_of_Pulse_Signal,user_input), PSK.PSK_Simulate2(Amplitude_of_carrier_signal,frequency_of_carrier_signal,frequency_of_Pulse_Signal,user_input), PSK.PSK_Simulate3(Amplitude_of_carrier_signal,frequency_of_carrier_signal,frequency_of_Pulse_Signal,user_input)
        return render_template('sim4.html')
    else:
        user_input = request.form.get('user_input')
        print(user_input, "123456789")
        return 'fail'
           


#experiments page ---------> expt5 ---------->sim5 --------> form entry -------->output/results

@app.route('/exp5.html')
def exp5():
    return render_template("exp5.html")

@app.route('/sim5.html')
def sim5():
    return render_template("sim5.html")

#experiments page ---------> expt6 ---------->sim6 --------> form entry -------->output/results

@app.route('/exp6.html')
def exp6():
    return render_template("exp6.html")

@app.route('/sim6.html')
def sim6():
    return render_template("sim6.html")

#experiments page ---------> expt7 ---------->sim7 --------> form entry -------->output/results

@app.route('/exp7.html')
def exp7():
    return render_template("exp7.html")

@app.route('/sim7.html')
def sim7():
    return render_template("sim7.html")

#experiments page ---------> expt8 ---------->sim8 --------> form entry -------->output/results

@app.route('/exp8.html')
def exp8():
    return render_template("exp8.html")

@app.route('/sim8.html')
def sim8():
    return render_template("sim8.html")

#experiments page ---------> expt9 ---------->sim9 --------> form entry -------->output/results


@app.route('/exp9.html')
def exp9():
    return render_template("exp9.html")

@app.route('/sim9.html')
# -------------------------->       function to display form and get inputs from user
def sim9():
    return render_template("sim9.html") 

@app.route('/sim9.html' ,methods = ["GET" , 'POST'])
# -------------------------->       function to display form and get inputs from user
def outform2():
    if request.method == 'POST':
        enter_the_first_probability = request.form["enter_the_first_probability"]
        enter_the_second_probability = request.form["enter_the_second_probability"]
        enter_the_third_probability  = request.form["enter_the_third_probability"]
        enter_the_forth_probability  = request.form["enter_the_forth_probability"]
        enter_the_fifth_probability   = request.form["enter_the_fifth_probability"]


#experiments page ---------> expt10 ---------->sim10 --------> form entry -------->output/results

@app.route('/exp10.html')
def exp10():
    return render_template("exp10.html")

@app.route('/sim10.html')
def sim10():
    return render_template("sim10.html")

if __name__ == "__main__":
    app.run(debug = True) 
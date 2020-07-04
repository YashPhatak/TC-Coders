import os
import secrets
from PIL import Image
from flask import render_template,url_for,flash,redirect,request
from EDUPOINT import app,db,bcrypt,mail
from EDUPOINT.forms import (RegistrationForm, LoginForm,UpdateAccountForm,
                            RequestResetForm,ResetPasswordForm)
from EDUPOINT.models import User
from flask_login import login_user,current_user,logout_user,login_required
from flask_mail import Message
import sqlite3 as sql

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',title='Home')

@app.route("/cart",methods=['GET','POST'])
def cart():
    if current_user.is_authenticated:
      
        
        con = sql.connect("userinfo.db")
        con.row_factory = sql.Row
   
        cur = con.cursor()
        
        cur.execute("select PNAME from products")
   
        rows = cur.fetchall()
        return render_template("list.html",rows = rows) 
            
    else:
        return redirect(url_for('login'))

@app.route("/list",methods=['GET','POST'])
def list():
 if request.method=='POST':
   prodid=request.form['PID']
   con = sql.connect("userinfo.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   prodid=request.form['PID']
   cur.execute("select PROD_NAME from products where PID='"+prodid+"'")
   
   rows = cur.fetchall()
   return render_template("list.html",rows = rows)

@app.route("/home/menu")
def menu():
    return render_template('menu.html', title='Menu')


@app.route("/home/menu/VJTI Books")
def VJTI_Books():
    return render_template('EDUPOINT VJTI books.html',title="VJTI Books")

@app.route("/home/menu/VJTI Books/Object-Oriented Programming with C++")
def balg():
    return render_template('balg.html',title="Object Oriented Progamming with C++")

@app.route("/home/menu/VJTI Books/Fundamentals of Electric Circuits")
def alex():
    return render_template('beeal.html',title="Fundamentals of Electric Circuits")

@app.route("/home/menu/VJTI Books/Design of Machine Elements")
def bhandari():
    return render_template('bhandari.html',title="Design of Machine Elements")

@app.route("/home/menu/VJTI Books/Object Oriented Paradigm With C++ Beginners Guide For C & C++")
def bmeshram():
    return render_template('bmeshram.html',title="Object Oriented Paradigm With C++ Beginners Guide For C & C++")

@app.route("/home/menu/VJTI Books/A Textbook Of Engineering Chemistry By Shashi Chawla")
def chawla():
    return render_template('chawla.html',title="A Textbook Of Engineering Chemistry By Shashi Chawla")

@app.route("/home/menu/VJTI Books/Basic Mechanical Engineering")
def dom():
    return render_template('dom.html',title="Basic Mechanical Engineering")

@app.route("/home/menu/VJTI Books/Engineering Drawing by N.D.Bhatt")
def egbhatt():
    return render_template('egbhatt.html',title="Engineering Drawing by N.D.Bhatt")

@app.route("/home/menu/VJTI Books/Engineering Drawing By N.H.Dubey")
def egdubey():
    return render_template('egdubey.html',title="Engineering Drawing By N.H.Dubey")

@app.route("/home/menu/VJTI Books/Higher Engineering Mathematics By B.S.Grewal")
def grewal():
    return render_template('grewal.html',title="Higher Engineering Mathematics By B.S.Grewal")

@app.route("/home/menu/VJTI Books/Engineering Chemistry By Jain and Jain")
def jain():
    return render_template('jain.html',title="Engineering Chemistry By Jain and Jain")

@app.route("/home/menu/VJTI Books/A Textbook of Engineering Physics")
def kshirsagar():
    return render_template('kshirsagar.html',title="A Textbook of Engineering Physics")

@app.route("/home/menu/VJTI Books/Applied Mathematics-1 By G.V.Kumbhojkar")
def kumbhojkar():
    return render_template('kumbhojkar.html',title="Applied Mathematics-1 By G.V.Kumbhojkar")

@app.route("/home/menu/VJTI Books/Applied Mathematics-2 By G.V.Kumbhojkar")
def kumbhojkar2():
    return render_template('kumbhojkar2.html',title="Applied Mathematics-2 By G.V.Kumbhojkar")

@app.route("/home/menu/VJTI Books/Let Us C++")
def lsc():
    return render_template('lsc+.html',title="Let Us C++")

@app.route("/home/menu/VJTI Books/Engineering Mechanics By M.D.Dayal")
def mechdayal():
    return render_template('mechdayal.html',title="Engineering Mechanics By M.D.Dayal")

@app.route("/home/menu/VJTI Books/Engineering Mechanics Statics and Dynamics By N.H.Dubey")
def mechdubey():
    return render_template('mechdubey.html',title="Engineering Mechanics Statics and Dynamics By N.H.Dubey")

@app.route("/home/menu/VJTI Books/Basic Electrical Engineering By Ravish Singh")
def ravish():
    return render_template('ravish.html',title="Basic Electrical Engineering By Ravish Singh")

@app.route("/home/menu/VJTI Books/SOLUTIONS Engineering Mechanics by M. D. Dayal")
def soldayal():
    return render_template('soldayal.html',title="SOLUTIONS Engineering Mechanics by M. D. Dayal")

@app.route("/home/menu/VJTI Books/Companion to Applied Mathematics 1 by G. V. Kumbhojkar")
def solkumb1():
    return render_template('solkumb1.html',title="Companion to Applied Mathematics 1 by G. V. Kumbhojkar")

@app.route("/home/menu/VJTI Books/Companion to Applied Mathematics 2 by G. V. Kumbhojkar")
def solkumb2():
    return render_template('solkumb2.html',title="Companion to Applied Mathematics 2 by G. V. Kumbhojkar")

@app.route("/home/menu/VJTI Books/Applied Physics-1")
def wavhal():
    return render_template('wavhal.html',title="Applied Physics-1")

@app.route("/home/menu/VJTI Books/Applied Physics-2")
def wavhal2():
    return render_template('wavhal2.html',title="Applied Physics-2")

@app.route("/home/menu/Engineering Equipments")
def engeq():
    return render_template('Engineering Equipments.html',title="Engineering Equipments")

@app.route("/home/menu/Engineering Equipments/Physics")
def phy():
    return render_template('EDUPOINT Physics Equipment.html',title="Engineering Equipments") 

@app.route("/home/menu/Engineering Equipments/Electronics")
def etrx():
    return render_template('EDUPOINT Electronics Equipment.html',title="Engineering Equipments")

@app.route("/home/menu/Engineering Equipments/Electronics/Accelerometer")
def acc():
    return render_template('accelerometer.html',title="Accelerometer")

@app.route("/home/menu/Engineering Equipments/Electronics/Arduino Board")
def ard():
    return render_template('Aurdinobored.html',title="Arduino Board") 

@app.route("/home/menu/Engineering Equipments/Electronics/Breadboard")
def brdb():
    return render_template('breadbored.html',title="Breadboard")  

@app.route("/home/menu/Engineering Equipments/Electronics/Digital Multimeter")
def digm():
    return render_template('digital multimeter.html',title="Digital Multimeter")     

@app.route("/home/menu/Engineering Equipments/Electronics/IR Sensor")
def irsensor():
    return render_template('IR sensor.html',title="IR Sensor")

@app.route("/home/menu/Engineering Equipments/Electronics/Lidar Sensor")
def lidarsensor():
    return render_template('lidar sensor.html',title="Lidar Sensor")

@app.route("/home/menu/Engineering Equipments/Electronics/Raspberry Pi")
def rsp():
    return render_template('rasbery pi.html',title="Raspberry Pi")    

@app.route("/home/menu/Engineering Equipments/Electronics/Soldering Iron")
def sldiron():
    return render_template('soldering iron.html',title="Soldering Iron") 

@app.route("/home/menu/Engineering Equipments/Electronics/SquadPixel ESP-32 WiFi , Bluetooth, Dual Core Chip Development Board")
def esp():
    return render_template('SquadPixel ESP-32 WiFi , Bluetooth, Dual Core Chip Development Board.html',title="SquadPixel ESP-32 WiFi , Bluetooth, Dual Core Chip Development Board") 

@app.route("/home/menu/Engineering Equipments/Electronics/Transistor")
def trns():
    return render_template('transister.html',title="Transistor") 

@app.route("/home/menu/Engineering Equipments/Physics/C.R.O")
def cro():
    return render_template('cro.html',title="C.R.O")

@app.route("/home/menu/Engineering Equipments/Physics/Diodes")
def diode():
    return render_template('Diodes.html',title="Diodes")    

@app.route("/home/menu/Engineering Equipments/Physics/Four Probe Apparatus")
def fpa():
    return render_template('fourproube.html',title="Four Probe Apparatus") 

@app.route("/home/menu/Engineering Equipments/Physics/Micrometer Screw Gauge")
def mgauge():
    return render_template('Micrometerscrewgauge.html',title="Micrometer Screw Gauge")

@app.route("/home/menu/Engineering Equipments/Physics/Vernier Caliper")
def vc():
    return render_template('verniercaliper.html',title="Vernier Caliper")

@app.route("/home/menu/Engineering Equipments/Physics/Polarimeter")
def polr():
    return render_template('polarimeter.html',title="Polarimeter")

@app.route("/home/menu/Engineering Equipments/Physics/Rheostat")
def rhst():
    return render_template('Rheostat.html',title="Rheostat")

@app.route("/home/menu/Engineering Equipments/Physics/Spectroscope")
def spec():
    return render_template('spectroscope.html',title="Spectroscope")

@app.route("/home/menu/Engineering Equipments/Physics/Travelling Microscope")
def travelingmicroscope():
    return render_template('travelingmicroscope.html',title="Travelling Microscope")

@app.route("/home/menu/generalbooks")
def generalbooks():
    return render_template('generalbooks.html', title='Generalbooks')

@app.route("/home/menu/generalbooks/Barrons Reading Workbook For The New SAT")
def BarronsReadingWorkbookForTheNewSAT():
    return render_template('Book_1.html', title='Barrons Reading Workbook For The New SAT')

@app.route("/home/menu/generalbooks/Coronavirus:What You Need To Know About The Global Pandemic")
def CoronavirusPandemic():
    return render_template('Book_2.html', title='Coronavirus:What You Need To Know About The Global Pandemic')

@app.route("/home/menu/generalbooks/Shuttling To The Top:The Story Of P.V.Sindhu")
def ShuttlingToTopTheStoryOfPVSindhu():
    return render_template('Book_3.html', title='Shuttling To The Top:The Story Of P.V.Sindhu')

@app.route("/home/menu/generalbooks/The Lost Symbol")
def LostSymbol():
    return render_template('Book_4.html', title='The Lost Symbol')

@app.route("/home/menu/generalbooks/The Da Vinci Code")
def DaVinciCode():
    return render_template('Book_5.html', title='The Da Vinci Code')

@app.route("/home/menu/generalbooks/Upstream")
def Upstream():
    return render_template('Book_6.html', title='Upstream')

@app.route("/home/menu/generalbooks/Ikigai : The Japanese Secret To A Long And Happy Life")
def Ikigai():
    return render_template('Book_7.html', title='Ikigai : The Japanese Secret To A Long And Happy Life')

@app.route("/home/menu/generalbooks/The Alchemist")
def TheAlchemist():
    return render_template('Book_8.html', title='The Alchemist')

@app.route("/home/menu/generalbooks/The Great Gatsby")
def TheGreatGatsby():
    return render_template('Book_9.html', title='The Great Gatsby')

@app.route("/home/menu/generalbooks/Ghost Flight")
def GhostFlight():
    return render_template('Book_10.html', title='Ghost Flight')

@app.route("/home/menu/generalbooks/Immortals Of Meluha Book 1 Of The Shiva Trilogy")
def ImmortalsOfMeluha():
    return render_template('Book_11.html', title='Immortals Of Meluha Book 1 Of The Shiva Trilogy')

@app.route("/home/menu/generalbooks/Secret Of The Nagas Book 2 Of The Shiva Trilogy")
def SecretOfTheNagas():
    return render_template('Book_12.html', title='Secret Of The Nagas Book 2 Of The Shiva Trilogy')

@app.route("/home/menu/generalbooks/Oath Of The Vayuputras Book 3 Of The Shiva Trilogy")
def OathOfTheVayuputras():
    return render_template('Book_13.html', title='Oath Of The Vayuputras Book 3 Of The Shiva Trilogy')

@app.route("/home/menu/generalbooks/Game Query : The Mind Stretching Economist Quiz")
def GameQuery():
    return render_template('Book_14.html', title='Game Query : The Mind Stretching Economist Quiz')

@app.route("/home/menu/generalbooks/World Puzzle Championship Challenge : Are You As Bright As The Best")
def WorldPuzzleChampionshipChallenge():
    return render_template('Book_15.html', title='World Puzzle Championship Challenge : Are You As Bright As The Best')

@app.route("/home/menu/generalbooks/LEGACY")
def LEGACY():
    return render_template('Book_16.html', title='LEGACY')

@app.route("/home/menu/generalbooks/Three Thousand Stitches : Ordinary People Extraordinary Lives")
def ThreeThousandStitches():
    return render_template('Book_17.html', title='Three Thousand Stitches : Ordinary People Extraordinary Lives')

@app.route("/home/menu/generalbooks/Hardy Boys : Great Airport Mystery")
def HardyBoysGreatAirportMystery():
    return render_template('Book_18.html', title='Hardy Boys : Great Airport Mystery')

@app.route("/home/menu/generalbooks/Hardy Boys : While The Clock Ticked")
def HardyBoysWhileTheClockTicked():
    return render_template('Book_19.html', title='Hardy Boys : While The Clock Ticked')

@app.route("/home/menu/generalbooks/Hardy Boys : Mysterious Caravan")
def HardyBoysMysteriousCaravan():
    return render_template('Book_20.html', title='Hardy Boys : Mysterious Caravan')

@app.route("/home/menu/generalbooks/Hardy Boys : Clue Of The Broken Blade")
def HardyBoysClueOfBrokeBlade():
    return render_template('Book_21.html', title='Hardy Boys : Clue Of The Broken Blade')

@app.route("/home/menu/stationery")
def stationery():
    return render_template('stationery.html', title='Stationery')

@app.route("/home/menu/stationery/Apsara Pencil")
def ApsaraPencil():
    return render_template('Apsara.html', title='Apsara Pencil')

@app.route("/home/menu/stationery/Amblitz Ambi Spiral Unruled Notebook")
def AmblitzAmbiSpiralUnruledNotebook():
    return render_template('blank notebook.html', title='Amblitz Ambi Spiral Unruled Notebook')

@app.route("/home/menu/stationery/Butterflow Pen")
def ButterflowPen():
    return render_template('butterflow.html', title='Butterflow Pen')

@app.route("/home/menu/stationery/Classmate Notebook")
def ClassmateNotebook():
    return render_template('classmate book.html', title='Classmate Notebook')

@app.route("/home/menu/stationery/Commerce Calculator")
def CommerceCalculator():
    return render_template('commerce cal.html', title='Commerce Calculator')

@app.route("/home/menu/stationery/DMOS X1 Pencil")
def DMOSXPencil():
    return render_template('DMOS pencil.html', title='DMOS X1 Pencil')

@app.route("/home/menu/stationery/Finegrip Pen")
def FinegripPen():
    return render_template('finegrip.html', title='Finegrip Pen')

@app.route("/home/menu/stationery/Folder Files")
def FolderFiles():
    return render_template('folder file.html', title='Folder Files')

@app.route("/home/menu/stationery/Camlin Geometry Box")
def CamlinGeometryBox():
    return render_template('geometry_box.html', title='Camlin Geometry Box')

@app.route("/home/menu/stationery/HB Pencil")
def HBPencil():
    return render_template('HB pencil.html', title='HB Pencil')

@app.route("/home/menu/stationery/Mini Drafter")
def MiniDrafter():
    return render_template('mini drafter.html', title='Mini Drafter')

@app.route("/home/menu/stationery/Nataraj Pencil")
def NatarajPencil():
    return render_template('nataraj.html', title='Nataraj Pencil')

@app.route("/home/menu/stationery/Classmate Project Paper")
def ClassmateProjectPaper():
    return render_template('one side ruled pages.html', title='Classmate Project Paper')

@app.route("/home/menu/stationery/Paper Files")
def PaperFiles():
    return render_template('paper files.html', title='Paper Files')

@app.route("/home/menu/stationery/Plastic File")
def PlasticFile():
    return render_template('plastic file.html', title='Plastic File')

@app.route("/home/menu/stationery/Pocket Calculator")
def PocketCalculator():
    return render_template('Pocket cal.html', title='Pocket Calculator')

@app.route("/home/menu/stationery/Roller Scale")
def RollerScale():
    return render_template('roller scale.html', title='Roller Scale')

@app.route("/home/menu/stationery/Scientific Calculator")
def ScientificCalculator():
    return render_template('Scientific Cal.html', title='Scientific Calculator')

@app.route("/home/menu/stationery/Reynolds Trimax")
def ReynoldsTrimax():
    return render_template('trimax.html', title='Reynolds Trimax')

@app.route("/home/menu/stationery/Use And Throw Pen")
def UseThrowPen():
    return render_template('use  and throw pen.html', title='Use And Throw Pen')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account is created! You are now able to Log In.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            next_page=request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else: 
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

def save_picture(form_picture):
    random_hex=secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path,'static/profile_pics',picture_fn)

    output_size = (125,125)
    i=Image.open(form_picture)
    i.thumbnail(output_size)

    i.save(picture_path)

    return picture_fn

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file=save_picture(form.picture.data)
            current_user.image_file=picture_file
        current_user.username=form.username.data
        current_user.email=form.email.data
        db.session.commit()
        flash('Your Account has been Updated!','success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data=current_user.username
        form.email.data=current_user.email

    image_file=url_for('static',filename='profile_pics/'+current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file,form=form)

def send_reset_email(user):
    token=user.get_reset_token()
    msg=Message('Password Reset Request',
                sender='smtp.googlemail.com',
                recipients=[user.email])
    msg.body='''To reset your password, visit the following link:
    {url_for('reset_token',token=token,_external=True)}
    If you did not make this request then simply ignore this email and no changes will be made.
    '''
    mail.send(msg)



@app.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password.','info')
        return redirect(url_for('login'))
    return render_template('reset_request.html',title= 'Reset Password',form=form)

@app.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token','warning')
        return redirect(url_for('reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password=hashed_password
        db.session.commit()
        flash('Your password has been updated! You are now able to Log In.', 'success')
        return redirect(url_for('login')) 
    return render_template('reset_token.html',title= 'Reset Password',form=form)

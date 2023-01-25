from flask import Flask, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from covid import Covid
from chatbot.main import get_response
from loguru import logger



#-----------------------------------------------------------------------
app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.sql"
db = SQLAlchemy(app)
#-----------------------------------------------------------------------
class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    email  = db.Column(db.String(50))
    name = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    initial =  db.Column(db.String(50))
    password  = db.Column(db.String(50))
    userType = db.Column(db.String(50), default='client')

class Institutions(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name  = db.Column(db.String(50))
    province  = db.Column(db.String(50))
    city  = db.Column(db.String(50))
    capacity = db.Column(db.Integer)
    contact =  db.Column(db.String(50))
    address = db.Column(db.String(150))
#-----------------------------------------------------------------------
def process(data):
    total = 0
    out =[]
    print(list(data.keys()))
    for key in list(data.keys()):
        try:
            total = total + int(data.get(key))
        except Exception as e:
            print(e)
            pass
    if total <= 16:
        out =[1,'This is the time between getting infected and when symptoms appear. In general, you may see symptoms start two to 14 days after infection. The incubation period varies among individuals, and it varies depending on the variant. Even though you do not have symptoms in the incubation period, you can transmit the coronavirus to another person during this stage']
    elif total>16 and total < 21:
        out = [2,'if you suspect you were exposed to someone with COVID-19, you should self-quarantine, watch for symptoms and consider getting tested four or five days following the exposure. This way, you can help prevent the spread of COVID-19. Please review Centers for Disease Control and Prevention (CDC) guidelines for isolation and quarantine.']
    elif total>21 and total < 28:
        out = [3,'Once symptoms appear, you have entered the acute stage. You may have fever, cough and other COVID-19 symptoms. Active illness can last one to two weeks if you have mild or moderate coronavirus disease, but severe cases can last months. Some people are asymptomatic, meaning they never have symptoms but do have COVID-19']
    elif total>30:
        out = [4,'Post-COVID-19 symptoms, such as lingering cough, on and off fever, weakness, and changes to your senses of smell or taste, can persist for weeks or even months after you recover from acute illness. Persistent symptoms are sometimes known as long COVID-19']
    print('total: ',total)
    return out
#-----------------------------------------------------------------------
def auth(email, password):
    user =Users.query.filter_by(email=email, password=password).first()
    if user != None:
        return user
    return None
#-----------------------------------------------------------------------
@app.route('/', methods = ['POST','GET'])
def index():
    session['msg']= None
    if request.method == 'POST':
        data = request.form.to_dict()
        user = auth(data.get('email'),data.get('password'))
        if user != None:
            session['user'] = {'id':user.id,'name':user.surname,'initial':user.initial, 'type':user.userType}
            return home()
        else:
            session['msg'] = 'af'
    template = 'login.html'
    return render_template(template, msg=session['msg'])
#-----------------------------------------------------------------------
@app.route('/sign_up', methods = ['POST','GET'])
def sign_up():
    if request.method == 'POST':
        data = request.form.to_dict()
        logger.debug(data)
        user = Users(email = data.get('email'),password = data.get('password'),name = data.get('name'),surname = data.get('surname'),initial = data.get('initial'))
        try:
            db.session.add(user)
            db.session.commit()
            session['msg'] = 'as'
            return index()
        except  Exception as e:
            logger.error(str(e))
            session['msg'] = 'af'
            
            
    template = 'register.html'
    return render_template(template)
#-----------------------------------------------------------------------
@app.route("/home/")
def home():
    covid = Covid(source="worldometers")
    data = covid.get_status_by_country_name("zimbabwe")
    zim_cases  = {'total_cases':data.get('total_cases'),'recovered':data.get('recovered'),'active':data.get('active_cases'),'deaths':data.get('deaths')}
    hosp = Institutions.query.all()

    template = 'index.html'
    return render_template(template,user=session['user'], data1= zim_cases,data=hosp)
#-----------------------------------------------------------------------
@app.route("/test", methods = ['POST','GET'])
def test():
    if request.method =='POST':
        data = request.form.to_dict()
        output = process(data)
        template = 'result.html'
        return render_template(template,user=session['user'], data=output)
    template = 'profile.html'
    return render_template(template,user=session['user'])
#-----------------------------------------------------------------------
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    print(userText)
    return str(get_response(userText))
#-----------------------------------------------------------------------

@app.route("/add", methods = ['POST','GET'])
def add():
    if request.method =='POST':
        data = request.form.to_dict()
        hospital = Institutions(name=data.get('name'),province=data.get('province'), contact = data.get('contact'), city = data.get('city'), capacity= data.get('capacity'), address= data.get('address'))
        db.session.add(hospital)
        db.session.commit()
        return health()
    template = 'add.html'
    return render_template(template,user=session['user'])
#-----------------------------------------------------------------------
@app.route("/statistics")
def statistics():
    hosp = Institutions.query.all()
    #covid = Covid(source="worldometers")
    #zim_cases = covid.get_status_by_country_name("zimbabwe")
    template = 'dashboard.html'
    data5=[0, 20, 5, 25, 10, 30, 15, 40, 4000]
    zim_cases  = {'total_cases':234,'recovered':678,'active':732,'deaths':789}
    return render_template(template,user=session['user'], data =hosp[:10], data1 = zim_cases, data5=data5)
#-----------------------------------------------------------------------
@app.route("/chatbot")
def chatbot():
    template = 'chatbot.html'
    return render_template(template,user=session['user'])
#-----------------------------------------------------------------------
@app.route("/health")
def health():
    template = 'health.html'
    hosp = Institutions.query.all()
    return render_template(template,user=session['user'],data=hosp)
#-----------------------------------------------------------------------
@app.route("/log_out")
def log_out():
    session['msg'] = None
    return index()
#-----------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True, port=5000)
#-----------------------------------------------------------------------
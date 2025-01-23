from flask import Flask, url_for, request, session, g
from flask.templating import render_template
from werkzeug.utils import redirect
from database import get_database
from werkzeug.security import generate_password_hash, check_password_hash
import os
import sqlite3
from backend import *

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

@app.teardown_appcontext
def close_database(error):
    if hasattr(g, 'crudapplication_db'):
        g.crudapplication_db.close()

'''def get_current_user():
    user = None
    if 'user' in session:
        user = session['user']
        db = get_database()
        user_cur = db.execute('select * from users where name = ?', [user])
        user = user_cur.fetchone()
    return user'''

'''@app.route('/')
def index():
    #user = get_current_user()
    return render_template('home.html')'''
#starting

@app.route("/",methods=["POST","GET"])
def index():
	if request.method=="POST":
		x=request.form["Uname"]
		y=request.form['Pass']
		if x==y and x=="admin":
			# Admin login
			return render_template('adminsection.html')
		else:
			# Check if user exist
			data=viewmoderator()
			for lst in data:
				if str(lst[0])==str(x) and str(lst[2])==str(y):
					return render_template('moderator_section.html',mode=x)

			return render_template('index.html',status="error")
	return render_template('index.html',status='get')
	
@app.route('/add_moderator',methods=["POST","GET"])
def moderator():

	if request.method=="POST":
		idd=request.form['mod_id']
		name=request.form['Inputname']
		paswd=request.form['exampleInputPassword1']
		email=request.form['exampleInputEmail1']
		phone=request.form['num']
		print(type(phone),"****************************")
		if len(str(phone))!=10:
			return render_template('add_mod.html',msg="phone")
		try:
			addmoderator(idd,name,paswd,str(email),phone)
			return render_template('add_mod.html',msg="success")
		except Exception as e:
			print(e,"========================================")

			
			return render_template('add_mod.html',msg="error")

		
		print(viewmoderator())


	return render_template('add_mod.html',msg="GET")

@app.route('/add_regstude',methods=["POST","GET"])
def add_regstude():

	if request.method=="POST":
		idd=request.form['mod_id']
		name=request.form['Inputname']
		paswd=request.form['exampleInputPassword1']
		phone=request.form['num']
		print(type(phone),"****************************")
		if len(str(phone))!=10:
			return render_template('add_reg_student.html',msg="phone")
		try:
			addstudent(idd,name,paswd,phone)
			return render_template('add_reg_student.html',msg="success")
		except Exception as e:
			print(e,"========================================")

			
			return render_template('add_reg_student.html',msg="error")

		
		


	return render_template('add_reg_student.html',msg="GET")

@app.route('/moderator_section',methods=["POST","GET"])
def modesection():
	nam="Moderator"
	if request.method=="POST":
		nam=str(request.form['Uname'])
	return render_template('moderator_section.html',mode=nam)

@app.route('/viewmoddata',methods=["POST","GET"])
def view_mod_data():
	# print("check1==================================",viewmoderator())
	if request.method=="POST":
		mod=request.form['mod_del']
		print(mod,"==============")
		deleterecmoderator(mod)	
	lst=viewmoderator()
	return render_template('view_mod.html',data=lst,lenght=len(lst))

@app.route('/view_regstud',methods=["POST","GET"])
def view_regstud():
        if request.method=="POST":
                        stu=request.form['mod_del']
                        print(stu,"==============")
                        deleterecstudent(stu)
        lst=view_student()
        return render_template('view_reg_stud.html',data=lst,lenght=len(lst))	
#miu emp
@app.route('/dashboard' ,methods=["POST","GET"])
def dashboard():
    #user = get_current_user()
    db = get_database()
    emp_cur = db.execute('select * from emp')
    allemp = emp_cur.fetchall()
    #return redirect(url_for('dashboard'),  allemp = allemp)
    return render_template('dashboard.html',  allemp = allemp)

#masii empe
@app.route('/dashboard_m' ,methods=["POST","GET"])
def dashboard_m():
    #user = get_current_user()
    db = get_database()
    emp_cur = db.execute('select * from empe')
    allemp = emp_cur.fetchall()
    #return redirect(url_for('dashboard'),  allemp = allemp)
    return render_template('dashboard_m.html',  allemp = allemp)
@app.route('/dashboard_ma' ,methods=["POST","GET"])
def dashboard_ma():
    #user = get_current_user()
    db = get_database()
    emp_cur = db.execute('select * from emp_m')
    allemp = emp_cur.fetchall()
    #return redirect(url_for('dashboard'),  allemp = allemp)
    return render_template('dashboard_ma.html',  allemp = allemp)

@app.route('/dashboard_k' ,methods=["POST","GET"])
def dashboard_k():
    #user = get_current_user()
    db = get_database()
    emp_cur = db.execute('select * from emp_k')
    allemp = emp_cur.fetchall()
    #return redirect(url_for('dashboard'),  allemp = allemp)
    return render_template('dashboard_k.html',  allemp = allemp)
@app.route('/dashboard_kis' ,methods=["POST","GET"])
def dashboard_kis():
    #user = get_current_user()
    db = get_database()
    emp_cur = db.execute('select * from empe_k')
    allemp = emp_cur.fetchall()
    #return redirect(url_for('dashboard'),  allemp = allemp)
    return render_template('dashboard_kis.html',  allemp = allemp)

@app.route('/dashboard_mk' ,methods=["POST","GET"])
def dashboard_mk():
    #user = get_current_user()
    db = get_database()
    emp_cur = db.execute('select * from empe_mk')
    allemp = emp_cur.fetchall()
    #return redirect(url_for('dashboard'),  allemp = allemp)
    return render_template('dashboard_mk.html',  allemp = allemp)
@app.route('/dashboard_i' ,methods=["POST","GET"])
def dashboard_i():
    #user = get_current_user()
    db = get_database()
    emp_cur = db.execute('select * from emp_i')
    allemp = emp_cur.fetchall()
    #return redirect(url_for('dashboard'),  allemp = allemp)
    return render_template('dashboard_i.html',  allemp = allemp)
@app.route('/dashboard_o' ,methods=["POST","GET"])
def dashboard_o():
    #user = get_current_user()
    db = get_database()
    emp_cur = db.execute('select * from empe_o')
    allemp = emp_cur.fetchall()
    #return redirect(url_for('dashboard'),  allemp = allemp)
    return render_template('dashboard_o.html',  allemp = allemp)
@app.route('/dashboard_ga' ,methods=["POST","GET"])
def dashboard_ga():
    #user = get_current_user()
    db = get_database()
    emp_cur = db.execute('select * from emp_a')
    allemp = emp_cur.fetchall()
    #return redirect(url_for('dashboard'),  allemp = allemp)
    return render_template('dashboard_ga.html',  allemp = allemp)

@app.route('/dashboard_e' ,methods=["POST","GET"])
def dashboard_e():
    #user = get_current_user()
    db = get_database()
    emp_cur = db.execute('select * from emp_e')
    allemp = emp_cur.fetchall()
    #return redirect(url_for('dashboard'),  allemp = allemp)
    return render_template('dashboard_e.html',  allemp = allemp)
@app.route('/dashboard_mi' ,methods=["POST","GET"])
def dashboard_mi():
    #user = get_current_user()
    db = get_database()
    emp_cur = db.execute('select * from empe_n')
    allemp = emp_cur.fetchall()
    #return redirect(url_for('dashboard'),  allemp = allemp)
    return render_template('dashboard_mi.html',  allemp = allemp)
@app.route('/dashboard_d' ,methods=["POST","GET"])
def dashboard_d():
    #user = get_current_user()
    db = get_database()
    emp_cur = db.execute('select * from emp_d')
    allemp = emp_cur.fetchall()
    #return redirect(url_for('dashboard'),  allemp = allemp)
    return render_template('dashboard_d.html',  allemp = allemp)
@app.route('/dashboard_kw' ,methods=["POST","GET"])
def dashboard_kw():
    #user = get_current_user()
    db = get_database()
    emp_cur = db.execute('select * from empe_m')
    allemp = emp_cur.fetchall()
    #return redirect(url_for('dashboard'),  allemp = allemp)
    return render_template('dashboard_kw.html',  allemp = allemp)
@app.route('/dashboard_ng' ,methods=["POST","GET"])
def dashboard_ng():
    #user = get_current_user()
    db = get_database()
    emp_cur = db.execute('select * from emp_g')
    allemp = emp_cur.fetchall()
    #return redirect(url_for('dashboard'),  allemp = allemp)
    return render_template('dashboard_ng.html',  allemp = allemp)
@app.route('/dashboard_ky' ,methods=["POST","GET"])
def dashboard_ky():
    #user = get_current_user()
    db = get_database()
    emp_cur = db.execute('select * from emp_y')
    allemp = emp_cur.fetchall()
    #return redirect(url_for('dashboard'),  allemp = allemp)
    return render_template('dashboard_ky.html',  allemp = allemp)
@app.route('/dashboard_kin' ,methods=["POST","GET"])
def dashboard_kin():
    #user = get_current_user()
    db = get_database()
    emp_cur = db.execute('select * from emp_n')
    allemp = emp_cur.fetchall()
    #return redirect(url_for('dashboard'),  allemp = allemp)
    return render_template('dashboard_kin.html',  allemp = allemp)

@app.route('/dashboard_kag' ,methods=["POST","GET"])
def dashboard_kag():
    #user = get_current_user()
    db = get_database()
    emp_cur = db.execute('select * from emp_o')
    allemp = emp_cur.fetchall()
    #return redirect(url_for('dashboard'),  allemp = allemp)
    return render_template('dashboard_kag.html',  allemp = allemp)

@app.route('/addnewemployee', methods = ["POST", "GET"])
def addnewemployee():
    #user = get_current_user()
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        total_projects = request.form['total_projects']
        joining_date = request.form['joining_date']
        total_test_case = request.form['total_test_case']
        if address =='miu' and len(str(phone))==10:
            db = get_database()
            db.execute('insert into emp (name, email, phone ,address,total_projects,joining_date,total_test_case) values (?,?,?,?,?,?,?)', [name, email, phone, address,total_projects,joining_date,total_test_case])
            db.commit()
            return redirect(url_for('dashboard',message="student successfully Added"))
        if address =='masii' and len(str(phone))==10:
            db = get_database()
            db.execute('insert into empe (name, email, phone ,address,total_projects,joining_date,total_test_case) values (?,?,?,?,?,?,?)', [name, email, phone, address,total_projects,joining_date,total_test_case])
            db.commit()
            return redirect(url_for('dashboard_m'))
        if address =='makutano' and len(str(phone))==10:
            db = get_database()
            db.execute('insert into emp_m (name, email, phone ,address,total_projects,joining_date,total_test_case) values (?,?,?,?,?,?,?)', [name, email, phone, address,total_projects,joining_date,total_test_case])
            db.commit()
            return redirect(url_for('dashboard_ma'))
        if address =='kithimani' and len(str(phone))==10:
            db = get_database()
            db.execute('insert into emp_k (name, email, phone ,address,total_projects,joining_date,total_test_case) values (?,?,?,?,?,?,?)', [name, email, phone, address,total_projects,joining_date,total_test_case])
            db.commit()
            return redirect(url_for('dashboard_k'))
        if address =='kisiiki' and len(str(phone))==10:
            db = get_database()
            db.execute('insert into empe_k (name, email, phone ,address,total_projects,joining_date,total_test_case) values (?,?,?,?,?,?,?)', [name, email, phone, address,total_projects,joining_date,total_test_case])
            db.commit()
            return redirect(url_for('dashboard_kis'))
        if address =='kikesa' and len(str(phone))==10:
            db = get_database()
            db.execute('insert into empe_mk (name, email, phone ,address,total_projects,joining_date,total_test_case) values (?,?,?,?,?,?,?)', [name, email, phone, address,total_projects,joining_date,total_test_case])
            db.commit()
            return redirect(url_for('dashboard_mk'))
        if address =='ikombe' and len(str(phone))==10:
            db = get_database()
            db.execute('insert into emp_i (name, email, phone ,address,total_projects,joining_date,total_test_case) values (?,?,?,?,?,?,?)', [name, email, phone, address,total_projects,joining_date,total_test_case])
            db.commit()
            return redirect(url_for('dashboard_i'))
        if address =='kithyoko' and len(str(phone))==10:
            db = get_database()
            db.execute('insert into empe_o (name, email, phone ,address,total_projects,joining_date,total_test_case) values (?,?,?,?,?,?,?)', [name, email, phone, address,total_projects,joining_date,total_test_case])
            db.commit()
            return redirect(url_for('dashboard_o'))
        if address =='masinga' and len(str(phone))==10:
            db = get_database()
            db.execute('insert into emp_a (name, email, phone ,address,total_projects,joining_date,total_test_case) values (?,?,?,?,?,?,?)', [name, email, phone, address,total_projects,joining_date,total_test_case])
            db.commit()
            return redirect(url_for('dashboard_ga'))
        if address =='ekalakala' and len(str(phone))==10:
            db = get_database()
            db.execute('insert into emp_e (name, email, phone ,address,total_projects,joining_date,total_test_case) values (?,?,?,?,?,?,?)', [name, email, phone, address,total_projects,joining_date,total_test_case])
            db.commit()
            return redirect(url_for('dashboard_e'))
        if address =='milaani' and len(str(phone))==10:
            db = get_database()
            db.execute('insert into empe_n (name, email, phone ,address,total_projects,joining_date,total_test_case) values (?,?,?,?,?,?,?)', [name, email, phone, address,total_projects,joining_date,total_test_case])
            db.commit()
            return redirect(url_for('dashboard_m'))
        if address =='ndithini' and len(str(phone))==10:
            db = get_database()
            db.execute('insert into emp_d (name, email, phone ,address,total_projects,joining_date,total_test_case) values (?,?,?,?,?,?,?)', [name, email, phone, address,total_projects,joining_date,total_test_case])
            db.commit()
            return redirect(url_for('dashboard_d'))
        if address =='kwamwaura' and len(str(phone))==10:
            db = get_database()
            db.execute('insert into empe_m (name, email, phone ,address,total_projects,joining_date,total_test_case) values (?,?,?,?,?,?,?)', [name, email, phone, address,total_projects,joining_date,total_test_case])
            db.commit()
            return redirect(url_for('dashboard_kw'))
        if address =='nguluni' and len(str(phone))==10:
            db = get_database()
            db.execute('insert into emp_g (name, email, phone ,address,total_projects,joining_date,total_test_case) values (?,?,?,?,?,?,?)', [name, email, phone, address,total_projects,joining_date,total_test_case])
            db.commit()
            return redirect(url_for('dashboard_ng'))
        if address =='kyeleni' and len(str(phone))==10:
            db = get_database()
            db.execute('insert into emp_y (name, email, phone ,address,total_projects,joining_date,total_test_case) values (?,?,?,?,?,?,?)', [name, email, phone, address,total_projects,joining_date,total_test_case])
            db.commit()
            return redirect(url_for('dashboard_ky'))
        if address =='kinyui' and len(str(phone))==10:
            db = get_database()
            db.execute('insert into emp_n (name, email, phone ,address,total_projects,joining_date,total_test_case) values (?,?,?,?,?,?,?)', [name, email, phone, address,total_projects,joining_date,total_test_case])
            db.commit()
            return redirect(url_for('dashboard_kin'))
        if address =='kangundo' and len(str(phone))==10:
            db = get_database()
            db.execute('insert into emp_o (name, email, phone ,address,total_projects,joining_date,total_test_case) values (?,?,?,?,?,?,?)', [name, email, phone, address,total_projects,joining_date,total_test_case])
            db.commit()
            return redirect(url_for('dashboard_kag'))
        else:
            return render_template('addnewemployee.html',msg ="Address or the phone numbers is wrong")
            
        
                
        
    return render_template('addnewemployee.html')
#Miu
@app.route('/fetchone/<int:empid>')
def fetchone(empid):        
    db = get_database()
    emp_cur = db.execute('select * from emp where empid = ?', [empid])
    single_emp= emp_cur.fetchone()
    return render_template('updateemployee.html',single_emp = single_emp)

#Masii
@app.route('/fetch/<int:empid>')
def fetch(empid):       
    db = get_database()
    emp_cur = db.execute('select * from empe where empid = ?', [empid])
    single_emp= emp_cur.fetchone()
    return render_template('updateemployee_m.html',single_emp = single_emp)
@app.route('/fetch_ma/<int:empid>')
def fetch_ma(empid):       
    db = get_database()
    emp_cur = db.execute('select * from emp_m where empid = ?', [empid])
    single_emp= emp_cur.fetchone()
    return render_template('updateemployee_ma.html',single_emp = single_emp)
@app.route('/fetch_k/<int:empid>')
def fetch_k(empid):       
    db = get_database()
    emp_cur = db.execute('select * from emp_k where empid = ?', [empid])
    single_emp= emp_cur.fetchone()
    return render_template('updateemployee_k.html',single_emp = single_emp)
@app.route('/fetch_kis/<int:empid>')
def fetch_kis(empid):       
    db = get_database()
    emp_cur = db.execute('select * from empe_k where empid = ?', [empid])
    single_emp= emp_cur.fetchone()
    return render_template('updateemployee_kis.html',single_emp = single_emp)
@app.route('/fetch_i/<int:empid>')
def fetch_i(empid):       
    db = get_database()
    emp_cur = db.execute('select * from emp_i where empid = ?', [empid])
    single_emp= emp_cur.fetchone()
    return render_template('updateemployee_i.html',single_emp = single_emp)
@app.route('/fetch_o/<int:empid>')
def fetch_o(empid):       
    db = get_database()
    emp_cur = db.execute('select * from empe_o where empid = ?', [empid])
    single_emp= emp_cur.fetchone()
    return render_template('updateemployee_o.html',single_emp = single_emp)
@app.route('/fetch_ga/<int:empid>')
def fetch_ga(empid):       
    db = get_database()
    emp_cur = db.execute('select * from emp_a where empid = ?', [empid])
    single_emp= emp_cur.fetchone()
    return render_template('updateemployee_ga.html',single_emp = single_emp)
@app.route('/fetch_e/<int:empid>')
def fetch_e(empid):       
    db = get_database()
    emp_cur = db.execute('select * from emp_e where empid = ?', [empid])
    single_emp= emp_cur.fetchone()
    return render_template('updateemployee_e.html',single_emp = single_emp)
@app.route('/fetch_mi/<int:empid>')
def fetch_mi(empid):       
    db = get_database()
    emp_cur = db.execute('select * from empe_n where empid = ?', [empid])
    single_emp= emp_cur.fetchone()
    return render_template('updateemployee_mi.html',single_emp = single_emp)
@app.route('/fetch_d/<int:empid>')
def fetch_d(empid):       
    db = get_database()
    emp_cur = db.execute('select * from emp_d where empid = ?', [empid])
    single_emp= emp_cur.fetchone()
    return render_template('updateemployee_d.html',single_emp = single_emp)
@app.route('/fetch_kw/<int:empid>')
def fetch_kw(empid):       
    db = get_database()
    emp_cur = db.execute('select * from empe_m where empid = ?', [empid])
    single_emp= emp_cur.fetchone()
    return render_template('updateemployee_kw.html',single_emp = single_emp)
@app.route('/fetch_ng/<int:empid>')
def fetch_ng(empid):       
    db = get_database()
    emp_cur = db.execute('select * from emp_g where empid = ?', [empid])
    single_emp= emp_cur.fetchone()
    return render_template('updateemployee_ng.html',single_emp = single_emp)
@app.route('/fetch_ky/<int:empid>')
def fetch_ky(empid):       
    db = get_database()
    emp_cur = db.execute('select * from emp_y where empid = ?', [empid])
    single_emp= emp_cur.fetchone()
    return render_template('updateemployee_ky.html',single_emp = single_emp)
@app.route('/fetch_kin/<int:empid>')
def fetch_kin(empid):       
    db = get_database()
    emp_cur = db.execute('select * from emp_n where empid = ?', [empid])
    single_emp= emp_cur.fetchone()
    return render_template('updateemployee_kin.html',single_emp = single_emp)
@app.route('/fetch_kag/<int:empid>')
def fetch_kag(empid):       
    db = get_database()
    emp_cur = db.execute('select * from emp_o where empid = ?', [empid])
    single_emp= emp_cur.fetchone()
    return render_template('updateemployee_kag.html',single_emp = single_emp)
@app.route('/fetch_kag/<int:empid>')
def fetch_kik(empid):       
    db = get_database()
    emp_cur = db.execute('select * from empe_mk where empid = ?', [empid])
    single_emp= emp_cur.fetchone()
    return render_template('updateemployee_mk.html',single_emp = single_emp)

@app.route('/updateemployee' , methods = ["POST", "GET"])
def updateemployee():
    #user = get_current_user()
    if request.method == 'POST':
        empid = request.form['empid']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        total_projects = request.form['total_projects']
        joining_date = request.form['joining_date']
        total_test_case = request.form['total_test_case']
        
        if address =='miu':
            db = get_database()
            db.execute('update emp set name = ?, email =? , phone = ? , address = ?,total_projects = ?,joining_date= ?,total_test_case = ? where empid = ?', [name, email, phone, address,total_projects,joining_date,total_test_case ,empid])
            db.commit()
            return redirect(url_for('dashboard'))
        if address =='masii':
            db = get_database()
            db.execute('update empe set name = ?, email =? , phone = ? , address = ?,total_projects = ?,joining_date= ?,total_test_case = ? where empid = ?', [name, email, phone, address,total_projects,joining_date,total_test_case ,empid])
            db.commit()
            return redirect(url_for('dashboard_m'))
        if address =='makutano':
            db = get_database()
            db.execute('update emp_m set name = ?, email =? , phone = ? , address = ?,total_projects = ?,joining_date= ?,total_test_case = ? where empid = ?', [name, email, phone, address,total_projects,joining_date,total_test_case ,empid])
            db.commit()
            return redirect(url_for('dashboard_ma'))
        if address =='kithimani':
            db = get_database()
            db.execute('update emp_k set name = ?, email =? , phone = ? , address = ?,total_projects = ?,joining_date= ?,total_test_case = ? where empid = ?', [name, email, phone, address,total_projects,joining_date,total_test_case ,empid])
            db.commit()
            return redirect(url_for('dashboard_k'))
        if address =='kisiiki':
            db = get_database()
            db.execute('update empe_k set name = ?, email =? , phone = ? , address = ?,total_projects = ?,joining_date= ?,total_test_case = ? where empid = ?', [name, email, phone, address,total_projects,joining_date,total_test_case ,empid])
            db.commit()
            return redirect(url_for('dashboard_kis'))
        if address =='kikesa':
            db = get_database()
            db.execute('update empe_mk set name = ?, email =? , phone = ? , address = ?,total_projects = ?,joining_date= ?,total_test_case = ? where empid = ?', [name, email, phone, address,total_projects,joining_date,total_test_case ,empid])
            db.commit()
            return redirect(url_for('dashboard_mk'))
        if address =='ikombe':
            db = get_database()
            db.execute('update emp_i set name = ?, email =? , phone = ? , address = ?,total_projects = ?,joining_date= ?,total_test_case = ? where empid = ?', [name, email, phone, address,total_projects,joining_date,total_test_case ,empid])
            db.commit()
            return redirect(url_for('dashboard_i'))
        if address =='kithyoko':
            db = get_database()
            db.execute('update empe_o set name = ?, email =? , phone = ? , address = ?,total_projects = ?,joining_date= ?,total_test_case = ? where empid = ?', [name, email, phone, address,total_projects,joining_date,total_test_case ,empid])
            db.commit()
            return redirect(url_for('dashboard_o'))
        if address =='masinga':
            db = get_database()
            db.execute('update emp_a set name = ?, email =? , phone = ? , address = ?,total_projects = ?,joining_date= ?,total_test_case = ? where empid = ?', [name, email, phone, address,total_projects,joining_date,total_test_case ,empid])
            db.commit()
            return redirect(url_for('dashboard_ga'))
        if address =='ekalakala':
            db = get_database()
            db.execute('update emp_e set name = ?, email =? , phone = ? , address = ?,total_projects = ?,joining_date= ?,total_test_case = ? where empid = ?', [name, email, phone, address,total_projects,joining_date,total_test_case ,empid])
            db.commit()
            return redirect(url_for('dashboard_e'))
        if address =='milaani':
            db = get_database()
            db.execute('update empe_n set name = ?, email =? , phone = ? , address = ?,total_projects = ?,joining_date= ?,total_test_case = ? where empid = ?', [name, email, phone, address,total_projects,joining_date,total_test_case ,empid])
            db.commit()
            return redirect(url_for('dashboard_mi'))
        if address =='ndithini':
            db = get_database()
            db.execute('update emp_d set name = ?, email =? , phone = ? , address = ?,total_projects = ?,joining_date= ?,total_test_case = ? where empid = ?', [name, email, phone, address,total_projects,joining_date,total_test_case ,empid])
            db.commit()
            return redirect(url_for('dashboard_d'))
        if address =='kwamwaura':
            db = get_database()
            db.execute('update empe_m set name = ?, email =? , phone = ? , address = ?,total_projects = ?,joining_date= ?,total_test_case = ? where empid = ?', [name, email, phone, address,total_projects,joining_date,total_test_case ,empid])
            db.commit()
            return redirect(url_for('dashboard_kw'))
        if address =='nguluni':
            db = get_database()
            db.execute('update emp_g set name = ?, email =? , phone = ? , address = ?,total_projects = ?,joining_date= ?,total_test_case = ? where empid = ?', [name, email, phone, address,total_projects,joining_date,total_test_case ,empid])
            db.commit()
            return redirect(url_for('dashboard_ng'))
        if address =='kyeleni':
            db = get_database()
            db.execute('update emp_y set name = ?, email =? , phone = ? , address = ?,total_projects = ?,joining_date= ?,total_test_case = ? where empid = ?', [name, email, phone, address,total_projects,joining_date,total_test_case ,empid])
            db.commit()
            return redirect(url_for('dashboard_ky'))
        if address =='kangundo':
            db = get_database()
            db.execute('update emp_o set name = ?, email =? , phone = ? , address = ?,total_projects = ?,joining_date= ?,total_test_case = ? where empid = ?', [name, email, phone, address,total_projects,joining_date,total_test_case ,empid])
            db.commit()
            return redirect(url_for('dashboard_kag'))
        if address =='kinyui':
            db = get_database()
            db.execute('update emp_n set name = ?, email =? , phone = ? , address = ?,total_projects = ?,joining_date= ?,total_test_case = ? where empid = ?', [name, email, phone, address,total_projects,joining_date,total_test_case ,empid])
            db.commit()
            return redirect(url_for('dashboard_kin'))
        
        
        
        return render_template('updateemployee_m.html')
#miu emp
@app.route('/deleteemp/<int:empid>', methods = ["GET", "POST"])
def deleteemp(empid):
    #user = get_current_user()
    db = get_database()
    db.execute('delete from emp where empid = ?', [empid])
    db.commit()
    return redirect(url_for('dashboard'))
#masii empe  
@app.route('/deleteempe/<int:empid>', methods = ["GET", "POST"])
def deleteempe(empid):
    #user = get_current_user()
    db = get_database()
    db.execute('delete from empe where empid = ?', [empid])
    db.commit()
    return redirect(url_for('dashboard_m'))
@app.route('/deleteemp_ma/<int:empid>', methods = ["GET", "POST"])
def deleteemp_ma(empid):
    #user = get_current_user()
    db = get_database()
    db.execute('delete from emp_m where empid = ?', [empid])
    db.commit()
    return redirect(url_for('dashboard_ma'))
@app.route('/deleteemp_k/<int:empid>', methods = ["GET", "POST"])
def deleteemp_k(empid):
    #user = get_current_user()
    db = get_database()
    db.execute('delete from emp_k where empid = ?', [empid])
    db.commit()
    return redirect(url_for('dashboard_k'))
@app.route('/deleteemp_kis/<int:empid>', methods = ["GET", "POST"])
def deleteemp_kis(empid):
    #user = get_current_user()
    db = get_database()
    db.execute('delete from empe_k where empid = ?', [empid])
    db.commit()
    return redirect(url_for('dashboard_kis'))
@app.route('/deleteemp_i/<int:empid>', methods = ["GET", "POST"])
def deleteemp_i(empid):
    #user = get_current_user()
    db = get_database()
    db.execute('delete from emp_i where empid = ?', [empid])
    db.commit()
    return redirect(url_for('dashboard_i'))
@app.route('/deleteemp_kik/<int:empid>', methods = ["GET", "POST"])
def deleteemp_kik(empid):
    #user = get_current_user()
    db = get_database()
    db.execute('delete from empe_mk where empid = ?', [empid])
    db.commit()
    return redirect(url_for('dashboard_i'))
@app.route('/deleteemp_o/<int:empid>', methods = ["GET", "POST"])
def deleteemp_o(empid):
    #user = get_current_user()
    db = get_database()
    db.execute('delete from empe_o where empid = ?', [empid])
    db.commit()
    return redirect(url_for('dashboard_o'))
@app.route('/deleteemp_ga/<int:empid>', methods = ["GET", "POST"])
def deleteemp_ga(empid):
    #user = get_current_user()
    db = get_database()
    db.execute('delete from emp_a where empid = ?', [empid])
    db.commit()
    return redirect(url_for('dashboard_ga'))
@app.route('/deleteemp_e/<int:empid>', methods = ["GET", "POST"])
def deleteemp_e(empid):
    #user = get_current_user()
    db = get_database()
    db.execute('delete from emp_e where empid = ?', [empid])
    db.commit()
    return redirect(url_for('dashboard_e'))
@app.route('/deleteemp_mi/<int:empid>', methods = ["GET", "POST"])
def deleteemp_mi(empid):
    #user = get_current_user()
    db = get_database()
    db.execute('delete from empe_n where empid = ?', [empid])
    db.commit()
    return redirect(url_for('dashboard_mi'))
@app.route('/deleteemp_d/<int:empid>', methods = ["GET", "POST"])
def deleteemp_d(empid):
    #user = get_current_user()
    db = get_database()
    db.execute('delete from emp_d where empid = ?', [empid])
    db.commit()
    return redirect(url_for('dashboard_d'))
@app.route('/deleteemp_kw/<int:empid>', methods = ["GET", "POST"])
def deleteemp_kw(empid):
    #user = get_current_user()
    db = get_database()
    db.execute('delete from empe_m where empid = ?', [empid])
    db.commit()
    return redirect(url_for('dashboard_kw'))
@app.route('/deleteemp_ng/<int:empid>', methods = ["GET", "POST"])
def deleteemp_ng(empid):
    #user = get_current_user()
    db = get_database()
    db.execute('delete from emp_g where empid = ?', [empid])
    db.commit()
    return redirect(url_for('dashboard_ng'))
@app.route('/deleteemp_ky/<int:empid>', methods = ["GET", "POST"])
def deleteemp_ky(empid):
    #user = get_current_user()
    db = get_database()
    db.execute('delete from emp_y where empid = ?', [empid])
    db.commit()
    return redirect(url_for('dashboard_ky'))
@app.route('/deleteemp_kin/<int:empid>', methods = ["GET", "POST"])
def deleteemp_kin(empid):
    #user = get_current_user()
    db = get_database()
    db.execute('delete from emp_n where empid = ?', [empid])
    db.commit()
    return redirect(url_for('dashboard_kin'))
@app.route('/deleteemp_kag/<int:empid>', methods = ["GET", "POST"])
def deleteemp_kag(empid):
    #user = get_current_user()
    db = get_database()
    db.execute('delete from emp_o where empid = ?', [empid])
    db.commit()
    return redirect(url_for('dashboard_kag'))













#correct the logout
@app.route('/logout')
def logout():
    #session.pop('user', None)
    render_template('moderator_section.html')

if __name__ == '__main__':
    app.run(debug = True)

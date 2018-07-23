from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request

app = Flask(__name__,instance_relative_config=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/answers.db'
db = SQLAlchemy(app)

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gender_1 = db.Column(db.String(10))
    gender_2 = db.Column(db.String(10))
    age = db.Column(db.String(10))
    exper_1 = db.Column(db.String(10))
    exper_2 = db.Column(db.String(10))
    year = db.Column(db.String(10))
    position_mt_m = db.Column(db.String(10))
    position_mt_t = db.Column(db.String(10))
    position_mb_b = db.Column(db.String(10))
    position_mb_m = db.Column(db.String(10))
    size_bl_b = db.Column(db.String(10))
    size_bl_l = db.Column(db.String(10))
    size_bf_b = db.Column(db.String(10))
    size_bf_f = db.Column(db.String(10))
    size_bs_b = db.Column(db.String(10))
    size_bs_s = db.Column(db.String(10))
    size_br_b = db.Column(db.String(10))
    size_br_r = db.Column(db.String(10))
    freq_page_1 = db.Column(db.String(10))
    freq_page_2 = db.Column(db.String(10))
    freq_1 = db.Column(db.String(10))
    freq_2 = db.Column(db.String(10))
    repeated_1 = db.Column(db.String(10))
    repeated_2 = db.Column(db.String(10))
    type_1 = db.Column(db.String(10))
    type_2 = db.Column(db.String(10))
    landing_1 = db.Column(db.String(10))
    landing_2 = db.Column(db.String(10))
    email = db.Column(db.String(100))

    def __init__(self,gender_1,gender_2,age,exper_1,exper_2,year,mt_m,mt_t,mb_b,mb_m,bl_b,bl_l,bf_b,bf_f,bs_b,bs_s,br_b,br_r,f_p_1,f_p_2,f_1,f_2,r_1,r_2,t_1,t_2,l_1,l_2,email):
        self.gender_1 = gender_1
        self.gender_2 = gender_2
        self.age = age
        self.exper_1 = exper_1
        self.exper_2 = exper_2
        self.year = year
        self.position_mt_m = mt_m
        self.position_mt_t = mt_t
        self.position_mb_b = mb_b
        self.position_mb_m = mb_m
        self.size_bl_b = bl_b
        self.size_bl_l = bl_l
        self.size_bf_b = bf_b
        self.size_bf_f = bf_f
        self.size_bs_b = bs_b
        self.size_bs_s = bs_s
        self.size_br_b = br_b
        self.size_br_r = br_r
        self.freq_page_1 = f_p_1
        self.freq_page_2 = f_p_2
        self.freq_1 = f_1
        self.freq_2 = f_2
        self.repeated_1 = r_1
        self.repeated_2 = r_2
        self.type_1 = t_1
        self.type_2 = t_2
        self.landing_1 = l_1
        self.landing_2 = l_2
        self.email = email

    def __repr__(self):
        return '<result %r>' % self.email


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/demographic')
def demographic():
    return render_template('demographic.html')


@app.route('/page2')
def page2():
    return render_template('page2.html')


@app.route('/page3')
def page3():
    return render_template('page3.html')


@app.route('/page4')
def page4():
    return render_template('page4.html')


@app.route('/page5')
def page5():
    return render_template('page5.html')


@app.route('/page6')
def page6():
    return render_template('page6.html')


@app.route('/page7')
def page7():
    return render_template('page7.html')


@app.route('/page8')
def page8():
    return render_template('page8.html')


@app.route('/page9')
def page9():
    return render_template('page9.html')


@app.route('/page10')
def page10():
    return render_template('page10.html')


@app.route('/page11')
def page11():
    return render_template('page11.html')


@app.route('/page12')
def page12():
    return render_template('page12.html')


@app.route('/thank')
def thank():
    return render_template('thank.html')


@app.route('/thank', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        data = request.get_data()
        data = str(data, encoding="utf-8")
        print (data)
        print (type(data))
        print (data[0])
        print (data[1])
        print (data[28])
        reslist = data.split('"')
        print(reslist)
        print(len(reslist))
        res = []
        for i in range(len(reslist)):
            tmp = i
            if ((tmp+1)%4 == 0):
                res.append(reslist[tmp])
        print (res)
        print (len(res))
        inputt = Result(res[0],res[1],res[2],res[3],res[4],res[5],res[6],res[7],res[8],res[9],res[10],res[11],res[12],res[13],
                        res[14],res[15],res[16],res[17],res[18],res[19],res[20],res[21],res[22],res[23],res[24],res[25],res[26],res[27],res[28])
        #db.session.add(inputt)
        #db.session.commit()
        print("finish!")
    return render_template('thank.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

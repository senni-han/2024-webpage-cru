from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


@app.route('/')
def firstpage():
    return render_template('index.html')

@app.route('/test',methods=['GET'])
def test():
    global A
    global B
    global C
    A =request.args.get('name')
    B =request.args.get('studentnumber')
    C =request.args.get('psw')
    return render_template('test.html',a=A,b=B,c=C)

@app.route('/result',methods=["GET"])
def result():

    global A
    global B
    global C
    A =request.args.get('name')
    B =request.args.get('studentnumber')
    C =request.args.get('psw')
    n1 = request.args.get("q1")
    if n1 == "1":
        s1 = 1 
    else:
        s1 = 0
    n2 = request.args.get("q2")
    if n2 == "3":
        s2 = 1 
    else:
        s2 = 0
    n3 = request.args.get("q3")
    if n3 == "2":
        s3 = 1 
    else:
        s3 = 0
    n4 = request.args.get("q4")
    if n4 == "4":
        s4 = 1 
    else:
        s4 = 0
    n5 = request.args.get("q5")
    if n5 == "2":
        s5 = 1 
    else:
        s5 = 0
    n6 = request.args.get("q6")
    if n6 == "2":
        s6 = 1 
    else:
        s6 = 0
    n7 = request.args.get("q7")
    if n7 == "1":
        s7 = 1 
    else:
        s7 = 0
    n8 = request.args.get("q8")
    if n8 == "2":
        s8 = 1 
    else:
        s8 = 0
    n9 = request.args.get("q9")
    if n9 == "4":
        s9 = 1 
    else:
        s9 = 0
    n10 = request.args.get("q10")
    if n10 == "1":
        s10 = 1 
    else:
        s10 = 0
    n11 = request.args.get("q11")
    if n11 == "2":
        s11 = 1 
    else:
        s11 = 0
    n12 = request.args.get("q12")
    if n12 == "4":
        s12 = 1 
    else:
        s12 = 0
    n13 = request.args.get("q13")
    if n13 == "3":
        s13 = 1 
    else:
        s13 = 0
    n14 = request.args.get("q14")
    if n14 == "1":
        s14 = 1 
    else:
        s14 = 0
    n15 = request.args.get("q15")
    if n15 == "4":
        s15 = 1 
    else:
        s15 = 0
    n16 = request.args.get("q16")
    if n16 == "3":
        s16 = 1 
    else:
        s16 = 0
    n17 = request.args.get("q17")
    if n17 == "2":
        s17 = 1 
    else:
        s17 = 0
    n18 = request.args.get("q18")
    if n18 == "4":
        s18 = 1 
    else:
        s18 = 0
    n19 = request.args.get("q19")
    if n19 == "3":
        s19 = 1 
    else:
        s19 = 0
    n20 = request.args.get("q20")
    if n20 == "2":
        s20 = 1 
    else:
        s20 = 0

    scoretotal = s1+s2+s3+s4+s5+s6+s7+s8+s9+s10+s11+s12+s13+s14+s15+s16+s17+s18+s19+s20
    return render_template('result.html',a=A,b=B,scoretotal=scoretotal)

if __name__ == '__main__':
    app.run(debug=True)


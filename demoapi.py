from flask import Flask, jsonify, request

app=Flask("demoapi")


@app.route('/', methods=['GET'])

def home():
		#if request.method=="POST":
	args=request.form.getlist('numbers')
	even=[]
	odd=[]
	ce=0
	co=0
	for i in args:
		x=int(args[i])
		if args[i]%2==0:
			even[i]=x
			ce+=1
		else:
			odd[i]=x
			co+=1
	return jsonify({'name':'Shubham Verma', 'odd':odd, even:'even'})
#		else:
#			return "Hello World"
app.run(debug=True)

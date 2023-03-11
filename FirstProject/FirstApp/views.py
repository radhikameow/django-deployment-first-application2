from django.shortcuts import render
from django.http import HttpResponse;


# Create your views here.
def display(request):
    #ss ----> is html-data/code
    ss = '''
            <center>
                <h2 style="color:Blue;">
                    Hello User,Welcome to Django First-Project First-App
                </h2>
                <hr color="brown" size="3" width="150"/>
            </center>
         ''';
         
    return HttpResponse(ss);
    
    
def show(request):
    #ss ----> is html-data/code
    ss = '''
            <center>
                <h2 style="color:Blue;">
                    Hello User,Welcome to Django First-Project First-App
                </h2>
                <hr color="brown" size="3" width="150"/>
            </center>
         ''';
         
    return HttpResponse(ss);
    

import time;	
def senddatetime(request):
    print("dtime/ url is requested & senddatetime() is executed");
    ct = time.ctime()
    print("Client Request Date & time on server :: ",ct);
    ss='''<html>
		<head>
			<title>Date-time Webpage</title>
			<style>
				h1{
					color:Blue;
					width:90%;
				}
				h2{
					color:Green;
					width:80%;
				}
				h3{
					color:Red;
					width:70%;
				}
				h1,h2,h3{
					background-color:lightgreen;
					border:2px Solid Brown;
				}
			</style>
		</head>
		<body>
			<center>
				<h1>Welcome to DJango-User..!!!</h1>
				<hr color='brown' width='80%'/>
				<h2>Server-Date & Time :: </h2>
				<hr color='brown' width='70%'/>
				<h3>''',ct,'''</h3>
				<hr color='brown' width='60%'/>
			</center>
		</body>
	</html>
	''';
    return HttpResponse(ss);


def demo(request):   
	print("mulitple-Requests-URLs same respose");
	htmldata='''<center>
		<h1>Welcome Demo User!!!</h1>
		<hr />
		<h2>This is Same-Output for diff-mulitple-Requests-URLs</h2>
		<hr />
		<h3>Have a Great Day...</h3>
		</center>''';
	return HttpResponse(htmldata);

#default-url-request-view-func
def homepage(request):
    htmldata='''<center>
        <h1>Welcome to DEFAULT Home-Page!!!</h1>
        <hr />
        <h2>Your Request Page is Not-Found...</h2>
        <hr />
        <h3>Plz try other URL or Links!!!</h3>
    </center>''';
    return HttpResponse(htmldata);

#program (Welcome.html) ---> Use Notepad++ only
(HTml webpage to display Welcome msg using diff.headings)

from django.shortcuts import render
from django.http import HttpResponse;

<!--
	HTML Webpage to display "Welcome Message" with different headings
-->
# Create your views here.
def show(request):
    #ss ----> is html-data/code
    ss = '''
            <center>
                <h2 style="color:Blue;">
                    Hello User,Welcome to Django First-Project First-App
                </h2>
                <hr color="brown" size="3" width="80"/>
            </center>
        ''',
   
<html>
	<head>
    
		<title>***Welcome-page***</title>
		<style>
			h1{
				color:Blue;
			}
			h2{
				color:Green;
			}
			h3{
				color:Red;
			}
			h4{
				color:Orange;
			}
			h5{
				color:Pink;
			}
			h6{
				color:violet;
			}
			h1,h3,h5{
				background-color:yellow;
			}
			h2,h4,h6{
				background-color:lightgreen;
			}
		</style>
	</head>
	<body>
		<center>
			<h1>Welcome to DJANGO HTML webpage</h1>
			<hr color="brown" width="95%"/>
			<h2>Welcome to DJANGO HTML webpage</h2>
			<hr color="brown" width="85%"/>
			<h3>Welcome to DJANGO HTML webpage</h3>
			<hr color="brown" width="75%"/>
			<h4>Welcome to DJANGO HTML webpage</h4>
			<hr color="brown" width="65%"/>
			<h5>Welcome to DJANGO HTML webpage</h5>
			<hr color="brown" width="55%"/>
			<h6>Welcome to DJANGO HTML webpage</h6>
			<hr color="brown" width="45%"/>
		</center>
	</body>
</html>
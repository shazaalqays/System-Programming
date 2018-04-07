import os
import cgi
`   +66

from django.shortcuts import render
from django.http import HttpResponseRedirect



def sendForm():
    print('''
    <html>
		<head>
		  <link rel="stylesheet" href="LOGINCSS.css">
		</head>
		<body>
		    <form action="LOGIN.py" method="get">
		        <div class="form-style">
		            <div class="section">
		                <h1>USERNAME<br><input type="text" name="username" /></h1>
		                <h1>PASSWORD<br><input type="password" name="username" /></h1>
		                <input type="button" value="LOG IN"/>
		            </div>
		            <img src="ytulogo.png" alt="Mountain View">
		            <line></line>
		            <div class="section2">
		                <a1>"İstikbal göklerdedir."</a1><br>
		                <a2>-Mustafa Kemal ATATÜRK</a2>
		            </div>
		        </div>
		    </form>
		</body>
	</html>
    ''')

def sendPage(name):
    print('''
    <html>
      <body>
        <h1>Hello {0}</h1>
      </body>
    </html>
    '''.format(name))


def getData():
    formData = cgi.FieldStorage()
    username = formData.getvalue("username")
    password = formData.getvalue("password")
    return(username, password)


if __name__ == "__main__":
    try:
        #sendForm()
        username, password = getData()
        sendPage(username)
    except:
        cgi.print_exception()

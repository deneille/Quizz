#!/usr/bin/python

import csv,cgi,urllib

#Code reads in the resources.csv file of my room
path = 'resources.csv'
f1 = open(path, 'r')
lines = [line for line in f1]
data = lines[0].strip().split(',')   #stores the resources.csv file in a list called data
f1.close()
data_ints = [int(i) for i in data]  #converts the data list into a list of integers
occupied = data_ints[2]

f=cgi.FieldStorage()
inventory=f.getvalue('inventory') #gets value of the inventory
URL=f.getvalue('URL')             #gets value of URL
inventory_string=str(inventory)
#checks the occupied value from the .csv file
if occupied == 1:  #if occupied value is 1 then the room is occupied 
	#code generates occupied page
	print "Content-type: text/html\n\n"
	print "<html>"
	print "<head><title>The Quizz</title></head>"
	print "<body><center><h1>Oops...This Room is Occupied</h1><center>"
	print "<center><img src ='https://img0.etsystatic.com/101/0/10703756/il_fullxfull.849553920_69ch.jpg' width='350' height='175'></center>"
	f = cgi.FieldStorage()
	url_string = str(URL)		    #converts URL value to string
	url_string = url_string.split("cgi-bin/room.cgi",1)[0]+'room.html'    
	#creates form to redirect the user the room from which they came
	page = '''<center>				
	<form action ="%s" method="get">
	<input type="hidden" name="inventory" value="%s">
	<input type="hidden" name="command" value="REFRESH">
	<input type="submit" value="Go Back">
	</form>
	</center>'''%(url_string,inventory)
	print page
	print "</body></html>"
if occupied == 0:  #if occupied value is 0 then the player can be transported to the room
	if inventory_string.split(",",1)[0] == "1":  #checking to see if the inventory is 1,0 to end the game
		print "Content-type: text/html\n\n"
 		print "<html>"
		print "<head><title>The Quizz</title></head>"
		print "<body><center><h1>Game Over!</h1><center>"
		print "<center><img src='https://media.giphy.com/media/HqpCnDg0U5w6Q/giphy.gif' width='500' height='400'></center>"
	else:
		print "Content-type: text/html\n\n"
		form = cgi.FieldStorage()	
		inventory = form.getvalue('inventory')
		URL = form.getvalue('URL')
		string_url = str(URL)
		tr_url = string_url.split('room.cgi',1)[0]+'success.py'   #url for success.py script
		#code to generate the url of the room to be transported to
		page= '''
<html>

<head>    
<title>TheQuizz</title>
</head>   
 

<body bgcolor="gold">

<center> <h1> WELCOME TO THE QUIZZ ! </h1>  </center>


<u>You are only allowed to use the following commands </u> 
    
<ul>
<li> PLAY</li>
<li> EXIT  </li> 
<li> DROP </li>
<li> REFRESH  </li>
</ul>



<center> <img src = "quizz.jpeg" > </center>


<br>

<center> 
<form action="http://cs.mcgill.ca/~hgokse/cgi-bin/transporter.py" method="post" style=float:center; >
		<input type=hidden name=inventory value=1,0>
		<input type=hidden name=URL value=http://cs.mcgill.ca/~akouma1/cgi-bin/room.cgi>
		<input type=submit value=North>
</form>
</center>

<center>
 <form action="cgi-bin/room.cgi" method="post" align="center">
    <input align="center" style="width: 500px; height 200px ;" type="text" name="command" placeholder="Answer here">
    <input type=hidden name=inventory value=1,0>
    <input type=submit value= "Submit Answer" >
 </form>

</center>

<form action="http://www.cs.mcgill.ca/~akouma1/cgi-bin/transporter.py"  method="get" style=float:left; >
		<input type=hidden name=inventory value=1,0>
		<input type=hidden name=URL value=http://cs.mcgill.ca/~akouma1/cgi-bin/room.cgi>
		<input type=submit value=West>
</form>

<form action=http://cs.mcgill.ca/~yhe54/cgi-bin/transporter.py  method="get" style=float:right; >
		<input type=hidden name=inventory value=1,0>
		<input type=hidden name=URL value=http://cs.mcgill.ca/~akouma1/cgi-bin/room.cgi>
		<input type=submit value=East>
</form>

<br>

<center>
<form action=http://cs.mcgill.ca/~dguise/cgi-bin/transporter.py  method="get" style=float:center; >
		<input type=hidden name=inventory value=1,0>
		<input type=hidden name=URL value=http://cs.mcgill.ca/~akouma1/cgi-bin/room.cgi>
		<input type=submit value=South>
</form>
</center>

<br>

<center> 
<textarea bgcolor="gold" rows="5" cols="50" >
Output area
</textarea>
</center>

</body>

</html>

		'''
		print page
		manna = data_ints[0] + 1
		manna_str = str(manna)
		up_data = [[manna_str,data[1],'1']]  #updates the resources.csv file of the room that the user was transported to
		with open('resources.csv', 'w') as f2:
			f2.truncate()
			w = csv.writer(f2, delimiter=',')
			w.writerows(up_data)
		f2.close()
		response=urllib.urlopen('http://www.cs.mcgill.ca/~dguise/cgi-bin/success.py') #calls the success.py file of the room that player was previously by updating the .csv occupied status
		response.read()

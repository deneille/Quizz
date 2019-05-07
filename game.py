#!/usr/bin/env python
#!C:\Python25\Python.exe
# Import modules for CGI handling 

import cgi, cgitb
import csv, sys

def main():

        cgitb.enable() #for debugging  


        # Create instance of FieldStorage 
        form = cgi.FieldStorage()
        #set our variables to 0 ; Add input for inventory 
        userInput=0;
        userInventory=0;
        sucess=0;
        # print "Content-type:text/html\r\n\r\n"
        # print form
        # print "Hello"
        # print sys.argv

        # Get data from fields
        if form.getvalue('command'):
           userInput = form.getvalue('command')

        if form.getvalue('inventory'):
           userInventory = form.getvalue('inventory')

        if form.getvalue('sucess'):
           sucess = form.getvalue('sucess')
          # print "Content-type:text/html\r\n\r\n"
          # print form.getvalue('sucess')       



        #check if it is the command PLAY play here 
        if userInput== "PLAY":
        #if form.getvalue('URL'):
        #if len(sys.argv) == 3 :

                #print sys.argv

                #pInv = userInventory.split(",")
                pInv= sys.argv

                print "Content-type:text/html\r\n\r\n"
                page= ''' 
                <html>
                <head>    
                <title>TheQuizz</title>
                </head>   
                 

                <body bgcolor="gold">
                <center> <h1> NOW YOU HAVE STARTED THE QUIZZ! </h1></center>    
                <center> <img src = "../quizz.jpeg" > </center>
                <br>
                <center> <textarea bgcolor="gold" rows="5" cols="50"> You have now started the game. Who is the best soccer player in the word ? Hint : he plays for barcelona </textarea></center>

                <center> <form action:"../cgi-bin/game.py" method="post" align="center">
                    <input align="center" style="width: 500px; height 200px ;" type="text" name="command" placeholder="Answer here">
                    <input type=hidden name=inventory value={0},{1}>
                    <input type=hidden name=sucess value=0>
                    <input type=submit value= "Submit Answer" >
                 </form>
                </center>
                <br>


                </body></html>
                '''
                print page.format(pInv[0],pInv[1])





        # print form
        # print "\n \n User input : " + userInput + "--- \n"
        # print " Inventory : " + userInventory

        #read from csv file 
        with open('resources.csv', 'r') as f:
                        r = csv.reader(f, delimiter=',')
                        resources = list(r)





        if userInput=="MESSI":
                   #here open the resource.csv and read it ; I also added a hidden tag named sucess 

                pInv = userInventory.split(",") #get the inventory to print it back 

                print "Content-type:text/html\r\n\r\n"
                # print resources
                # print resources[0][1]

                pagePart1= ''' 
                        <html>
                        <head>    
                        <title>TheQuizz</title>
                        </head>   
                         

                        <body bgcolor="gold">
                        <center> <h1> CONGRATS</h1></center>    
                        <center> <img src = "../quizz.jpeg" > </center>
                        <br> <center> <h3> PLEASE CAREFULLY READ THE INSTRUCTIONS AND CONDITIONS BEFORE ANSWERING </h3> </center>
                        <center> <textarea bgcolor="gold" rows="10" cols="115">
                        You have won. Congrats.
                        Enter in the text box the resources you want. Pick resources according to our rules. 
                        You can take at most 5 units of something. 
                        For example for 3 manna and 2 gold enter it in the following format "3,2"
                        Not the following restriction : 
                        - if you enter more than 5 elements you will get 3 manna and 2 golds 
                        - if you request resources more than what the room has your inventory will "not" be updated 
                        - if you don't enter resources in the correct format, the page will encounter an error.
                          Press the back button to re-enter your answer
                        </textarea></center>
                        Here are the hidden available resources of our room : {0} Manna and {1} Gold 
                        <br>
                        Here is your inventory : {2} Manna and {3} Gold 
                        '''
                print pagePart1.format(resources[0][0], resources[0][1], pInv[0],pInv[1])

                page = '''

                        <center> <form action:"../cgi-bin/game.py" method="get" align="center">
                            <input align="center" style="width: 500px; height 200px ;" type="text" name="command" placeholder="Answer here">
                            <input type=hidden name=inventory value={0},{1}>
                            <input type=hidden name=sucess value=1>
                            <input type=submit value= "Submit Answer" >
                         </form>
                        </center>
                        <br>
                                                </body></html>
                        '''
                print page.format(pInv[0],pInv[1]) #We have added a hidden input announcing sucess



        #if the user doesn't get the right answer 


        if userInput!= "MESSI" and userInput!=0 and sucess=='0' and userInput!="QUIT":

                #here open the ressource.csv and read it ; I also added a hidden tag named sucess 
                pInv = userInventory.split(",") #get the inventory to print it back 

                print "Content-type:text/html\r\n\r\n"
                page=  ''' 
                        <html>
                        <head>    
                        <title>TheQuizz</title>
                        </head>   
                         

                        <body bgcolor="gold">
                        <center> <h1> Nooooo...... :( </h1></center>    
                        <center> <img src = "../quizz.jpeg" > </center>
                        <br>
                        <center> <textarea bgcolor="gold" rows="5" cols="50">SORRY you missed it !! Either you are wrong or you entered an incorrect input.Enter QUIT to return the the home Menu 
                        OR answer to the following question :
                        Who is the best soccer player in the word ? Hint : he plays in barcelona
                         </textarea></center>

                        <center> <form action:"game.py" method="get" align="center">
                            <input align="center" style="width: 500px; height 200px ;" type="text" name="command" placeholder="Answer here">
                            <input type=hidden name=inventory value={0},{1}>
                            <input type=hidden name=sucess value=0>
                            <input type=submit value= "Submit Answer" >
                         </form>
                        </center>
                        <br>
                        </body></html>
                        '''
                print page.format(pInv[0],pInv[1])


    #If the player WINS and chooses the ressources he wants 

        if sucess == '1' and userInput.split(",") :

                update = userInput.split(",")
        #if the user exceeds the input of 5 elements  
                if (int(update[0])+int(update[1]))>5 :
                        update[0]= 3
                        update[1]= 2
        #Now update the room ressources                 
                rManna1= resources[0][0]
                rGold1= resources[0][1]
        #Here we update the resources list      
                resources[0][0]= int(rManna1) - int(update[0])
                resources[0][1]= int(rGold1) - int(update[1])
        #Here we check if the room resources went negative we set limit to 0 
                mannaError=0; #we create variable to check if the room mana is gone below 0 same for gold 
                goldError=0;

                if resources[0][0]<0 : #if the manna goes bellow 0, we penalize the player by not updating his inventory or the room's resource
                        resources[0][0]= rManna1
                        mannaError=1
                if resources[0][1]<0 : #if
                        resources[0][1]= rGold1
                        goldError=1

        #Now update the ressource file with the new resources 
                with open("resources.csv", "wb") as f:
                         writer = csv.writer(f)
                         writer.writerows(resources)

        #now here we udpate the player inventory 
                pInv = userInventory.split(",")
                pManna1= pInv[0]
                pGold1= pInv[1]

                if mannaError==0 and goldError==0 : #if the ressource chosen by the player do not exceed the room's ressources 
                        pInv[0]= int(pManna1)+ int(update[0])
                        pInv[1]= int(pGold1)+ int(update[1])
                        #Else the player inventory won't be updated as a sanction to the player 

        #Here we check for sucess 
                if int(pInv[1]) >= 100:
                        print "Content-type:text/html\r\n\r\n"
                        print pInv
                        print userInventory
                        page= '''
                        <html> <head> <title> Winner !! </title> </head>
                        <body bgcolor="red">  
                        <center><h2> CONGRATS YOU HAVE MANAGED TO GET 100 GOLD YOU WON !!!! YOU ARE THE BESTT !!!! <h2> </center>
                        <center> <img src = "../winner.jpg" > </center>
                        <center> <h3> Here is your final inventory : Manna: {0} Gold : {1} </h3> </center>
                        GOOD BYE, please close the browser window 
                        </body></hmtl>
                        '''
                        #now update the ressource file o mark as not occupied : 
                        resources[0][2]= 0;
                        #overwrite the ressource file 
                        with open("../resources.csv", "wb") as f:
                         writer = csv.writer(f)
                         writer.writerows(resources)

                        print page.format(pInv[0],pInv[1])

                else :
                        print "Content-type:text/html\r\n\r\n"
                        #added april 5th 
                        # print update
                        # print resources
                        # print len(update)
                        # print "// "
                        # print userInventory
                        # print"//"
                        # print pInv

                        page = '''
                        <html>
                        <head>    
                        <title>TheQuizz</title>
                        </head>                  
                        <body bgcolor="gold">
                        <center> <h1> WELCOME BACK TO THE QUIZZ ! </h1>  </center>
                        <u>You are only allowed to use the following commands </u>                  
                        <ul>
                        <li> PLAY</li>
                        <li> EXIT  </li> 
                        <li> DROP </li>
                        <li> REFRESH  </li>
                        </ul>
                        <h3> Note that your ressources have been updated ONLY if you have entered a good entry previously </h3>
                        <center> <img src = "../quizz.jpeg" > </center>
                        <br>
                        <center> 
                        <form action="http://cs.mcgill.ca/~hgokse/cgi-bin/transporter.py" method="get" style=float:center; >
                                        <input type=hidden name=inventory value={0},{1}>
                                        <input type=hidden name=URL value=http://cs.mcgill.ca/~akouma1/cgi-bin/room.cgi>
                                        <input type=submit value=North>
                        </form>
                        </center>
                        <center>
                         <form action="room.cgi" method="post" align="center">
                            <input align="center" style="width: 500px; height 200px ;" type="text" name="command" placeholder="Answer here">
                            <input type=hidden name=inventory value={0},{1}>
                            <input type=submit value= "Submit Answer" >
                         </form>

                        </center>
                        <form action=http://www.cs.mcgill.ca/~akouma1/cgi-bin/transporter.py  method="get" style=float:left; >
                                        <input type=hidden name=inventory value={0},{1}>
                                        <input type=hidden name=URL value=http://cs.mcgill.ca/~akouma1/cgi-bin/room.cgi>
                                        <input type=submit value=West>
                        </form>
                        <form action=http://cs.mcgill.ca/~yhe54/cgi-bin/transporter.py  method="get" style=float:right; >
                                        <input type=hidden name=inventory value={0},{1}>
                                        <input type=hidden name=URL value=http://cs.mcgill.ca/~akouma1/cgi-bin/room.cgi>
                                        <input type=submit value=East>
                        </form>
                        <br>
                        <center>
                        <form action=http://cs.mcgill.ca/~idouzi/cgi-bin/transporter.py  method="get" style=float:center; >
                                        <input type=hidden name=inventory value={0},{1}>
                                        <input type=hidden name=URL value=http://cs.mcgill.ca/~akouma1/cgi-bin/room.cgi>
                                        <input type=submit value=South>
                        </form>
                        </center>
                        <br>
                        <center> 
                        <textarea bgcolor="gold" rows="5" cols="50" >
                        You have {0} Manna and {1} Gold </textarea>
                        </center></body></html>

                        '''
                        print page.format(pInv[0],pInv[1])


        #If the player presses QUIT
        if userInput=="QUIT":

                print "Content-type:text/html\r\n\r\n"
                #added april 5th 

                pInv = userInventory.split(",")

                page = '''
                <html>
                <head>    
                <title>TheQuizz</title>
                </head>                  
                <body bgcolor="gold">
                <center> <h1> WELCOME BACK TO THE QUIZZ ! </h1>  </center>
                <u>You are only allowed to use the following commands </u>                  
                <ul>
                <li> PLAY</li>
                <li> EXIT  </li> 
                <li> DROP </li>
                <li> REFRESH  </li>
                </ul>
                <center> <img src = "../quizz.jpeg" > </center>
                <br>
                <center> 
                <form action="http://cs.mcgill.ca/~hgokse/cgi-bin/transporter.py" method="get" style=float:center; >
                                <input type=hidden name=inventory value={0},{1}>
                                <input type=hidden name=URL value=http://cs.mcgill.ca/~akouma1/cgi-bin/room.cgi>
                                <input type=submit value=North>
                </form>
                </center>
                <center>
                 <form action="room.cgi" method="post" align="center">
                    <input align="center" style="width: 500px; height 200px ;" type="text" name="command" placeholder="Answer here">
                    <input type=hidden name=inventory value={0},{1}>
                    <input type=submit value= "Submit Answer" >
                 </form>

                </center>
                <form action=transporter.py  method="get" style=float:left; >
                                <input type=hidden name=inventory value={0},{1}>
                                <input type=hidden name=URL value=http://cs.mcgill.ca/~akouma1/cgi-bin/room.cgi>
                                <input type=submit value=West>
                </form>
                <form action=http://cs.mcgill.ca/~yhe54/cgi-bin/transporter.py  method="get" style=float:right; >
                                <input type=hidden name=inventory value={0},{1}>
                                <input type=hidden name=URL value=http://cs.mcgill.ca/~akouma1/cgi-bin/room.cgi>
                                <input type=submit value=East>
                </form>
                <br>
                <center>
                <form action=http://cs.mcgill.ca/~idouzi/cgi-bin/transporter.py  method="get" style=float:center; >
                                <input type=hidden name=inventory value={0},{1}>
                                <input type=hidden name=URL value=http://cs.mcgill.ca/~akouma1/cgi-bin/room.cgi>
                                <input type=submit value=South>
                </form>
                </center>
                <br>
                <center> 
                <textarea bgcolor="gold" rows="5" cols="50" >
                Output area </textarea>
                </center></body></html>

                '''
                print page.format(pInv[0],pInv[1])



main()



           
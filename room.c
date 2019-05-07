
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
void printg(int m, int g){
printf("%s%c%c\n","Content-Type:text/html;charset=iso-8859-1",13,10);
printf("<html><head><title>TheQuizz</title></head><body bgcolor='gold'><center><h1>WELCOME TO THE QUIZZ !</h1></center><u>You are only allowed to use the following commands</u><ul><li>PLAY</li><li>EXIT</li><li>DROP</li><li>REFRESH</li></ul><center><img src = '../quizz.jpeg' ></center><br><center><form action=http://cs.mcgill.ca/~hgokse/cgi-bin/transporter.py  method='get' style=float:center; ><input type=hidden name=inventory value=%d,%d><input type=hidden name=URL value=http://cs.mcgill.ca/~akouma1/cgi-bin/room.cgi><input type=submit value=North></form></center><center><form action='room.cgi' method='post' align='center'><input align='center' style='width: 500px; height 200px ;' type='text' name='command' placeholder='Answer here'><input type=hidden name=inventory value=%d,%d><input type=submit value= 'Submit Answer' ></form></center><form action=teleport.py  method='get' style=float:left; ><input type=hidden name=inventory value=%d,%d><input type=hidden name=URL value=http://cs.mcgill.ca/~akouma1/cgi-bin/room.cgi><input type=submit value=West></form><form action=http://cs.mcgill.ca/~yhe54/cgi-bin/transporter.py  method='get' style=float:right; ><input type=hidden name=inventory value=%d,%d><input type=hidden name=URL value=http://cs.mcgill.ca/~akouma1/cgi-bin/room.cgi><input type=submit value=East></form><br><center><form action=http://cs.mcgill.ca/~idouzi/cgi-bin/transporter.py  method='get' style=float:center; ><input type=hidden name=inventory value=%d,%d><input type=hidden name=URL value=http://cs.mcgill.ca/~akouma1/cgi-bin/room.cgi><input type=submit value=South></form></center><br><center><textarea bgcolor='gold' rows='5' cols='50' >Output area</textarea></center></body></html>",m,g,m,g,m,g,m,g,m,g);}
int main (int argv, char* argc){
//get the command and inventory using post
char string[200];
char c;
int i=0;
char cmd[200];
c=getchar();
//whatever is before the first = is not important so skip it
while (c!='='){
c=getchar();}
//get the next char from =
c=getchar();
//everything that is before & is a command so we keep it
char tmp[100];
int a=0;
char *ptr;
int n=0;
while (c!='&'){
//if it is + means that the following integer will be the number of coins the player wants to drop so keep it
if (c=='+'){
c=getchar();
while(c!='&'){
//create a temporary string with the number in order to use strtol to make it into an int 
tmp[a]=c;
a++;
c=getchar();
}
n= strtol(tmp,&ptr,0);
}
//else its a command so keep it again
else {
cmd[i]=c;
i++;
c=getchar();
}
}
//before the second = has been processed previously or its not important so skip
while (c!='='){
c=getchar();}
//skip the equals to point to the mana
c=getchar();
int mana;
int gold;
char *ptr1;
char tmp1[100];
int z=0;
//the number that is before the % is the mana we use same method as before to store it as an int
while (c!='%'){
tmp1[z]=c;
z++;
c=getchar();}
mana=strtol(tmp1,&ptr1,0);
//skip the %2C to point to the gold
c=getchar();
c=getchar();
c=getchar();
char *ptr2;
char tmp2[100];
int y=0;
//the numebr before the end of file is the gold so keep it using the same mehod
while (c!= EOF){
tmp2[y]=c;
y++;
c=getchar();}
gold=strtol(tmp2,&ptr2,0);
//if the command is drop then uptade the inventory acording the instructions
if(strncmp(cmd,"DROP",4)==0){
//if the player wants to drop more gold then they have reprint the page but give an error messege;
if ((gold-n)<0){
printf("%s%c%c\n","Content-Type:text/html;charset=iso-8859-1",13,10);
printf("<html><head><title>TheQuizz</title></head><body bgcolor='gold'><center><h1>WELCOME TO THE QUIZZ !</h1></center><u>You are only allowed to use the following commands</u><ul><li>PLAY</li><li>EXIT</li><li>DROP</li><li>REFRESH</li></ul><center><img src = '../quizz.jpeg' ></center><br><center><form action=http://cs.mcgill.ca/~hgokse/cgi-bin/transporter.py  method='get' style=float:center; ><input type=hidden name=inventory value=%d,%d><input type=hidden name=URL value=http://cs.mcgill.ca/~akouma1/cgi-bin/room.cgi><input type=submit value=North></form></center><center><form action='room.cgi' method='post' align='center'><input align='center' style='width: 500px; height 200px ;' type='text' name='command' placeholder='Answer here'><input type=hidden name=inventory value=%d,%d><input type=submit value= 'Submit Answer' ></form></center><form action=http://www.cs.mcgill.ca/~akouma1/cgi-bin/transporter.py  method='get' style=float:left; ><input type=hidden name=inventory value=%d,%d><input type=hidden name=URL value=http://cs.mcgill.ca/~akouma1/cgi-bin/room.cgi><input type=submit value=West></form><form action=http://cs.mcgill.ca/~yhe54/cgi-bin/transporter.py  method='get' style=float:right; ><input type=hidden name=inventory value=%d,%d><input type=hidden name=URL value=http://cs.mcgill.ca/~akouma1/cgi-bin/room.cgi><input type=submit value=East></form><br><center><form action=http://cs.mcgill.ca/~idouzi/cgi-bin/transporter.py  method='get' style=float:center; ><input type=hidden name=inventory value=%d,%d><input type=hidden name=URL value=http://cs.mcgill.ca/~akouma1/cgi-bin/room.cgi><input type=submit value=South></form></center><br><center><textarea bgcolor='gold' rows='5' cols='50' >You tried to drop more gold then what you had!! Enter less gold</textarea></center></body></html>",mana,gold,mana,gold,mana,gold,mana,gold,mana,gold);}
else{
//does the math
int tmp=n/2;
gold=gold-n;
mana=mana+tmp;
//open the resources for reading and writing
FILE *f;
f=fopen("resources.csv", "r+");
char ch = fgetc(f);
char tmp4[100];
char *ptr4;
int o=0;
//get the first characters representing mana and terun them into ints using the previous method
while(ch!=','){
tmp4[o]=ch;
o++;
ch= fgetc(f);
}
int hm=strtol(tmp4,&ptr4,0);
//skip the ,
ch=fgetc(f);
char tmp5[100];
char *ptr5;
int p=0;
//get the chars before , representing gold and turn them into ints
while(ch!=','){
tmp5[p]=ch;
p++;
ch= fgetc(f);
}
int hg=strtol(tmp5,&ptr5,0);
//skip the ,
ch=fgetc(f);
int oc;
//find out if the room is occupied
if(ch=='1'){
oc=1;}
else{
oc=0;}
//add the gold the player left to the hidden resources
hg = hg + n;
rewind(f);
//update the file
fprintf(f,"%d,%d,%d",hm,hg,oc);
//print the page again
printg(mana,gold);
}}
//go to the game page that calls game.py
else if(strncmp(cmd,"PLAY",4)==0){
printf("%s%c%c\n","Content-Type:text/html;charset=iso-8859-1",13,10);
printf("<html><head><title>TheQuizz Game</title></head><body bgcolor='gold'><center><h1> You have now started the GAME, Good Luck ! </h1></center><center><img src = '../quizz.jpeg' ></center><br> <center><textarea bgcolor='gold' rows='5' cols='50'> You have now started the game. Who is the best soccer player in the word ? Hint : he plays for barcelona </textarea></center><form action='game.py' method='post' align='center'><input align='center' style='width: 500px; height 200px ;' type='text' name='command' placeholder='Answer here'><input type=hidden name=inventory value=%d,%d><input type=hidden name=sucess value=0><input type=submit value= 'Submit Answer' ></form></center><br></body></html>",mana,gold);}
//redraw the screen with inventory
else if(strncmp(cmd,"REFRESH",7)==0){
printg(mana,gold);
}
else if(strncmp(cmd,"EXIT",4)==0){
//open resources to update it
FILE *f2;
f2=fopen("resources.csv", "r+");
char ch2 = fgetc(f2);
char tmp5[100];
char *ptr5;
int o2=0;
//get the mana of the room
while(ch2!=','){
tmp5[o2]=ch2;
o2++;
ch2= fgetc(f2);
}
int hm2=strtol(tmp5,&ptr5,0);
//skip ,
ch2=fgetc(f2);
char tmp6[100];
char *ptr6;
int p2=0;
//get the gold of the room
while(ch2!=','){
tmp6[p2]=ch2;
p2++;
ch2= fgetc(f2);
}
int hg2=strtol(tmp6,&ptr6,0);
//set the room as occupied
int oc2=0;
//add the players mana and gold to the rooms resources
hm2=hm2+mana;
hg2=hg2+gold;
//update the file
rewind(f2);
fprintf(f2,"%d,%d,%d",hm2,hg2,oc2);
//print sorry to leave page
printf("%s%c%c\n","Content-Type:text/html;charset=iso-8859-1",13,10);
printf("<html><head></head><body bgcolor='red'><center><img src='http://www.thecardking.com.au/wp-content/uploads/2012/08/02720A-1.jpg'></center></body></html>");
}
//else reprint the page and inform the user they entered the wrong command
else{
        printf("%s%c%c\n","Content-Type:text/html;charset=iso-8859-1",13,10);
        printf("<html><head><title>TheQuizz</title></head><body bgcolor='gold'><center><h1>WELCOME TO THE QUIZZ !</h1></center><u>You are only allowed to use the following commands</u><ul><li>PLAY</li><li>EXIT</li><li>DROP</li><li>REFRESH</li></ul><center><img src = '../quizz.jpeg' ></center><br><center><form action=http://cs.mcgill.ca/~hgokse/cgi-bin/transporter.py  method='get' style=float:center; ><input type=hidden name=inventory value=%d,%d><input type=hidden name=URL value=http://cs.mcgill.ca/~akouma1/cgi-bin/room.cgi><input type=submit value=North></form></center><center><form action='room.cgi' method='post' align='center'><input align='center' style='width: 500px; height 200px ;' type='text' name='command' placeholder='Answer here'><input type=hidden name=inventory value=%d,%d><input type=submit value= 'Submit Answer' ></form></center><form action=http://www.cs.mcgill.ca/~akouma1/cgi-bin/transporter.py  method='get' style=float:left; ><input type=hidden name=inventory value=%d,%d><input type=hidden name=URL value=http://cs.mcgill.ca/~akouma1/cgi-bin/room.cgi><input type=submit value=West></form><form action=http://cs.mcgill.ca/~yhe54/cgi-bin/transporter.py  method='get' style=float:right; ><input type=hidden name=inventory value=%d,%d><input type=hidden name=URL value=http://cs.mcgill.ca/~akouma1/cgi-bin/room.cgi><input type=submit value=East></form><br><center><form action=http://cs.mcgill.ca/~idouzi/cgi-bin/transporter.py  method='get' style=float:center; ><input type=hidden name=inventory value=%d,%d><input type=hidden name=URL value=http://cs.mcgill.ca/~akouma1/cgi-bin/room.cgi><input type=submit value=South></form></center><br><center><textarea bgcolor='gold' rows='5' cols='50' >You entered a wrong command. Try one of the suggested ones on the top.</textarea></center></body></html>",mana,gold,mana,gold,mana,gold,mana,gold,mana,gold);
}
}

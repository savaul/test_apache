#! /usr/bin/env python
import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import socket
import os, os.path
import time, sys
#except:
socket_txt="No socket, sorry"
#from urlparse import urlparse
argument = os.environ['REQUEST_URI']+"ls"
reply="No reply, yet"
color_merge="FFFFFF"
color_auto="FFFFFF"
#create an INET, STREAMing socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    sys.exit()


host = '';
port = 9000;

#try:
#    remote_ip = socket.gethostbyname( host )

#except socket.gaierror:
    #could not resolve
#    print 'Hostname could not be resolved. Exiting'
#    sys.exit()

#Connect to remote server
s.connect((host, port))

#Send some data to remote server
message = "browser"+str(argument)

try :
    #Set the whole string
    s.sendall(message)
except socket.error:
    #Send failed
    sys.exit()


#Now receive data
reply_brut = s.recv(4096)
STATE= reply_brut[13:14]
if STATE=="0":
	STATE="METEO"
elif STATE=="1":
	STATE="RADIO"
elif STATE=="2":
	STATE= "MAIL"
else:
	STATE= "NEWS"
shi=reply_brut.find("&", 15)
vol=reply_brut[15:shi]
MERGE=reply_brut[shi+1:shi+2]
if MERGE=="0":
	color_merge="#990000"
if MERGE=="1":
	color_merge="#00CC66"
shi2=reply_brut.find("&", shi+3)
STATIA=reply_brut[shi+3:shi2]
shi=shi2
shi2=reply_brut.find("&", shi+1)
AUTO=reply_brut[shi+1:shi2]
shi=reply_brut.find("&", shi2+1)
status_cent=reply_brut[shi2+1:shi]
if status_cent=="0":
	status_cent="OPRITA"
	color_auto="#990000"
if status_cent=="1":
	status_cent="PORNITA"
	color_auto="#00CC66"
if reply_brut.find("&", shi+1) !=-1:
	rss_txt=reply_brut[shi+1:-6]
else: rss_txt=""
reply= argument[18:]+"\n"+STATE+ " \n"+ "Volum "+vol +"\n" +"STATIA "+STATIA+"\n"+"Centrala este in regimul "+AUTO+"\n"+rss_txt
#reply=reply_brut
s.close()


#try:
#        if os.path.exists( "/tmp/python_unix_sockets_example" ):
#                os.remove( "/tmp/python_unix_sockets_example" )
#
#        server = socket.socket( socket.AF_UNIX, socket.SOCK_DGRAM )
#        server.bind("/tmp/python_unix_sockets_example")

#        socket_txt= server.recv( 1024 )
#        while not socket_txt:
#                socket_txt=server.recv( 1024 )
#                break
#                if "DONE" == socket_txt:
#                        break
#except:
#	socket_txt="bla_bla"

time_now=0
def get_time():
	time_now=time.time()

#socket_txt="text_variabil_&nbsp29 de caractere"
def html_out(variabila1, variabila2, color_m, color_a):
	print "Content-type: text/html"
	print
	print """
	<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
	<html xmlns="http://www.w3.org/1999/xhtml">
	<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
	<META HTTP-EQUIV="refresh" CONTENT="15">
	<title>Untitled Document</title>
	<style type="text/css">
	.arial {
		font-family: Arial, Helvetica, sans-serif;
		text-align: center;
		font-size: 14px;
	}
	</style>
	</head>
	<body>
	<table width="608" height="105" border="0" cellpadding="2" cellspacing="0">
	  <caption class="arial">
	  <strong>CONTROL PANEL
	  RASPBERRY
	  </strong>
	  </caption>
	  <tr>
            <td width="100" height="100" align="center" valign="middle"><form id="form1" name="form1" method="get" action="hello.py">
      	    <input name="v_up" type="submit" class="arial" id="v_upmm" value="V+" />
	    </form></td>
	    <td width="100" height="100" align="center" valign="middle"><form id="form2" name="form2" method="get" action="hello.py">
	      <input name="prog_up" type="submit" class="arial" id="prog_up"  value="P+" />
	    </form></td>
            <td width="100" height="100" align="center" valign="middle"><form id="form3" name="form3" method="get" action="hello.py">
              <input name="c_on" type="submit" class="arial" id="c_on"  value="      ON    " />
            </form></td>
            <td width="100" height="100" align="center" valign="middle"><form id="form4" name="form4" method="get" action="hello.py">
              <input name="c_f_on" type="submit" class="arial" id="c_f_on"  value="FULL ON" />
            </form></td>

	    <td width="188" rowspan="2" align="center" valign="middle"><img src="" alt="" name="camera" width="160" height="120" id="camera" /></td>
	  </tr>
	  <tr>
            <td width="100" height="100" align="center" valign="middle"><form id="form5" name="form5" method="get" action="hello.py">
              <input name="v_down" type="submit" class="arial" id="v_down"  value="      V-    " />
            </form></td>
            <td width="100" height="100" align="center" valign="middle"><form id="form6" name="form6" method="get" action="hello.py">
              <input name="prog_down" type="submit" class="arial" id="prog_down"  value="      P-    " />
            </form></td>
            <td width="100" height="100" align="center" valign="middle"><form id="form7" name="form7" method="get" action="hello.py">
              <input name="c_off" type="submit" class="arial" id="c_off"  value="     OFF    " />
            </form></td>
            <td width="100" height="100" align="center" valign="middle"><form id="form8" name="form8" method="get" action="hello.py">
              <input name="c_f_off" type="submit" class="arial" id="c_f_off"  value="  FULL OFF   " />
            </form></td>
	  </tr>
	  <tr>
            <td width="100" height="100" align="center" valign="middle" bgcolor="
	    """ + color_m + """
           "><form id="form9" name="form9" method="get" action="hello.py">
              <input name="radio_on_off" type="submit" class="arial"  id="radio_on_off"  value="    ON/OFF    " />
            </form></td>
	    <td width="100" height="100" align="center" valign="middle">&nbsp;</td>
            <td width="100" height="100" align="center" valign="middle" bgcolor="
	    """ + color_a +  """
            "><form id="form10" name="form10" method="get" action="hello.py">
              <input name="auto" type="submit" class="arial" id="auto"  value="   AUTO   " />
            </form></td>
	    <td colspan="2" rowspan="2" align="left" valign="middle">      <input name="radio_status" type="text" id="radio_status" value="" size="35" readonly="readonly" />
	    <input name="status centrala" type="text" id="status centrala" value=

	"""+ variabila1 +"""

	 "size="35" readonly="readonly" />
	    <textarea name="texte" id="texte" cols="35" rows="8">
	"""+variabila2+"""
	  </textarea></td>
	  </tr>
	  <tr>
            <td width="100" height="100" align="center" valign="middle"><form id="form11" name="form11" method="get" action="hello.py">
              <input name="meteo" type="submit" class="arial" id="meteo"  value="  METEO   " />
            </form></td>
            <td width="100" height="100" align="center" valign="middle"><form id="form12" name="form12" method="get" action="hello.py">
              <input name="rss" type="submit" class="arial" id="rss"  value="  RSS   " />
            </form></td>
            <td width="100" height="100" align="center" valign="middle"><form id="form13" name="form13" method="get" action="hello.py">
              <input name="mail" type="submit" class="arial" id="mail"  value="  MAIL   " />
            </form></td>
	  </tr>
	</table>
	</body>
	
	</html>
	""" 
	return

html_out(str(socket_txt), reply, color_merge, color_auto)

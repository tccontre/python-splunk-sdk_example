# python-splunk-sdk_example
simple python script using python-splunk-sdk for automating query and searches

# Installation:
1. set-up atleast 2 VM machine connected to each other (for this test 1 win7-client and (win10 - splunk monitoring instance))
2. install python 2.7
3. install python-splunk-sdk and put it to the PYTHONPATH of the machine.
4. set-up universal forwarder
5. enable monitoring for security event logs especially in log-in success and failure setting in gpedit.msc
6. then do some failure login and check if splunk instance catch it,
7. then test this script

<b>figure 1 - example of splunk search query after of some test <br /></b>

<img src ="2.PNG"> </img>

<b>figure 2 - example of remote execution of script. just change the host parameter in the code of the ipaddress of the splunk instance machine  <br /></b>

<img src ="3.PNG"> </img>

<b>figure 3 - script execution to the local machine where the splunk instance is installed  <br /></b>

<img src ="4.PNG"> </img>


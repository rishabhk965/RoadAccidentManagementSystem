
import socket as soc

# def main():
#     import time
#     from selenium import webdriver
#     from selenium.webdriver.chrome.options import Options
#     from twilio.rest import Client
#     import webbrowser
#     import requests
#     from PIL import Image
#     from pytesseract import pytesseract
    
#     options = webdriver.ChromeOptions()
#     options.headless = True
#     driver = webdriver.Chrome(options=options)

#     URL = 'http://192.168.43.1:8080/sensors.html'

#     driver.get(URL)
#     time.sleep(3)
#     S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
#     driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment                                                                                                                
#     driver.find_element_by_tag_name('body').screenshot('web_screenshot1.png')

#     driver.quit()
#     # Defining paths to tesseract.exe 
#     # and the image we would be using
#     path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#     image_path = r"web_screenshot1.png"
      
#     # Opening the image & storing it in an image object
#     img = Image.open(image_path)
      
#     # Providing the tesseract 
#     # executable location to pytesseract library
#     pytesseract.tesseract_cmd = path_to_tesseract
      
#     # Passing the image object to 
#     # image_to_string() function
#     # This function will
#     # extract the text from the image
#     text = pytesseract.image_to_string(img)
#     #print(text)
#     str1=[]
#     akmstr=[]
#     if("Get location" in text[:-1]):
#         akm=text.index("Get location")
#         for i in (text[(akm):]):
#             if(i.isdigit() or i=="."):
#                 str1.append(i)
#     for i in range(len(str1)):
#         if(str1[i]=="."):
#             akmstr.append(i)
#     #print(akmstr)
#     url1=str(str1[akmstr[0]-2])+str(str1[akmstr[0]-1])+'.'+str("".join(str1[(akmstr[0]+1):(akmstr[0]+6)]))
#     url2=str(str1[akmstr[1]-2])+str(str1[akmstr[1]-1])+'.'+str("".join(str1[(akmstr[1]+1):(akmstr[1]+6)]))
#     url=(f"https://www.google.com/maps/search/?api=1&query={url1},{url2}")
#     #print(url)
#     account_sid = '#' 
#     auth_token = '#' 
#     client = Client(account_sid, auth_token) 
#     message = client.messages.create( 
#                                   from_='whatsapp:+14#',  
#                                   body=f"{url}",      
#                                   to='whatsapp:+91#' 
#                               )
#     account_sid = '#'
#     auth_token = '#'
#     client = Client(account_sid, auth_token)
#     message = client.messages \
#           .create(
#                      body=f"{url}",
#                      from_='+1#',
#                      to='+91#'
#                  )
     
#     #print(message.sid)
# if __name__=="__main__":
#     main()


import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

number = '+917763829752'
ch_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_number, "en"))
service_provider = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_provider, "en"))


import serial, time, pynmea2


#Enable Serial Communication
# ser = serial.Serial("/dev/ttyS13", baudrate=9600, timeout=1)
# #Transmitting AT Commands to the Modem
# #\r indicates the Enter key

# ser.flushOutput()
# ser.flushInput()

# ser.write('ATE'+'\r') #Check to see if modem is responding
# str = ser.readline()
# print (str)
# time.sleep(5)


# ser.write('AT+CGPSOUT=32'+'\r') #Outputs raw NMEA data
# str = ser.readline()
# print (str)
# time.sleep(3)


# ser.write('AT+CGNSPWR=1,AT+CGPSSTATUS=?'+'\r') #Turns on the GPS power

# while str.find ("Location Not Fix") > 1:
#     print ('Waiting for a fix - ',str)
#     ser.flushInput()
#     ser.flushOutput()
#     time.sleep(15)
#     str = ser.readline(100)



# ser.write('AT+CGNSTST=1'+'\r') #Starts sending data to UART
# str = ser.readline()
# print (str)
# time.sleep(5)


# #Parsing Raw NMEA data through pynmea2

# ser.flushInput()
# ser.flushOutput()
# def parseGPS(str):
#     if str.find("GGA") > 0:
#         data = pynmea2.parse(str)
#         print ("Timestamp: %s -- Lat: %s %s -- Lon: %s %s " % (data.timestamp, data.latitude, data.lat_dir, data.longitude, data.lon_dir))


# while True:
#     str = ser.readline()
#     parseGPS(str)

coordinate = "'{'gps': {'altitude': -66.24295043945312, 'latitude': 10.59111675, 'longitude': 76.2170966, 'time': 1616769609000, 'accuracy': 3.2160000801086426, 'speed': 0, 'provider': 'gps', 'bearing': 0}, 'network': {'altitude': 0, 'latitude': 10.5894624, 'longitude': 76.214415, 'time': 1616769602806, 'accuracy': 1500, 'speed': 0, 'provider': 'network', 'bearing': 0}}'";
s = soc.socket()
host = "127.0.0.1"
port = 443
s.setsockopt(soc.SOL_SOCKET, soc.SO_REUSEADDR, 1)
s.bind((host,port))


sockInfo = soc.getnameinfo(("93.184.216.34", 443), soc.NI_NOFQDN);

print(sockInfo);
print(coordinate);
s.listen(1)
c,addr = s.accept()
if True:
    print(c.recv(2048).decode('ascii'))
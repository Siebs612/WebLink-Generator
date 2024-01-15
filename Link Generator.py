"""
Link Generator app

@author Paul Siebenaler
@date 01/15/24
@version 1.0

This is a simple srcipt that opens the command terminal and allows the user
to enter a URL. This will check to see if it is a vaild url. If it is valid
then a new python file will be created in the same directory that will allow
you to double click the .py file and it will automatically display the 
designated webpage.

@note I found that there was too many steps to create a shortcut, so I
automated it with the class.

@note to switch the web browser of choice the user must go into this
code and edit the browser variable to point to the correct browser
start location.

>> look Here if you are having issues: https://docs.python.org/3/library/webbrowser.html

"""

import webbrowser as wb
import validators

def create_new_file(path):
    
    code = """
\
import webbrowser as wb
url = "{}"
browser = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
wb.register('google-chrome', None, wb.BackgroundBrowser(browser))
wb.get('google-chrome').open(url)
            """.format(path)
    
    with open('Link.py', 'w') as file:
        file.write(code)

if __name__ == "__main__":
    count = 10
    while(True):
        url = input("Enter a URL: ")
        if validators.url(url):
            create_new_file(url)
            quit()
        print("Invalid URL")
        user = input('exit?(y/n): ')
        if user=='y':
            quit()
        if count < 0:
            print('Too Many Failed Attempts... Exiting')
            quit()
        count-=1
    

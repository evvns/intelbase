#!/usr/bin/env python3




from bs4 import BeautifulSoup
import re
import requests
import ipaddress
import datetime
from datetime import datetime
from googlesearch import search
import webbrowser
import readline



print("Loading Successful.")




def printintelbasebanner():
    """
    intelbase banner
    """
    print("""\u001b[32m\033[1m


.__        __         .__ ___.                         
|__| _____/  |_  ____ |  |\_ |__ _____    ______ ____  
|  |/    \   __\/ __ \|  | | __ \\__  \  /  ___// __ \ 
|  |   |  \  | \  ___/|  |_| \_\ \/ __ \_\___ \\  ___/ 
|__|___|  /__|  \___  >____/___  (____  /____  >\___  >
        \/          \/         \/     \/     \/     \/                                                                  

GitHub:  https://github.com/evaannn                                                        
Twitter: @deserializing 
Instagram: @mainframes
___________________________________________________________________ \033[0m\n""")



# Proton API Check/Verification

def checkprotonapistatus():
    """
    Proton API Online or Offline Check
    """
    requestprotonmailstatus = requests.get('https://api.protonmail.ch/pks/lookup?op=index&search=admin@protonmail.com')
    if requestprotonmailstatus.status_code == 200:
        print(
            "\u001b[32m\033[1m\n\nGood to go! ProtonMail API is ONLINE!!!\u001b[32m \U0001F7E2 \033[0m\n\n")
    else:
        print(
            "\u001b[31m Protonmail API is OFFLINE\U0001F534")


# intelbase Choices

def printintelbaseintro():
    intelbaseintro = """
\n\n\u001b[31m\U0001F575\033[1m INTEL SCRAPE METHODS:\n

\u001b[32m\U0001F50D \033[1mCONTRAST\033[0m\u001b[32m: Check if ProtonMail account exists\n

\u001b[32m\U0001F4E1 \033[1mAGENT\033[0m\u001b[32m: Proton Email search to check for digital footprints\n

\u001b[32m\U0001F3F4 \033[1mRIPTIDE\033[0m\u001b[32m: Dark Web search\n 

\u001b[32m\U0001F511 \033[1mLOCKSMITH\033[0m\u001b[32m: Get ProtonMail user PGP Key + Key creation date\n

\u001b[32m\U0001F4BB \033[1mPERISCOPE\033[0m\u001b[32m: Verify IP address belongs to ProtonVPN user\n
"""
    print(intelbaseintro)




# Retrieve the timestamp of created email addreses

def extract_timestamp(mail, source_code):

    try:
        timestamp = re.sub(':', '', re.search(':[0-9]{10}::', source_code.text)[0])
        return datetime.fromtimestamp(int(timestamp))
    except AttributeError:
        return None


# Check if this is a business email address

def check_domain_name(mail):
    return mail.split("@")[1] not in ["protonmail.com", "proton.me"]


# Perform the API request

def make_api_request(mail):
    try:
        request = requests.get("https://account.proton.me/api/users/available", 
            headers={
                "x-pm-appversion":"web-account@5.0.11.11",
                "x-pm-locale":"en_US"
            },
            params={
                "Name":mail,
                "ParseDomain":"1"
            })

        is_business_address = check_domain_name(mail)

        #Return code 429 = API limit exceeded
        if (request.status_code == 409):
            source_code = requests.get(
                f'https://api.protonmail.ch/pks/lookup?op=index&search={mail}'
            )

            creation_date = extract_timestamp(mail, source_code)

            print("\033[1m\n\nProtonMail Account is VALID! Creation date: " + str(creation_date) + " \033[0m\U0001F4A5")

            return True

        elif(request.status_code == 429):
            print("\u001b[31m\n\nAPI requests limit exceeded...")

        elif is_business_address:
            print("\u001b[33m\nProtonmail API does not handle business emails, "
                  "but you can get account creation date + PGP Key")
            return True
        else:
            print("\u001b[31m\n\nProtonMail account is NOT VALID")

        return False

    except:
        print("Error when requesting the API")
        return False


# ProtonMail account validity check

def protonmailaccountcheck():
    """
    ALPHA : Check if ProtonMail account exists
    """
    invalidEmail = True
    regexEmail = "([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"

    print(
        "\033[1m\u001b[32m\nCheck if ProtonMail account exists \n")
    while invalidEmail:

        mail = input("\033[1mType Email address + Enter : ")

        if (re.search(regexEmail, mail)):
            invalidEmail = False

        else:
            print("\u001b[31m\n\nProtonMail user does not exist\u001b[32m")
            invalidEmail = True

    make_api_request(mail)


# Email search for Digital Footprints

def emailtraces():
    """
    BRAVO : Check Email Traces with a Google Dork
    """

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)\
                AppleWebKit/537.36 (KHTML, like Gecko) Cafari/537.36'}

    print("\033[1m\u001b[32m\nChecking server status\n")
    response = requests.get('https://google.com', headers)
    print(response)
    if response.status_code == 200:
        print('Status: Success!\n')
    elif response.status_code == 404:
        print('404 Not Found, please try again.')

    searchfor = input(
        """\u001b[32mEnter Target Email in quotation marks!(Example:"admin@protonmail.com"): """)
    print("\nProcessing request...\n")

    for result in search(searchfor, tld="com", stop=10, pause=2):
        print(result)


# DarkWeb email search

def darkwebtraces():
    """
    CHARLY : Check Dark Web Traces
    """

    print("\033[1m\u001b[32m\nChecking server status\n")
    response = requests.get('https://ahmia.fi')
    print(response)
    if response.status_code == 200:
        print('Status: Success!\n')

    elif response.status_code == 404:
        print('404 Not Found, please try again')

    choice = input(
        """\033[1mView results in Browser [B] or Terminal [T]: """)

    if choice == "B":
        darkwebbrowser()

    if choice == "T":
        darkwebterminal()


# Dark Web Search with Browser auto-opening

def darkwebbrowser():
    """
    Dark Web Browser Open

    """
    query = input("""\nInput Target email (example: darkmatterproject@protonmail.com: """)
    webbrowser.open(f"https://ahmia.fi/search/?q={query}")


# Dark web search results displayed within the terminal

def darkwebterminal():
    """
    Dark Web Terminal

    """

    query = input("Input target email: ")
    URL = f"https://ahmia.fi/search/?q={query}"
    page = requests.get(URL)
    request = requests.get(URL)

    if request.status_code == 200:
        print("\n\nRequest went through\n")

    soup = BeautifulSoup(page.content, "html.parser")
    for a_href in soup.find_all("a", href=True):
        print(a_href["href"])


# Get ProtonMail user PGP Key

def pgpkeyinformation():
    """
    DELTA: Get ProtonMail user PGP Key & Info

    """

    choice = input(
        """\033[1m\nView PGP Key in Terminal [T] or Download Key [D]: """)

    if choice == "T":
        pgpkeyview()

    if choice == "D":
        pgpkeydirectdownload()


# Download PGP Key

def pgpkeydirectdownload():
    """
    Download PGP Key Directly

    """

    query = input(
        """\nInput Target email to Scrape PGP Key: """)
    webbrowser.open(f"https://api.protonmail.ch/pks/lookup?op=get&search={query}")


# extract PGP Key

def extract_key(source_code):
    """
    Extract the key type and length of the email address
    """

    regex = ':[0-9]{2,4}:(.*)::'

    try:
        return re.search(regex, source_code.text)[0].split(":")[1]
    except AttributeError:
        return None

# View PGP Key within terminal

def pgpkeyview():
    """
    View PGP Key in Terminal

    """

    invalidEmail = True
    regexEmail = "([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"

    print(
        "\033[1m\nInput Protonmail user email to get user's PGP Key\n")
    while invalidEmail:

        mail = input("\033[1mType Proton email + Enter: ")

        if (re.search(regexEmail, mail)):
            invalidEmail = False
        else:
            print("\u001b[31m\n\nProtonmail user does not exist\u001b[32m")
            invalidEmail = True

    #Business addresses are not handled with the new API, so there is a risk that the email doesn't exists and returns a random timestamp

    if(make_api_request(mail)):
        source_code = requests.get('https://api.protonmail.ch/pks/lookup?op=index&search=' + mail)

        if("info:1:0" in source_code.text):
            print("\u001b[31m\n\nCan't retrieve the PGP information\u001b[32m")
        else:
            timestamp = extract_timestamp(mail, source_code)
            key = extract_key(source_code)

            print("\u001b[32mPGP Key Date and Creation Time:", str(timestamp))

            if(key != "22"):
                print("\u001b[32mEncryption Standard : RSA " + key + "-bit")
            else:
                print("\u001b[32mEncryption Standard : ECC Curve25519")

            # Get the USER PGP Key
            invalidResponse = True

            print("\033[1m\nGet user PGP Key? ")
            while invalidResponse:
                # Input
                responseFromUser = input("""\033[1m [Y] or [N]:\033[0m """)
                # Text if the input is valid
                if responseFromUser == "Y":
                    invalidResponse = False
                    requestProtonPublicKey = requests.get('https://api.protonmail.ch/pks/lookup?op=get&search=' + str(mail))
                    bodyResponsePublicKey = requestProtonPublicKey.text
                    print(bodyResponsePublicKey)
                elif responseFromUser == "N":
                    invalidResponse = False
                else:
                    print("Input Not Valid")
                    invalidResponse = True


# Check user IP belongs to ProtonVPN user

def protonvpnipsearch():
    """
    ECHO : Find out if user IP address is a ProtonVPN user
    """

    while True:
        try:
            ip = ipaddress.ip_address(input(
                '\033[1m\n\nEnter Target IP address: (Example: "185.159.157.1"): '))
            break
        except ValueError:
            continue

    requestProton_vpn = requests.get('https://api.protonmail.ch/vpn/logicals')
    bodyResponse = requestProton_vpn.text
    if str(ip) in bodyResponse:
        print(
            "\033[1m\n\nThis IP belongs to a ProtonVPN user! \n")
    else:
        print(
            "\u001b[31m\033[1m\n\nThis IP does not belong to a ProtonVPN user\n")

# main

def main():
    printintelbasebanner()
    choice = input(
        """\033[1m\u001b[32mType [c] or [C] to check Proton API Status: \033[0m\u001b[32m""")
    if choice in ["c", "C"]:
        checkprotonapistatus()
    choice = input("""\033[1mView All Options? \u001b[32m [Y] or [N]:\033[0m\u001b[32m """)
    if choice == "Y":
        printintelbaseintro()

    while True:
        choice = input("""\033[1mInput CAPITAL LETTER from each option to make choice!\n"""
                       """\nA | B | C | D |E"""
                       """\nInput choice:  """)
        if choice == "A":
            protonmailaccountcheck()
        if choice == "B":
            emailtraces()
        if choice == "C":
            darkwebtraces()
        if choice == "D":
            pgpkeyinformation()
        if choice == "E":
            protonvpnipsearch()

        inp = input("\n\n\u001b[32m\033[1mContinue [Y] or [N]: ")
        if inp.lower() == 'n':
            break



if __name__ == '__main__':
    main()

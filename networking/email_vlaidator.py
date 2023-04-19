import re
def check_email(email):
    pattern = r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, email):
        return True
    else:
        return False

if __name__ == "__main__":
    print(check_email('bipin.csit.etc@gmail.com'))
    print(check_email('bpnsengar@outlook.com'))
    print(check_email('bipin768@hi5.co'))
    print(check_email('bipin768@hi5.'))
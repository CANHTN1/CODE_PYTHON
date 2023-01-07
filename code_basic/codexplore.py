def emailProcess(email):
    email_username = email[0:email.index("@")]
    email_domain = email[email.index("@")+1:]
    # print (f"Username is {email_username}")
    return[email_username, email_domain]
  
def printmsg(email_username, email_domain):
    print(f"username is {email_username}; Email domain is {email_domain}")

def main():
    email = input("lam on hay nhap email: ").strip()
    email_username, email_domain = emailProcess(email)
    #print (emailProcess(email))
    printmsg (email_username, email_domain)
if __name__ == "__main__":
   main()
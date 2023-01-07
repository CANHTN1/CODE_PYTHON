from codexplore import emailProcess, printmsg
 
def main():
    emails = ['canh@gmail.com', 'canh1111@yahoo.com', 'thuy@balana.cn']
    for email in emails:
        email_username, email_domain = emailProcess(email)
        printmsg(email_username, email_domain)

if __name__ == "__main__":
    main()
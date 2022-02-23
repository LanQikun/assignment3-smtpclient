from socket import *

# port 1025 and mail server address 127.0.0.1
# In order to limit spam, some mail servers do not accept TCP connections
# from arbitrary sources. For the experiment described below, you may want to try connecting both to your university
# mail server and to a popular Webmail server, such as an AOL mail server. To connect to the university mail server,
# you will need to use NYU's VPN


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))

    def send(s):
        clientSocket.send(s.encode())

    # recv = clientSocket.recv(1024).decode()
    # print(recv) #You can use these print statement to validate return codes from the server.
    # if recv[:3] != '220':
    #     print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    send(heloCommand)
    # recv1 = clientSocket.recv(1024).decode()
    # print(recv1)
    # if recv1[:3] != '250':
    #     print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    mail = 'bob@gmail.com'
    temp1 = '{}: <' + mail + '>\r\n'
    mailFrom = temp1.format('MAIL FROM')
    send(mailFrom)

    # Send RCPT TO command and handle server response.
    rcptTo = temp1.format('RCPT TO')
    send(rcptTo)

    # Send DATA command and handle server response.
    data = "test\r\n"
    send(data)

    # Send message data.
    temp2 = '{}: ' + mail
    theTo = temp2.format('To')
    theFrom = temp2.format('from')
    subject = 'Subject: test'
    for x in theTo, theFrom, subject, msg:
        send(x)

    # Message ends with a single period, send message end and handle server response.
    for x in endmsg, msg:
        send(x)

    # recv2 = clientSocket.recv(1024).decode()
    # print(recv2)
    # if recv2[:3] != '250':
    #     print('250 reply not received from server.')

    # Send QUIT command and handle server response.
    theQuit = 'QUIT\r\n'
    send(theQuit)

    # recv3 = clientSocket.recv(1024).decode()
    # print(recv3)
    # if recv3[:3] != '221':
    #     print('221 reply not received from server.')


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')

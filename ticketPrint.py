#by knight
import qr_code
import InfoOnTemplate
import emailPart

ticket_no = 0

def printTicket(name,email,phone_number):
    
    global ticket_no

    input_data = f"NAME: {name} TICKET NO: {ticket_no}"
    qr_code.generate_qr_code(input_data,ticket_no)
    
    #savedImage = f"out{ticket_no}.png"

    ticket_filename = InfoOnTemplate.create_ticket(name,email,phone_number,ticket_no)

    emailPart.sendMail(email,ticket_filename)

    ticket_no += 1     

#printTicket("test_name","dhruvanu3@gmail.com","0123456789")
#by knight
from PIL import Image ,ImageDraw, ImageFont

def create_ticket(name,email,phone_number,tick_no):
    
    template_image = Image.open("name.png") #to change
    draw = ImageDraw.Draw(template_image)

    font_ = ImageFont.truetype("arial.ttf", 24) #change if want
    tick_no_str = str(tick_no)

    name_position = (130, 75) #to change
    email_position = (130, 160) #to change
    phone_positon = (130,245) #to change
    tick_no_positon = (5,5) #to change

    draw.text(name_position, name, font=font_, fill="black")
    draw.text(email_position, email, font=font_, fill="black")
    draw.text(phone_positon,phone_number,font=font_,fill='black')
    draw.text(tick_no_positon,tick_no_str,font=font_,fill='black')

    qr_code_image = Image.open(f"out{tick_no}.png")
    qr_code_image = qr_code_image.resize((200, 200))

    qr_code_position = (650, 85) #to change

    template_image.paste(qr_code_image, qr_code_position)

    #template_image.show() 
    template_image.save(f"ticket{tick_no}.png")

    tic_filename = f"ticket{tick_no}.png"
    
    return tic_filename

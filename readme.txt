ticketPrint is the main module you need to use, import it in your program and pass name,email and phone number in those order 

-> changes needed to be done 

    1 In qr_code

        changes not recomended 
        output file name can be changed but will have to alter in other modules 
    
    2 In InfoOnTemplate
 
        line 5 add template_image = Image.open("  template.png   ")
        name_position, email_position, phone_positon, tick_no_positon and qr_code_position changed according to the template

    3 In emailPart 

        user = add sender's email
        for password you need to go to mannage my account -> security -> two factor auth -> app password -> genrate password for mail
        add subject and body as per your wish 

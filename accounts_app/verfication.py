def email_creation(user, code):
    
    email_body ='''
    Hi %s,

    Here is your account activation code:

    %s

    Thank you
    Microcircuit Team 
    ''' % (user, code)
    return email_body
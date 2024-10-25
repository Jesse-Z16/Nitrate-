# Nitrate program
#Write a program that outputs how much carbon to dose from the nitrate. Greater than 10 is 3ml,
#greater than 2.5 is 2ml, greater than 1 is ml, or 0.5ml if the nitrate is equal to or less than 1.

# -------------------------
# Subprograms
# -------------------------

nitrate = float(input('How much nitrate is in the fish tank in ml?  '))

def calculate_dose(nitrate):
    if nitrate > 10:
        print('For',nitrate,'ml of nitrate, the dose of carbon is 3ml')
    elif nitrate > 2.5 and nitrate < 10:
        print('For',nitrate,'ml of nitrate, the dose of carbon is 2mml')
    elif nitrate > 1 and nitrate < 2.5:
        print('For',nitrate,'ml of nitrate, the dose of carbon is 1ml')
    elif nitrate <= 1:
        print('For',nitrate,'ml of nitrate, the dose of carbon is 0.5ml')
    else:
        print('enter a valid ml for nitrate')
        
print(calculate_dose(nitrate))

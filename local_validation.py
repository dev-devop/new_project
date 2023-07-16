from rest_framework.serializers import ValidationError

def newPasswordValidator(entry)->str:
    if entry.isalpha():

        raise ValidationError('oops your password should contain at least one Numerical character')
    elif len(entry) <= 7:

        raise ValidationError('sorry your password should be at least 8 characters long')
    elif entry.isdigit():
        raise ValidationError('sorry your password should have at least 1 alphabet character')
   
def numberValidation(entry):
    pass

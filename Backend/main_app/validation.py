from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class CustomPasswordValidator:
    def validate(self, password, user=None):
        if not any(char.isdigit() for char in password):
            print("Validation error: Must contain at least one number")
            raise ValidationError(_("Must contain at least one number"), code='password_no_number',)
        
        if len(password) < 7:
            raise ValidationError(_("The password must be at least 7 characters long."), code='password_too_short',)
        
        if len(password) > 50:
            raise ValidationError(_("The password must be no more than 50 characters long."), code='password_too_long')
        
        if not any(char.isupper() for char in password):
            raise ValidationError(_("Password must contain at least one uppercase"), code='password_no_upper',)
        
        if not any(char in '!@#$%^&*()_=-+[]|;:,.<>?/' for char in password):
            raise ValidationError(_("Password must contain at least one special character"), code='password_no_special',)
        
    def get_help_text(self):
        return _(
            "Your password must be between 7 and 50 characters long, & contain at least 1 uppercase, number and special character"
        )
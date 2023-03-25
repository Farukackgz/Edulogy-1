from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    def _init_(self, *args, **kwargs):
        super(UserCreateForm, self)._init_(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update(
                                      {'class': 'form-control'})
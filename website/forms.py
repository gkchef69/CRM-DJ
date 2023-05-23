from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SingUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Διεύθυνση Email'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ονομα'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Επώνυμο'}))
    
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
    
    def __init__(self, *args, **kwargs):
        super(SingUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Απαιτείται. Μέχρι 150 χαρακτήρες. Γράμματα, ψηφία και @/./+/-/_ μόνο.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Ο κωδικός πρόσβασής σας δεν μπορεί να είναι πολύ παρόμοιος με τα άλλα προσωπικά σας στοιχεία.</li><li>Ο κωδικός πρόσβασής σας πρέπει να περιέχει τουλάχιστον 8 χαρακτήρες.</li><li>Ο κωδικός πρόσβασής σας δεν μπορεί να είναι κωδικός πρόσβασης που χρησιμοποιείται συνήθως.</li><li>Ο κωδικός πρόσβασής σας δεν μπορεί να αποτελείτε μόνο από αριθμητικά ψηφία.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Εισαγάγετε τον ίδιο κωδικό πρόσβασης με πριν, για επαλήθευση.</small></span>'
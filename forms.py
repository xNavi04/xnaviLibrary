from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField, PasswordField, BooleanField
from wtforms.validators import DataRequired, ValidationError
from datetime import datetime

class categoriesForm(FlaskForm):
    name = StringField("Nazwa", validators=[DataRequired()])
    submit = SubmitField("zatwierdź")

class storesForm(FlaskForm):
    name = StringField("Nazwa", validators=[DataRequired()])
    submit = SubmitField("zatwierdź")

class borrowForm(FlaskForm):
    borrower = StringField("Pożyczający", validators=[DataRequired()])
    finish_date = DateField("Data oddania", validators=[DataRequired()])
    submit = SubmitField("zatwierdź")

    def validate_finish_date(self, field):
        if field.data and field.data < datetime.now().date():
            raise ValidationError('Data musi być równa lub późniejsza od dnia dzisiejszego!')

class itemForm(FlaskForm):
    title = StringField("Tytuł", validators=[DataRequired()])
    author = StringField("Autor/wydawnictwo", validators=[DataRequired()])
    category = SelectField("Kategoria", choices=[], validators=[DataRequired()])
    store = SelectField("Magazyn", choices=[], validators=[DataRequired()])
    submit = SubmitField("zatwierdź")

class itemFormForBorrow(FlaskForm):
    title = StringField("Tytuł", validators=[DataRequired()])
    author = StringField("Autor/wydawnictwo", validators=[DataRequired()])
    borrower = StringField("Pożyczający", validators=[DataRequired()])
    category = SelectField("Kategoria", choices=[], validators=[DataRequired()])
    store = SelectField("Magazyn", choices=[], validators=[DataRequired()])
    finish_date = DateField("Data oddania", validators=[DataRequired()])
    submit = SubmitField("zatwierdź")

    def validate_finish_date(self, field):
        if field.data and field.data < datetime.now().date():
            raise ValidationError('Data musi być równa lub późniejsza od dnia dzisiejszego!')

class selectCategoryForm(FlaskForm):
    categories = SelectField("Kategoria", choices=[], validators=[DataRequired()])
    submit = SubmitField("zatwierdź")

class addPermissionToUserForm(FlaskForm):
    reading = BooleanField("Czytanie")
    editing = BooleanField("Edycja")
    deleting = BooleanField("Usuwanie")
    adding = BooleanField("Dodawanie")
    submit = SubmitField("zatwierdź")

class selectStoreForm(FlaskForm):
    stores = SelectField("Magazyn", choices=[], validators=[DataRequired()])
    submit = SubmitField("zatwierdź")

class confirmReturnForm(FlaskForm):
    password = PasswordField("Wprowadź hasło", validators=[DataRequired()])
    submit = SubmitField("zatwierdź")
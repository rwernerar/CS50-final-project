import string
import random

from flask import Flask, flash, redirect, render_template, request


# Configure application
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Default settings to render template
DEFAULT_SETTINGS = {
                    'allow_numbers': 'checked',
                    'allow_upperc': 'checked',
                    'exclude_similar': '',
                    'allow_symbols': 'checked',
                    'allow_lowerc': 'checked',
                    'exclude_duplicate': ''
}


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
#@login_required
def index():
    """Renders default index"""

    return render_template("index.html", settings=DEFAULT_SETTINGS, password_length=8, password="")


@app.route("/gencopypassword", methods=["GET", "POST"])
def gencopypassword():
    """Generates password or copies password to clipboard"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Get settings
        settings = {
            "allow_numbers": "checked" if request.form.get("allow_numbers") else "",
            "allow_upperc": "checked" if request.form.get("allow_upperc") else "",
            "exclude_similar": "checked" if request.form.get("exclude_similar") else "",
            "allow_symbols": "checked" if request.form.get("allow_symbols") else "",
            "allow_lowerc": "checked" if request.form.get("allow_lowerc") else "",
            "exclude_duplicate": "checked" if request.form.get("exclude_duplicate") else ""
        }

        # Get password length and password
        password_length = request.form.get("password_lenght")
        password = request.form.get("password")

        if request.form['submit'] == 'genpassword':

            # Check consistency of password length
            if not password_length:
                flash("Must provide Password Length", "error")
                return render_template("index.html", settings=settings,
                                    password_length=password_length, password="")
            elif not password_length.isnumeric():
                flash("Must provide a valid Password Length", "error")
                return render_template("index.html", settings=settings,
                                    password_length=password_length, password="")
            elif int(password_length) < 8 or int(password_length) > 20:
                flash("Password Lenght must be between 8 and 20", "error")
                return render_template("index.html", settings=settings,
                                    password_length=password_length, password="")
            else:
                password_length = int(password_length)

            # check at least one character set is selected
            if (not settings['allow_numbers'] and not settings['allow_upperc'] and
                not settings['allow_symbols'] and not settings['allow_lowerc']):
                flash("You must select at least one of the 4 available character sets", "error")
                return render_template("index.html", settings=settings,
                                    password_length=password_length, password="")

            # creates total selected character set
            char_set = ''
            if settings['allow_numbers']: char_set += string.digits
            if settings['allow_upperc']: char_set += string.ascii_uppercase
            if settings['allow_symbols']: char_set += "!@#$%^&*.()+"
            if settings['allow_lowerc']: char_set += string.ascii_lowercase

            # removes similar chracters from character set if required
            if settings['exclude_similar']:
                for c in 'iI1loO0':
                    if c in char_set:
                        char_set = char_set.replace(c, '')

            # --- Generates random passwords ---
            password = ''

            # No duplicate characters
            if settings['exclude_duplicate']:
                for _ in range(password_length):
                    char = random.choice(char_set)
                    password += char
                    char_set = char_set.replace(char, '')
                    if not char_set:
                        flash("You must provide enought different characters for selected password length", "error")
                        return render_template("index.html", settings=settings,
                                            password_length=password_length, password="")

            # Simple password, characters can repeat, similar characters are included
            else:
                for _ in range(password_length):
                    password += random.choice(char_set)

            # Renders result
            return render_template("index.html", settings=settings,
                                    password_length=password_length, password=password)

        # Copy password to clipboard. Render html with javascript
        if request.form['submit'] == 'copy':

            # Check if password was generated
            if password == '':
                flash("Must generate a password", "error")
                return render_template("index.html", settings=settings,
                                            password_length=password_length, password="")

            # Render same HTML with javascript
            flash("Password copied!")
            return render_template("index.html", settings=settings,
                                    password_length=password_length, password=password, copy=True)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return redirect("/")
        #render_template("index.html", settings=DEFAULT_SETTINGS, password_length=8, password="")

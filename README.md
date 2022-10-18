# STRONG PASSWORD GENERATOR
#### Video Demo:  <https://youtu.be/vdE4TG2Jrxg>
#### Description:

Password generators help those who have to constantly come up with new passwords to ensure authorized access for programs and to manage a large number of passwords for identity and access management.

Password generators should be used with password managers in order to keep passwords save. This also avoids having to use the same password for accessing different applications, since the user does not have to remember it. A password generator and a password manager combined, are a great solution for dealing with different strong passwords.

In this project I have built a web application that is aimed to generate strong random passwords by letting the user choose between a variety of different options:

* Upper- and lower-case characters, symbols and numbers.

* If character repetition is an option or not, as well as avoiding similar characters such as “iI1loO0”.

* Password lenght, between 8 and 20 characters.

After password generation is successful, copying the password to the clipboard is also available. Though, keep in mind that there exist programs that keep track of the clipboard in order to steal passwords. The same is true for typing in a password (this programs are called keyloggers), but in this case it can be solved by using virtual keyboards (on screen).

## Project Files & Technical Description

### Technical Description:

The project was coded using:
+ python 3.6
+ flask framework 2.0
+ jinja 2
+ html
+ CSS / Bootstrap 5.1
+ JS

Password calculations and webpage re-rendering was done using python and flask framework in combination with jinja.
Clipboard copying was implemented using java script. The short script that enables copying text to clipboard was taken from [here](https://www.w3schools.com/howto/howto_js_copy_clipboard.asp) and slightly modified:

```
<script>
var copyText = document.getElementById("password");
    // Select the text field
copyText.select();
copyText.setSelectionRange(0, 99999); // For mobile devices

// Copy the text inside the text field
navigator.clipboard.writeText(copyText.value);

</script>
```

### Design:

Regarding the design I’m fully conscious that flask and a backend is not strictly necessary in this case. Everything could have been coded using just javascript on the frontend side. Since I wanted to practice a little more Flask and on the other hand, I’m still not very confident coding in javascript, I decided to do it this way!
This approach helped me to learn how to manage many buttons in the same form using Flask for example.

It is also worth mentioning that the web interface was designed to my best effort to work correctly on mobile devices too, although this was not fully achieved and still needs some adjustments.


### Files:

- **/app.py:** contains all the necessary logic to perform random password calculations given user’s input. Leverages `random` and `string` libraries besides Flask framework

- **/templates/layout.html:** contains the basic layout of the webpage

- **/templates/index.html:** extends layout.html and is the main webpage, with all the jinja constrains and JS

- **/static/:** contains webpage’s icon and a CSS file for basic customization


#!/usr/bin/env python3
import cgi
import subprocess

print("Content-type: text/html\n")

# Get user input from the form
form = cgi.FieldStorage()
code = form.getvalue("code")

# Compile and run the code
try:
    output = subprocess.check_output(["python3", "-c", code], stderr=subprocess.STDOUT, timeout=10, universal_newlines=True)
    print("{}".format(output))
except subprocess.CalledProcessError as e:
    print("<p>Error:</p>")
    print("<pre>{}</pre>".format(e.output))
except subprocess.TimeoutExpired:
    print("<p>Execution timed out.</p>")
except Exception as e:
    print("<p>An error occurred: {}</p>".format(e))

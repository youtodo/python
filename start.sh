chmod 777 ./cgi-bin/*.py
echo "__________*** Grants the right to execute the scripts ***__________"
python3 -m http.server --cgi
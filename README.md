brute-hsm v0.1
=========
The purpose of this script is connect and try several pins/puks for SO and User in HSM. 

Warning: You should be carefully to test the brute forcing because almost all manufactures has pin lock policy use for your own risk!!! 


Pre-requirements pykcs11 (pkcss11 wrapper for python) 

to install you can use pip or easy_install 


pip install pykcs11 


easy_install pykcs11

usage: 

python brute.py wordlist.txt library-that-you-want-to-use.dll for default I'm loading the criptoki.dll for eracom connection


If you have any think to add please send mail to tvilas at hushmail dot com

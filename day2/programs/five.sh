#read the password and echo back with "*"
password=""
echo "Enter username: "
read username
echo "Enter password: "
while IFS= read -r -s -n 1 char
do
	if [[ $char == "" ]]; then
		break
	fi
	password+="$char"
	printf "*"
done
echo "Password entered"


#IFS =  ensure spaces are not discarded
#-r = reads special characters
#-s = silent mode
#-n1 = allow the script to read all the characters

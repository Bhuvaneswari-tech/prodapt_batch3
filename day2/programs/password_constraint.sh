#read the password with constraints - 8 characters
echo "Enter username: "
read username
echo "Enter password(8 characters): "
password=""
while IFS= read -r -s -n 1 char
do
	#stop when Enter pressed
	if [[ -z "$char" ]]; then
		break
	fi
	#Accept only 8 characters
	if [[ ${#password} -lt 8 ]]; then
		password+="$char"
		printf "*"
	fi
done

#Validation
if [[ ${#password} -ne 8 ]]; then
	echo "Password must be exactly 8 characters long"
	exit 1
fi

#Validation rules

if [[ "$password" =~ [A-Z] && "$password" =~ [a-z] && "$password" =~ [0-9] && 
"$password" =~ [^a-zA-Z0-9] ]];
then
	echo "Password is valid"
	echo "Entered password: $password"
else
	echo "Invalid Password"
	echo "Password must contain one uppercase, one lowercase, one digit, one special characters"
fi




check_odd_even(){
if [[ $(($1 % 2)) -eq 0 ]]
then
	echo "$1 is even"
else
	echo "$1 is odd" 
fi
}

check_odd_even 10


reverse_string(){
str=$1
rev_str=""
for  (( i=${#str}-1; i>=0; i-- ))
do
	rev_str="$rev_str${str:$i:1}"
done

echo "$rev_str" 
}

reverse_string "Linux"

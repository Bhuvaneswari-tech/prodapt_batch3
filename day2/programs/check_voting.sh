echo "Enter your age: "
read age

if [[ $age -ge 18 ]]; then
	echo "Eligible to vote"
else
	echo "Not eligible to vote"
fi

#Greatest of two numbers
echo "Enter the first number: "
read first
echo "Enter the second number: "
read second
if [[ $first -gt $second ]]; then
	echo "$first is greater"
elif [[ $first -lt $second ]]
then
	echo "$second is greater"
else
	echo "Both are equal"
fi

#use for loop to print multiplication table
echo "Enter a number: "
read num
for i in {1..10}
do
	echo "$num X $i = $((num*i))"
done

#While loop (print 1 to 10)
count=1
while [[ $count -le 10 ]]
do
	echo -n "$count "
	count=$((count+1))
done
echo



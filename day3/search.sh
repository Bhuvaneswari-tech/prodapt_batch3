search_word(){
file=$1
word=$2

if grep -qi "$word" "$file"
then
	echo "'$word' found in $file"
else
	echo "'$word' not found in $file"
fi
}

search_word file1.txt linux

count_word(){
file=$1
word=$2

count=$(grep -o "$word" "$file" | wc -l)

echo "Occurance of $word: $count"
}

count_word file1.txt Linux

#Print line number of the word present
show_line(){
file=$1
word=$2

grep -n "$word" "$file"
}

show_line file1.txt Linux

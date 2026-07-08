#Function to count the ERRORS
count_errors(){
	echo "Number of error messages: "
	grep -c "ERROR" server.log
}

#Function to display WARNING messages
show_warning(){
	echo "WARNING messages: "
	grep "WARNING" server.log
}

#Function to replace ERROR with CRITICAL
replace_error(){
	echo "Replacing ERROR with CRITICAL..."
	sed 's/ERROR/CRITICAL/g' server.log
}

echo "============================"
echo "       Log File Analyzer    "
echo "============================"

count_errors
echo
show_warning
echo
replace_error


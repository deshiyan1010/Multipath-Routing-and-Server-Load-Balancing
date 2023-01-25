while true
do
	sleep $(($(($RANDOM%6))+2))
	curl -X GET http://10.0.0.47:5000/compute
	echo "done"
done

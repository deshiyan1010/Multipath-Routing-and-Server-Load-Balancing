while true
do
	sleep 1
	curl -X GET http://10.0.0.1:5000/usage_stats &
    curl -X GET http://10.0.0.2:5000/usage_stats &
    curl -X GET http://10.0.0.3:5000/usage_stats &
	# curl -X GET http://127.0.0.1:5000/usage_stats &
	# echo "done"
done

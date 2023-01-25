while getopts m:c:h: flag
do
    case "${flag}" in
        m) mem=${OPTARG};;
        c) cpu=${OPTARG};;
        h) host=${OPTARG};;
    esac
done

sudo systemd-run --scope -p MemoryLimit="$mem"M -p CPUQuota="$cpu"% ./run.sh 10.0.0."$host" "$cpu" "$mem"
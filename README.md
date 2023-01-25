
# Multipath routing and server load balancing

This project is a combination of multipath routing (network load balancing) and server load balancing.




## Files
Here the functions of each files/folders are explained.
| File path | Description |
| --- | --- |
| controller.py | Ryu Controller. |
| flask_server.py | Flask app running on few host |
| load_balancer_logic.py | Refreshs server stats and holds logic |
| load_balancer.py | Flask app that does load balancing |
| Makefile | Cleanup previous MiniNet topology |
| MiniNAM.py | Realtime network visualizer |
| rand_req.sh | Queries service from load balancer randomly, every client runs this. |
| run.sh | Runs Falsk server on clients |
| run_server.sh | Runs "run.sh" with memory, CPU constrains. |
| stats.py | Collects stats on the machine it is running on (server). |
| topo_mini.py | Small network for multipath testing. |
| topo_scalar.py | Full scale data center topology. |
| visualizer.py | Visualizing stats collected by load balancer. |

## Demo

Step 1: Open terminal from the folder location. Run the following command.

```
ryu-manager controller.py --observe-links
```

Step 2: Open another terminal and run the command.
```
sudo python topo_scaler.py 
```

Step 3: In the Mininet CLI run the following command to open terminal on each server and on load balancer.
```
xterm h1 & xterm h2 & xterm h3 & xterm h100 & xterm h100 & xterm h10 & xterm h4 & xterm h5
```
Step 4: Execute the following command on ```h1```, ```h2```, ```h3```, ```h4``` and ```h5```. Here resources dedicated are 700 MB is memory constrain and 100% i.e. one core.
```
./run.sh -m 700 -c 100 -h <the host number>
```

Step 5: Run load balancer in ```h100```
```
<path to python executable> load_balancer.py 10.0.0.47
```

Step 6: Launch and run visualizer in ```h100```
```
brave-browser --no-sandbox & <path to python executable> visualizer.py
```

Step 7: When the Brave Browser opens, go to 10.0.0.47:8000
for visuals.
## Demo of multipath routing

Step 1: Run the Mininet file
```
sudo python MiniNAM.py --custom topo_mini.py --topo mytopo --controller remote
```

Step 2: Run Ryu manager.
```
ryu-manager controller.py --observe-links
```
## Prerequisite
-  Brave Browser

-  Installations from requirements.txt
## Screenshots

![Network Visualization](/assets/mini_topo.png)

![Stats Visualizer](/assets/visualizer.png)

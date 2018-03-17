# robot_picon_zero

## Install
* sudo pip install psutil
* sudo apt-get install lm-sensors
    
* sudo cp robot_picon_zero.service /lib/systemd/system/
* sudo systemctl start robot_picon_zero.service
* systemctl status robot_picon_zero.service
* sudo systemctl stop robot_picon_zero.service
* sudo systemctl enable robot_picon_zero.service

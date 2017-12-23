#!/bin/bash
LOC=/sys/class/gpio


setio()
{
PIN=$1
STATE=$2
PINLOC=$LOC/gpio"$1"/value

echo "$STATE" > $PINLOC
    
	if [ "$(cat $PINLOC)" -eq "1" ]; then
	echo "P$PIN is on"
	else
	echo "P$PIN is off"
	fi

}








action="$1"


#gpio [set/get] [pin] [0/1]

case "$action" in
	"set")
	#if the file location exisit
	if [ -d $LOC/gpio"$2" ];
	 then 
	setio $2 $3
  	

	else
 	  echo "$2" > $LOC/export
 	  echo "out" > $LOC/gpio"$2"/direction 
	sleep .1s
	setio $2 $3
	fi
	;;

	"get")
		cat $LOC/gpio"$2"/value
	;;

esac

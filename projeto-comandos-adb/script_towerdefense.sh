#!/bin/zsh
counter=1
total_time=$(date +%s)
for i in {1..1000}
do
    start_time=$(date +%s)
    echo "1 Tela"
    ./adb shell input touchscreen tap 615 327
    sleep 0.5 
    
    echo "2 Quadrado"
    ./adb shell input tap 1169 274
    sleep 0.5 

    echo "3 Arma"
    ./adb shell input tap 999 645
    sleep 0.5 

    echo "4 Quadrado"
    ./adb shell input touchscreen tap 1169 274
    sleep 0.5 

    echo "5 Upgrade"
    ./adb shell input touchscreen tap 1374 672
    sleep 0.5 

    echo "6 Next Wave"
    ./adb shell input touchscreen tap 803 53
    sleep 0.5 

    echo "7 Acelera"
    ./adb shell input touchscreen tap 1319 57
    sleep 11 

    echo "8 Upgrade"
    ./adb shell input touchscreen tap 1374 669
    sleep 0.5 

    echo "9 Next Wave"
    ./adb shell input touchscreen tap 803 53
    sleep 12 

    echo "10 Upgradie"
    ./adb shell input touchscreen tap 1374 669
    sleep 3 

    echo "11 Next Wave"
    ./adb shell input touchscreen tap 803 53
    sleep 12 

    echo "12 Upgrade"
    ./adb shell input touchscreen tap 1374 669
    sleep 3 

    echo "13 Next Wave"
    ./adb shell input touchscreen tap 803 53
    sleep 12 

    echo "14 Upgrade" 
    ./adb shell input touchscreen tap 1374 669
    sleep 0.5 

    echo "15 Next Wave" 
    ./adb shell input touchscreen tap 803 53
    sleep 1 

    echo "16 Increase Power" 
    ./adb shell input touchscreen tap 1475 375
    sleep 2 

    echo "17 Upgrade" 
    ./adb shell input touchscreen tap 1374 669
    sleep 5 


    echo "18 Reload page" 
    ./adb shell input touchscreen tap 701 479
    sleep 3 
      # Echo the count on the terminal
    echo "Loop $counter"

    # Increment the counter
    counter=$((counter + 1))

    end_time=$(date +%s)

    elapsed_time=$((end_time - start_time))
    # total_time=$((total_time + elapsed_time))
    # total_time_seconds=$((total_time / 1000))

    echo "The elapsed time in milliseconds is $elapsed_time"
    # echo "Total time in milliseconds is $total_time"
    # echo "The elapsed time in Seconds is $total_time_seconds"
done

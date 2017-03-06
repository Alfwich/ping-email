printf "Attempts: "
grep "received" nohup.out | wc -l
printf "Good: "
grep "1 received" nohup.out | wc -l
printf "Bad: "
grep "0 received" nohup.out | wc -l

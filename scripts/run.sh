#! /bin/sh

LOG=all-logs.log
EXON=results.txt
EXONOUT=results-sorted.txt

# Fetch the logs.
./fetchlogs.py

# Remove the headers.
sed -i '/^AddressHash/d' $LOG

# Country.
cut -f 12 $LOG | sort | uniq -c | awk '{print $2,$1}' | sort -nrk2,2 | head -10 > country.dat
# ReadyOpenConnection.
cut -f 9 $LOG | sort | uniq -c | grep -v ReadyOpenConnection | awk '{print $2,$1}' > readyopen.dat
# TotalCreateCells.
cut -f 11 $LOG | sort | uniq -c | grep -v TotalRelayCells | awk '{print $2,$1}' > totalrelay.dat
# Time.
cut -f 4 $LOG | sort | uniq -c | grep -v Duration | awk '{print $2,$1}' | head -10 > time.dat

if [ "$#" -lt "1" ]
then
    echo "Running ExoneraTor. This will take some time..."
    # Check IPs for Tor relays.
    ./exonerator.py
fi

# Sort the Exonerator data.
sort $EXON | uniq -c | awk '{print $2}' > $EXONOUT
./checkmalicious.py

# Generate the graphs.
./generategraphs.py

# Cleanup.
rm *.dat
rm $LOG

echo "All done"

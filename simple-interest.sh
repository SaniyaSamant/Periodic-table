#!/bin/bash
# Script to calculate simple interest

echo "Enter Principal Amount:"
read principal
echo "Enter Rate of Interest:"
read rate
echo "Enter Time Period (in years):"
read time

# Calculate Simple Interest
interest=$(echo "$principal * $rate * $time / 100" | bc)
echo "The Simple Interest is: $interest"



echo "Make sure you have the OSINT-SPY already installed and it is residing in your Desktop"
cd ~/Desktop/OSINT-SPY

echo "Running Bitcoin OSINT scanner ... "
echo "Enter the date you would like to search:(Ex: 20210425) "
read btc_date


python3 osint-spy.py --btc_date $btc_date | awk '/Pool_link::/ {print}'| sed 's/Pool_link:://g' | sed 's/https://g' | cut -c 5- | tr -d / | sed 's/tp://g' > collected_urls.txt

sort -u collected_urls.txt > final_urls.txt
# if you have nmap:
nmap -iL final_urls.txt --script whois-ip > nmap_whois_output.txt
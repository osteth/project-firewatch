#set up chron task to pull file every hour
#write out current crontab
crontab -l > mycron
#echo new cron into cron file
echo "0 * * * * ./opt/project-firewatch/projectfirewatch/scripts/getModusFile.sh" >> mycron
#install new cron file
crontab mycron
rm mycron

#!/bin/bash
sudo yum update -y
sudo yum install httpd -y 
sudo systemctl enable httpd
sudo systemctl start httpd
echo "Hunter Hanson - Week 15 Complete" > /var/www/html/index.html
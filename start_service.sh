#!/bin/bash
echo "Hi, $USER!"
#Get RabbitMQ going
echo Now we will start RabbitMQ
sleep 3
sudo service rabbitmq-server restart

#Run Celery
echo lets start Celery now
sleep 6
celery multi start w1 -A __init__.celery worker --loglevel=info --concurrency=1

#Run Gunicorn
echo Lets now start Gunicorn
 sleep 7
sudo gunicorn __init__:app

echo PLEASE OPEN BROWSER TO 127.0.0.1:8000 AND WAIT TILL DATABASE IS FULLY STOCKED

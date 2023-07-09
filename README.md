# Launtel Internet Pause/Unpause Script

This Python script allows you to conveniently pause and unpause your Launtel internet connection. 
It can be useful when you want to temporarily suspend your internet service, such as during vacations or extended 
periods of non-usage, in order to save costs as Launtel charges on a per-day basis.

## Prerequisites

Before using this script, ensure that you have the following prerequisites:

- Python 3.x installed on your system
- The `requests` library installed. If not, you can install it by running the following command:
```
pip install -r requirements.txt
```

## Configuration

Before running the script, you need to configure it with your Launtel account details. The following environment variables need to be set:

- `LAUNTEL_EMAIL`: Your Launtel account email address.
- `LAUNTEL_PASSWORD`: Your Launtel account password.

Make sure to set these environment variables with your actual Launtel account credentials before running the script.

### Pausing the Internet

To pause your Launtel internet connection, run the following command:
```
python launtel.py pause
```

### Unpausing the Internet

To unpause your Launtel internet connection, run the following command:
```
python launtel.py unpause
```

## Usage

I use this script in combination with a Telegram bot and AWS Lambda to schedule internet pauses and unpauses.
By integrating the script with a Telegram bot and configuring AWS Lambda as a webhook, 
you can automate the process of pausing and unpausing your Launtel internet connection. 
One possible approach is to utilize Telegram's scheduled message feature to trigger the desired pause 
or unpause command at the scheduled time. 

Another potential use case for this script is to utilize an EC2 instance and a cron job to execute the script
at a scheduled time.

## Disclaimer:

Please be aware that there can be delays in the turnaround time for pausing or unpausing a service with NBN 
(National Broadband Network). In certain cases, if you schedule a pause request close to midnight,
but it only gets processed by NBN after midnight, Launtel may incur an additional day's charge. 
To ensure fairness to Launtel and minimize any potential additional costs, I recommend scheduling the pausing 
of your service earlier during the day. This allows Launtel sufficient time to complete the pausing process
within the same day. By following this approach, you can support Launtel and contribute to a smoother 
and more cost-effective service experience for all users.
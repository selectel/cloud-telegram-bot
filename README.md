# Cloud Telegram Bot

1. Download this repo as ZIP
2. Unpack
3. Go inside "cloud-telegram-bot-master", select all files and folders inside and archive. 
It will help to avoid python package names limitations.
4. Go to https://my.selectel.ru -> Cloud Platform -> Functions, tap "Create function"
5. Upload ZIP file 
6. Set "Path to the file" to "bot/tele_bot"
7. Set "Function to execute" to "main"
8. Add item to "Environment variables", name it "TOKEN" and insert token of your Telegram bot as value.
9. Click "Save and deploy"
10. Mark "HTTP-request" as public
11. Use URL as Webhook for your bot


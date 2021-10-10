echo "Cloning Repo...."
git clone https://github.com/ZauteKm/auto-filter-bot-v3.git /auto-filter-bot-v3
cd /auto-filter-bot-v3
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py

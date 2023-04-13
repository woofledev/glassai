# Bot will be archived soon
this bot will be discontinued and archived. logs, or older databases will not be published due to user privacy.


# glassai
a dumb ai bot thing on [discord](https://discord.com/users/1081912681998581830)

## setup
you need python (3.10.6 is my version) with pip for this project.

install these dependencies: `pip install discord.py==1.7.0 spacy chatterbot chatterbot-corpus`

you can also follow the chatterbot setup guide [here.](https://chatterbot.readthedocs.io/en/stable/setup.html)

and run this command: `python -m spacy download en_core_web_sm` (or use [any of these models](https://spacy.io/models/en))

### creating a database
create a python file named anything and paste this inside it
```py
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.response_selection import get_most_frequent_response

bot = ChatBot('GlassAI')
bot.response_selection_method = get_most_frequent_response
trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.english')
```
this should create a `db.sqlite` file with about 200KB~

### running the bot
if you didn't already, write your bot token inside the `token.txt` file.

after that, you can simply run bot.py and voila! the bot should be running.

### troubleshooting
if you got any error related to chatterbot, you might need to change the way it uses spaCy to load the model.

[heres a great stackoverflow article explaining how to fix this](https://stackoverflow.com/questions/66087475/chatterbot-error-oserror-e941-cant-find-model-en) (just edit line 13 in the tagging.py file)

you might need to replace the model with the actual model you're using, in this case, en_core_web_sm if you followed everything

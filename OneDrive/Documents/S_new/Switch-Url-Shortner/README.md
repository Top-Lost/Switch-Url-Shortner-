# URL Shortner Bot
A Switch Bot written in Python which offers to shorten urls's with different shortners

## Supported Sites
- [GPlinks](https://gplinks.in/)
- [ATG Links](https://atglinks.com/)
- [Share Us](https://publisher.shareus.io/)
- [Gyani Links](https://gyanilinks.com/)

*More Websites adding soon*

# How to Deploy?

## Prerequisites
- Python 3.0 or greater

### Installing Requirements
- Clone this repo:

```
git clone https://github.com/Top-Lost/Switch-Url-Shortner urlshortner/ && cd urlshortner
```

- Install dependencies for running setup scripts:
```
pip3 install -r requirements.txt
```

### Run the bot
- Rename sample_config.env to config.env


```
python -m bot.py
```
### Setting config file
**1. Required Fields**

- `BOT_TOKEN`: The Switch Bot Token.
- `DATABASE_URL`: Database url from [MongoDB](https://mongodb.com)
- `DATABASE_NAME`: Database name from [MongoDB](https://mongodb.com). Default will be Cluster0

**2. Optional Field**
- `ADMINS`: User ids of admins seperated by space.
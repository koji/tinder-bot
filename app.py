import tinder_bot

def main():
  bot = tinder_bot.TinderBot()
  two_fa = True
  bot.login(two_fa)
  debug = True
  bot.auto_swipe(debug)



if __name__ == "__main__":
    main()



# Dicey

Dicey is a tiny [Diceware](http://world.std.com/~reinhold/diceware.html) password generator written in Python 3. It's a little different from other Diceware password generators because it can pick and choose from different word lists in easily editable plain text files. Dicey can't guarantee security, but it can help generate [strong passwords](https://xkcd.com/936/)!

## Usage

Simply run

    python3 dicey.py
    >deceiving unfixable rouse durably anglo

You can also specify a number of words

    python3 dicey.py 10
    >handpick glory tooth holt shamrock five tinsmith culpa nop tactful

## More usage

Words are pulled from the .txt files in the `wordlists/` directory which share the same line-by-line format `11111\tword\n`. This repo contains the [EFF long wordlist](https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases) and a slightly reformatted [Reinhold Diceware list](http://world.std.com/~reinhold/diceware.html).

## License

This tiny project is licensed until the [MIT License](https://opensource.org/licenses/MIT).
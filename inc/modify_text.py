# Modifies the text on the page. Adds a trademark for all 6-letter words

import string
import re


def modify_text(page):
    text_tags = page.find_all(string=True)

    for single in text_tags:
        changed = False
        words = single.split()

        for i, word in enumerate(words):
            if len(re.sub(r'\W', '', word)) == 6:
                words[i] += u"\u2122"
                changed = True

        if changed:
            single = single.replace_with(" ".join(words))

    return page

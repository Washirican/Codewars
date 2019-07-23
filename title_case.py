def title_case(title, minor_words=""):

    # print("Ogirinal Title:", title)
    # print("Exceptions Words:", minor_words.lower(), "\n")

    title = title.capitalize().split()
    minor_words = minor_words.lower().split()

    print(" ".join([word.title() if word not in minor_words else word for word in title]))


title_case('a clash of KINGS', 'a an the of')
title_case('THE WIND IN THE WILLOWS', 'The In')
title_case('the quick brown fox')
title_case('First a of in', 'an often into')

# Description: This file contains all the constants used in the project.

# emoji_dict is a dictionary that maps the emoji to the corresponding text
emoji_dict = {
    ':)': '😊',
    ':(': '😔',
    ':D': '😃',
    ':p': '😛',
    ':P': '😛',
    ':o': '😮',
    ':O': '😮',
    ';)': '😉',
    ':|': '😐',
    ':*': '😘',
    '<3': '❤️',
    ':/': '😕'
}

# emoji_list is a list of all the emojis
emoji_list = list(emoji_dict.values())


# Packet size in bytes
PACKET_SIZE = 1024 

# Timeout in seconds
TIMEOUT = 1000000
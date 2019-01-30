# PYGROUPME VER 0.0.3

Simple python wrapper for the GroupMe API that allows users to interface with Microsoft's GroupMe messaging platform via the requests module. I created this after realizing that there is no existing wrapper for the API in python, and typing the code necessary to interface with GroupMe repeatedly in code is exhausting. In order to interact with GroupMe, users first need to have a GroupMe account and a designated GroupMe group, then register a bot at https://dev.groupme.com/session/new and provide the program with its bot id to send messages and/or the token code to receive messages.  


Example usage:
    
    import pygroupme as pgm
    
    pgm.gm_msg(bid=BOT_ID_HERE, text="Hello, world!") # sends "Hello, world!" to the GroupMe chat in which the user has set up his GroupME api interface
    message = pgm.gm_rec(token=USER_TOKEN_HERE, gid=USER_GID_HERE, limt=n) # receive the last n messages from a GroupMe chat, default is 1
    
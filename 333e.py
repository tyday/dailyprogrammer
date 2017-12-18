#https://www.reddit.com/r/dailyprogrammer/comments/72ivih/20170926_challenge_333_easy_packet_assembler/
# Each line of input represents a single packet. Each line will be formatted as X Y Z some_text, 
# where X Y and Z are positive integer and some_text is an arbitrary string. X represents the message ID 
# (ie which message this packet is a part of). Y represents the packet ID (ie the index of this packet in the message) 
# (packets are zero-indexed, so the first packet in a message will have Y=0, the last packet in a message will have Y=Z-1). 
# Z represents the total number of packets in the message. 
# It is guaranteed that there will be no duplicate packets or message IDs.

# for each packet in incoming_packets
#
# evaluate packet
# evaluate packet will:
# 1 convert string into list consisting of x,y,z and text
# 2 evaluate to see if string is in message buffer
#   then add it to buffer if necessary
# 3 evaluate message buffer to see if any messages are complete
# 4 print out complete messages
# 5 clear complete messages from the message buffer

def evaluate_packet(packet):
    """Returns a packet as a list item
    """
    message = packet.split(maxsplit=3)
    if len(message) <4:
        message.append('\n')
    contents = {'z':message[2],message[1] : message[3]}
    title = message[0]
    return title,contents 

def add_packet_to_buffer(buffer,title,contents):
    if title not in buffer:
        newmessage = {title:contents}
        buffer.update(newmessage)
    elif title in buffer:
        message_buffer[title].update(contents)
def compile_print(buffer,title):
    garbled_message = message_buffer[title]
    complete_message = []
    str_complete_message =""
    for i in sorted(garbled_message.keys()):
        if i != 'z':
            j = int(i)
            # print(garbled_message[i])
            complete_message.insert(j,garbled_message[i])
    for i in complete_message:
        str_complete_message += i
    return(str_complete_message)

message_buffer = {}

for line in open("333e_c.txt"):
    title,contents = evaluate_packet(line)
    add_packet_to_buffer(message_buffer, title, contents)
    length = len(message_buffer[title])-1
    if int(contents['z']) == length:
        print(compile_print(message_buffer,title))

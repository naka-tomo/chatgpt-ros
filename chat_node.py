import rospy
from std_msgs.msg import String
from chat_gpt import ChatGPT


def main():
    rospy.init_node("chat_gpt")
    pub_synthesis = rospy.Publisher("google_speech/utterance", String, queue_size=10)

    apikey = open("apikey.txt").readline()
    personality_texts = ["あなたは猫です", "語尾に「にゃー」をつけて可愛くしゃべりなさい"]

    chat = ChatGPT(apikey, personality_texts)

    while not rospy.is_shutdown():
        msg = rospy.wait_for_message("/google_speech/recres", String)
        print(msg.data)

        res = chat.request_responce(msg.data)

        print(res)
        pub_synthesis.publish(res)


if __name__ == "__main__":
    main()

import rospy
from std_msgs.msg import String
from chat_gpt import ChatGPT
import time


def main():
    rospy.init_node("chat_gpt")
    pub_synthesis = rospy.Publisher("jtalk/utterance", String, queue_size=10)

    apikey = open("apikey.txt").readline()
    personality_texts = ["あなたは猫のキャラクターです", "語尾に「にゃー」をつけて可愛くしゃべりながら子供たちと楽しいおしゃべりをしてください"]
    chat = ChatGPT(apikey, personality_texts)

    while not rospy.is_shutdown():
        msg = rospy.wait_for_message("/google_speech/recres", String)
        print(msg.data)

        res = chat.request_responce(msg.data)

        print(res)
        pub_synthesis.publish(res)

        time.sleep(1)
        rospy.wait_for_message("/google_speech/recres", String)


if __name__ == "__main__":
    main()

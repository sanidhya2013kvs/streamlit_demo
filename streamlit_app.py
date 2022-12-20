import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2
from cvzone.HandTrackingModule import HandDetector
import cv2

detector = HandDetector(detectionCon=0.8, maxHands=2)

st.title("HAND DETECTION")
st.write("PLEASE CLICK ON START BUTTON  TO START")

class VideoProcessor:
    def recv(self, frame):
      img = frame.to_ndarray(format="bgr24")
      
    # Find the hand and its landmarks
      hands, img = detector.findHands(img)  # with draw
    # hands = detector.findHands(img, draw=False)  # without draw

      if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmark points
        bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
        centerPoint1 = hand1['center']  # center of the hand cx,cy
        handType1 = hand1["type"]  # Handtype Left or Right

        fingers1 = detector.fingersUp(hand1)
        
        if len(hands) == 2:
            # Hand 2
            hand2 = hands[1]
            lmList2 = hand2["lmList"]  # List of 21 Landmark points
            bbox2 = hand2["bbox"]  # Bounding box info x,y,w,h
            centerPoint2 = hand2['center']  # center of the hand cx,cy
            handType2 = hand2["type"]  # Hand Type "Left" or "Right"

            fingers2 = detector.fingersUp(hand2)
      


      return av.VideoFrame.from_ndarray(img, format="bgr24")




    

 


ctx=webrtc_streamer(
    key="example",
    video_processor_factory=VideoProcessor,
    rtc_configuration={  
        "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
    }
)



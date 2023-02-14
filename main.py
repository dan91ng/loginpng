import cv2, time
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) # 打开摄像头
 

filename = str(int(time.time()))+'.png'

print(time.time())
while (1):
  # get a frame
  ret, frame = cap.read()
  frame = cv2.flip(frame, 1) # 摄像头是和人对立的，将图像左右调换回来正常显示
  # show a frame
  #cv2.imshow("capture", frame) # 生成摄像头窗口
 
  #if cv2.waitKey(1) & 0xFF == ord('q'): # 如果按下q 就截图保存并退出
  #filename = 
  cv2.imwrite("D:\\code\\python\\video\\"+filename, frame) # 保存路径
  break
    #break
 
cap.release()
cv2.destroyAllWindows()
import subprocess
import time
import cv2
from colorama import Fore,Style

"""                                                                            تعريف الاجهزه """
dv1="MB28692365452100265"
dv2 =""
dv3=""

"""                                               دالة التقاط الشاشه و عند استدعائها تحتاج الى اسم صوره فقط و لا تنسى علامة التنصيص """

def capture_remov(filename="screenshot.png"):
    import os
    try:
        # التقاط السكرينشوت وحفظه في ذاكرة الهاتف
        subprocess.run(["adb", "shell", "screencap", "-p", "/sdcard/screenshot.png"], check=True)

        # نقل السكرينشوت من الهاتف إلى الكمبيوتر
        subprocess.run(["adb", "pull", "/sdcard/screenshot.png", filename], check=True)

        print(Fore.GREEN+"SEVE IMG"+Style.RESET_ALL)
        ttime(2)  



    except subprocess.CalledProcessError as e:
        print("حدث خطأ أثناء التقاط السكرينشوت:", e)
    

# تنفيذ العملية
#capture_screenshot("screenshot.png")


""" دالة النقر على الشاشه و تخاذ قيمة اكس و واي مع دالة الوقت و تاخذ وقت فقط """

def apt(x,y):
    subprocess.run(["adb","-s",dv1,"shell","input","tap",str(x),str(y)]) #and subprocess.run(["adb","-s",dv2,"shell","input","tap",str(xx),str(yy)])
    ttime(2)
def ttime(t):
    time.sleep(t)
def remov():
    import os

    # تحديد مسار الصورة (إذا كانت في نفس المجلد، يكفي اسم الملف فقط)
    image_path = "/home/rico/Desktop/Tiktok/screenshot.png"
    ttime(1)

    # التحقق من وجود الملف ثم حذفه
    if os.path.exists(image_path):
        os.remove(image_path)
        print(Fore.GREEN+"REMOV"+Style.RESET_ALL)
        ttime(2)
    else:
        print("الصورة غير موجودة.")     
"""                                                 دالة اغلاق التطبيق """

def closing():
    # معرف حزمة التطبيق
    package_name = "com.tikfamous.tik.tok.followers.likes.tikfans.reports.free.app"

    # إغلاق التطبيق بالقوة
    subprocess.run(["adb", "shell", "am", "force-stop", package_name])

    print(f"تم إغلاق التطبيق: {package_name}")  
    
    ttime(1)
    apt(98,227)
    ttime(3)
    

"""الان المشروع """

while   True:
    capture_remov("screenshot.png")
    
    original_image = cv2.imread("screenshot.png", cv2.IMREAD_GRAYSCALE)  # صورة الشاشة الكاملة
    icon_heart = cv2.imread("like.png", cv2.IMREAD_GRAYSCALE)  # صورة أيقونة القلب ❤️ فقط
    icon_person = cv2.imread("follow.png", cv2.IMREAD_GRAYSCALE)  # صورة أيقونة الشخص 👤 فقط
    icon_comnt = cv2.imread("comnt.png", cv2.IMREAD_GRAYSCALE)  #صورة التعليق
    ########################################الكود الي فوق مجرد ياحذ صوره و ينقلها مع تعريف كل من لايك و الفولو و التعليق 
    if original_image is None or icon_heart is None or icon_person is None :  #تاكد من تحميل صوره الاصليه 
        print("خطأ: تعذر تحميل الصور! تأكد من المسارات.")
        exit()
    # استخدام Canny Edge Detection لاستخراج الحواف
    edges_original = cv2.Canny(original_image, 50, 150)
   
    edges_heart = cv2.Canny(icon_heart, 50, 150)
    
    edges_person = cv2.Canny(icon_person, 50, 150)
    
    edges_comnt = cv2.Canny(icon_comnt, 50, 150)    

    ############################################(1)
    # استخدام Template Matching للبحث عن أيقونة القلب
    
    result_heart = cv2.matchTemplate(edges_original, edges_heart, cv2.TM_CCOEFF_NORMED)
    _, max_val_heart, _, max_loc_heart = cv2.minMaxLoc(result_heart)
    


    ###############################################(2)
    # استخدام Template Matching للبحث عن أيقونة الشخص
    
    result_person = cv2.matchTemplate(edges_original, edges_person, cv2.TM_CCOEFF_NORMED)
    _, max_val_person, _, max_loc_person = cv2.minMaxLoc(result_person) 
    
    ###############################################(3)
    #للبحث عن تعليق 
    result_comnt = cv2.matchTemplate(edges_original, edges_comnt, cv2.TM_CCOEFF_NORMED)
    _, max_val_comnt, _, max_loc_comnt = cv2.minMaxLoc(result_comnt)
   
    """العتله """
    
    threshold = 0.9  # يمكن تعديلها حسب الحاجة

    detected = False
    result_image = cv2.imread("screenshot.png")  # إعادة تحميل الصورة الملونة للرسم عليها

    

    #######################################################(        LIKE          )#####################################################################################
    if max_val_heart >= threshold:
        apt(143,848)
        ttime(5)
        apt(56,869)
        ttime(1)
        apt(353,1562)
        ttime(0.5)
        apt(98,213)
        ttime(5)
        


        print(Fore.RED+"DONE LIKE"+Style.RESET_ALL)
        remov()

        #top_left = max_loc_heart
        #h, w = icon_heart.shape
        #bottom_right = (top_left[0] + w, top_left[1] + h)
        #cv2.rectangle(result_image, top_left, bottom_right, (0, 255, 0), 3)
        detected = True

        
        

#######################################################(        FOLOOW          )######################################################################################
    if max_val_person >= threshold:
        apt(143,848)
        ttime(5)
        apt(413,631)
        ttime(0.5)
        apt(353,1562)
        ttime(0.5)
        apt(99,213)
        ttime(5)
        
        
        print(Fore.BLUE+" DONE FOLLOW"+Style.RESET_ALL)
        remov()


    

        detected = True
        
#######################################################(        COMENT          )######################################################################################

    if max_val_comnt >= threshold:
        apt(143,848)
        ttime(5)
        apt(56,982)
        ttime(0.5)
        apt(652,1347)
        ttime(0.5)
        apt(95,1458)
        ttime(0.5)
        apt(335,1562)
        ttime(0.5)
        apt(99,213)
        ttime(5)
        

        print(Fore.YELLOW+"DONE COMENT"+Style.RESET_ALL)
        remov()
        #top_left = max_loc_comnt
        #h, w = icon_comnt.shape
        #bottom_right = (top_left[0] + w, top_left[1] + h)
        #cv2.rectangle(result_image, top_left, bottom_right, (255, 0, 0), 3)

        detected = True
        
    ################
    # عرض الصورة مع التحديدات
    #if detected:
        #cv2.imshow("Detected Icons", result_image)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
    else:
        print("لم يتم العثور على أيقونة القلب أو الشخص.")
        
        


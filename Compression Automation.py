import pyautogui
import pyperclip
import time

directory = 'C:\\Users\\adelgado\\Desktop\\Devhack\\Khan Academy\\Videos'
compDirectory = 'C:\\Users\\adelgado\\Desktop\\Devhack\\Khan Academy\\Compressed\\'

videos = 'basic_division.mp4', 'division_1.mp4', 'division_application.mp4', 'division_dos_digitos.mp4',
'division_example_4.mp4', 'division_remainder.mp4', 'partial_division.mp4', 'partial_division_2.mp4'



def compressVideo(videoName):
    # fileOpen
    pyautogui.click(867, 273)

    # fileName # Change to directory
    pyautogui.click(1217, 412)

    # paste in new directory name
    pyperclip.copy(directory)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('enter')

    # videoName

    # enterVideoName
    pyautogui.click(929, 878)
    pyperclip.copy(videoName)
    pyautogui.hotkey("ctrl", 'v')

    # openFile
    pyautogui.click(1409, 914)

    # gives the video time to load
    time.sleep(1)

    # Location to Save
    pyperclip.copy(compDirectory + 'compressed_' + videoName)

    # get to save as
    pyautogui.click(790, 956)

    # goes to previous text
    pyautogui.hotkey("ctrl", 'a')

    # deletes
    pyautogui.hotkey('delete')

    # paste in Save As
    pyautogui.hotkey("ctrl", 'v')

    # Start Encode
    pyautogui.click(1084, 91)


for i in videos:
    compressVideo(i)
    endTime = time.time() + 35
    while time.time() < endTime:
        doNothing = 0
    pyautogui.click(764, 86)




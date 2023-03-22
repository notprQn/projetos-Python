import cv2
import curses

stdscr = curses.initscr()

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

WIDTH = 100
HEIGHT = 60



cap = cv2.VideoCapture(r"c:\Users\j1p2r\Desktop\Coisas\ascii\video\videoplayback.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    grayScale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    tamanhoVideo = cv2.resize(grayScale, (WIDTH, HEIGHT))

    ascii_chars = []
    for row in tamanhoVideo:
        row_chars = []
        for pixel in row:
            index = int(pixel / 25.5)
            row_chars.append(ASCII_CHARS[index])
        ascii_chars.append("".join(row_chars))

    ascii_art = "\n".join(ascii_chars)

    stdscr.move(0, 0)
    stdscr.clear()
    try:
        stdscr.addstr(ascii_art)
    except curses.error:
        pass
    stdscr.refresh()

    cv2.imshow("ASCII Art", tamanhoVideo)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

curses.endwin()
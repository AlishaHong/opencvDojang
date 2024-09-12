import cv2

img = cv2.imread('data/lena.jpg', cv2.IMREAD_GRAYSCALE)
rects = cv2.selectROIs('img', img, False, True)
print('rects : ', rects)    #여러개 찍을 수 있음 하나찍고 스페이스바 그리고 또하나찍고 스페이스바 
# 리스트 형태로 반환 

# for문 돌리기
# 선택된 부분의 좌표를 리스트로 담자 
rois  = []
for r in rects: 
    cv2.rectangle(img, (r[0], r[1]), (r[0]+r[2], r[1]+r[3]), 255)
    roi = img[r[1]:r[1] + r[3], r[0]: r[0]+r[2]]
    rois.append(roi)
    
    for roi in rois:
        cv2.imshow(f'img{len(rois)}', roi)
        cv2.waitKey()

# cv2.imshow('img', img)
# cv2.waitKey()
cv2.destroyAllWindows()


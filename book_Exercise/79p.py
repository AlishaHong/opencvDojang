import cv2

src = cv2.imread('data/lena.jpg')

# 3색 분리
dst = cv2.split(src)
# print(dst)
print(type(dst))    #튜플
print(type(dst[0])) #넘파이어레이


cv2.imshow('src', src)
cv2.imshow('blue', dst[0])
cv2.imshow('green', dst[1])
cv2.imshow('red', dst[2])


# 다시 병합하기 
dst2 = cv2.merge(dst)

cv2.imshow('dst2', dst2)

cv2.waitKey()
cv2.destroyAllWindows()
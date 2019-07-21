# from pyimagesearch.transform import four_point_transform
import cv2
import imutils
from skimage.filters import threshold_local


#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required = True,
#	help = "Path to the image to be scanned")
#args = vars(ap.parse_args())


#scanner object initiated when the service is requested
#think of multiple bills.
#intitiates when asked to add a bill
class Scanner():
    def getImage(self):
        #UI - ask if needs to be scanned or imported
        # assert the option buttons to define the path or send 0 for camera:
        #make sure to return the image object from the path.
        path = ""
        print("fetching image")
        if path != None:
            return None
        else:
            #write logic to open camera and click and image
            return None

    def prepImage(self, image):
        ratio = image.shape[0] / 500.0
        orig = image.copy()
        image = imutils.resize(image, height=500)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        edged = cv2.Canny(gray, 75, 200)
        cv2.imshow("Image", image)
        cv2.imshow("Edged", edged)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST,
                                cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]

        for c in cnts:
            # approximate the contour
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)

            if len(approx) == 4:
                screenCnt = approx
                break

        cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
        cv2.imshow("Outline", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # warped = four_point_transform(orig, screenCnt.reshape(4, 2) * ratio)
        warped = None
        warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
        T = threshold_local(warped, 11, offset=10, method="gaussian")
        warped = (warped > T).astype("uint8") * 255

        cv2.imshow("Original", imutils.resize(orig, height=650))
        cv2.imshow("Scanned", imutils.resize(warped, height=650))
        cv2.waitKey(0)

        return 0


test = Scanner()
test.getImage()

## Macbook Pro
This file will record my steps of configuring my *Macbook Pro*

### Macdown syntax example
1. Order_list 1: *aaa* **bold**  ==high light== `inline code` <!--this is comment line!-->

* Unordered list 1 and inline math equations: $x = y$
* Unordered list 2

> aws  
> fei

[Baidu link](www.baidu.com)

> This is a picture
<!--![pic1](/Users/jarvis/Research/picture/WechatIMG7.jpeg)-->

$$x = y$$

<!--This is a table-->
|feeeeee  | ewww |ef|
|---------|-------|----|
efe.   |fe|eef|


First Header  | Second Header
------------- | -------------
ell  | Content Cell
Content Cell  | Content Cell

---
### Compile OpenCV 3.4 for Anaconda Python 3.7, 3.6, 3.5, 3.4 and 2.7 
> Reference pages [Compile OpenCV](https://www.scivision.co/anaconda-python-opencv3/)  
> Need a ***ladder***

#### Install Prerequest dependency
```bash
brew install git cmake pkg-config jpeg libpng libtiff openexr eigen tbb
```
#### Build OpenCV for Python and C++
[Download](https://github.com/opencv/opencv/releases) the latest OpenCV **Souce Code** ZIP file, then do the following orders.

```bash
unzip 3*.zip
cd opencv*

mkdir release
cd release

cmake -DBUILD_TIFF=ON -DBUILD_opencv_java=OFF -DWITH_CUDA=OFF -DWITH_OPENGL=ON -DWITH_OPENCL=ON -DWITH_IPP=ON -DWITH_TBB=ON -DWITH_EIGEN=ON -DWITH_V4L=ON -DWITH_VTK=OFF -DBUILD_TESTS=OFF -DBUILD_PERF_TESTS=OFF -DCMAKE_BUILD_TYPE=RELEASE ..

make -j -l 2
make install  # not sudo, except for Raspberry Pi

```

**Note:** especially for embedded systems like the Raspberry Pi, consider make -j -l 2 to avoid over-temperature and under-voltage warnings (in general when compiling on Raspberry Pi, not just for OpenCV).

#### Fix the error
> **ModuleNotFoundError**: No module named ‘cv2’  

Ensure that desired Python `site-packages` found with

```bash
python -c "import sys; print(next(p for p in sys.path if 'site-packages' in p))"
```

contains: ***cv2.\*.so***, 
The ***cv2.\*.so*** is found in `/usr/local/lib/python3.7/site-packages/cv2.cpython-37m-darwin.so`, then link it to the **Anaconda python site-package path**, so as

```bash
ln -s /usr/local/lib/python3.7/site-packages/cv2.cpython-37m-darwin.so /Users/jarvis/anaconda3/lib/python3.6/site-packages/cv2.so
```

#### Test for C++ and Python
**The C++ source code:**

```c++
#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

int main()
{
    Mat srcImage = imread("./WechatIMG7.jpeg");
    imshow("源图像",srcImage);

    waitKey(0);

    return 0;
}
```

The `CMakeLists.txt` is:

```c++
cmake_minimum_required(VERSION 2.8)
project(opencvtest)
find_package(OpenCV REQUIRED)
add_executable(opencvtest opencvtest.cpp)
target_link_libraries(opencvtest ${OpenCV_LIBS})
```

Then use `cmake` to build and run the source code, or use the `g++`

```bash
# cmake
cmake .
make
./opencvtest
# or g++
g++ `pkg-config opencv --cflags` test.cpp  -o opencv `pkg-config opencv --libs`
```

**The python code:**

```python
import cv2
print(cv2.__version__) % echo `3.4.2`
```

### Another way to install OpenCV 3 for Python on Mac
> [Reference](https://www.codingforentrepreneurs.com/blog/install-opencv-3-for-python-on-mac/)
> Ever follow it to install, but not work. 

Install OpenCV3 for Python using **Homebrew**

```bash
brew install opencv3 --with-contrib --with-python3
# Add the cv2.*.so file to the Anaconda python site-packeges
ln -s /usr/local/Cellar/opencv/3.4.2/lib/python3.7/site-packages/cv2.cpython-37m-darwin.so /Users/jarvis/anaconda3/lib/python3.6/site-packages/cv2.so
```
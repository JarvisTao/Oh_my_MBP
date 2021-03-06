1. opencv cmake result, the configuration

	```bash
	General configuration for OpenCV 3.4.2 =====================================
	--   Version control:               unknown
	--
	--   Platform:
	--     Timestamp:                   2018-08-14T12:25:16Z
	--     Host:                        Darwin 17.5.0 x86_64
	--     CMake:                       3.12.0
	--     CMake generator:             Unix Makefiles
	--     CMake build tool:            /usr/bin/make
	--     Configuration:               RELEASE
	--
	--   CPU/HW features:
	--     Baseline:                    SSE SSE2 SSE3 SSSE3 SSE4_1
	--       requested:                 DETECT
	--     Dispatched code generation:  SSE4_2 FP16 AVX AVX2 AVX512_SKX
	--       requested:                 SSE4_1 SSE4_2 AVX FP16 AVX2 AVX512_SKX
	--       SSE4_2 (1 files):          + POPCNT SSE4_2
	--       FP16 (1 files):            + POPCNT SSE4_2 FP16 AVX
	--       AVX (5 files):             + POPCNT SSE4_2 AVX
	--       AVX2 (9 files):            + POPCNT SSE4_2 FP16 FMA3 AVX AVX2
	--       AVX512_SKX (1 files):      + POPCNT SSE4_2 FP16 FMA3 AVX AVX2 AVX_512F AVX512_SKX
	--
	--   C/C++:
	--     Built as dynamic libs?:      YES
	--     C++ Compiler:                /Library/Developer/CommandLineTools/usr/bin/c++  (ver 9.1.0.9020039)
	--     C++ flags (Release):         -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Winit-self -Wno-narrowing -Wno-delete-non-virtual-dtor -Wno-unnamed-type-template-args -Wno-comment -fdiagnostics-show-option -Wno-long-long -Qunused-arguments -Wno-semicolon-before-method-body -ffunction-sections -fdata-sections  -msse -msse2 -msse3 -mssse3 -msse4.1 -fvisibility=hidden -fvisibility-inlines-hidden -O3 -DNDEBUG  -DNDEBUG
	--     C++ flags (Debug):           -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Winit-self -Wno-narrowing -Wno-delete-non-virtual-dtor -Wno-unnamed-type-template-args -Wno-comment -fdiagnostics-show-option -Wno-long-long -Qunused-arguments -Wno-semicolon-before-method-body -ffunction-sections -fdata-sections  -msse -msse2 -msse3 -mssse3 -msse4.1 -fvisibility=hidden -fvisibility-inlines-hidden -g  -O0 -DDEBUG -D_DEBUG
	--     C Compiler:                  /Library/Developer/CommandLineTools/usr/bin/cc
	--     C flags (Release):           -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Winit-self -Wno-narrowing -Wno-delete-non-virtual-dtor -Wno-unnamed-type-template-args -Wno-comment -fdiagnostics-show-option -Wno-long-long -Qunused-arguments -Wno-semicolon-before-method-body -ffunction-sections -fdata-sections  -msse -msse2 -msse3 -mssse3 -msse4.1 -fvisibility=hidden -fvisibility-inlines-hidden -O3 -DNDEBUG  -DNDEBUG
	--     C flags (Debug):             -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Winit-self -Wno-narrowing -Wno-delete-non-virtual-dtor -Wno-unnamed-type-template-args -Wno-comment -fdiagnostics-show-option -Wno-long-long -Qunused-arguments -Wno-semicolon-before-method-body -ffunction-sections -fdata-sections  -msse -msse2 -msse3 -mssse3 -msse4.1 -fvisibility=hidden -fvisibility-inlines-hidden -g  -O0 -DDEBUG -D_DEBUG
	--     Linker flags (Release):
	--     Linker flags (Debug):
	--     ccache:                      NO
	--     Precompiled headers:         NO
	--     Extra dependencies:
	--     3rdparty dependencies:
	--
	--   OpenCV modules:
	--     To be built:                 calib3d core dnn features2d flann highgui imgcodecs imgproc java_bindings_generator ml objdetect photo python_bindings_generator shape stitching superres video videoio videostab
	--     Disabled:                    js world
	--     Disabled by dependency:      -
	--     Unavailable:                 cudaarithm cudabgsegm cudacodec cudafeatures2d cudafilters cudaimgproc cudalegacy cudaobjdetect cudaoptflow cudastereo cudawarping cudev java python2 python3 ts viz
	--     Applications:                apps
	--     Documentation:               NO
	--     Non-free algorithms:         NO
	--
	--   GUI:
	--     Cocoa:                       YES
	--     OpenGL support:              NO
	--
	--   Media I/O:
	--     ZLib:                        build (ver 1.2.11)
	--     JPEG:                        build-libjpeg-turbo (ver 1.5.3-62)
	--     WEBP:                        build (ver encoder: 0x020e)
	--     PNG:                         build (ver 1.6.34)
	--     TIFF:                        build (ver 42 - 4.0.9)
	--     JPEG 2000:                   build (ver 1.900.1)
	--     OpenEXR:                     build (ver 1.7.1)
	--     HDR:                         YES
	--     SUNRASTER:                   YES
	--     PXM:                         YES
	--
	--   Video I/O:
	--     DC1394:                      NO
	--     FFMPEG:                      YES
	--       avcodec:                   YES (ver 58.18.100)
	--       avformat:                  YES (ver 58.12.100)
	--       avutil:                    YES (ver 56.14.100)
	--       swscale:                   YES (ver 5.1.100)
	--       avresample:                YES (ver 4.0.0)
	--     GStreamer:                   NO
	--     AVFoundation:                YES
	--     gPhoto2:                     NO
	--
	--   Parallel framework:            TBB (ver 2018.0 interface 10005)
	--
	--   Trace:                         YES (with Intel ITT)
	--
	--   Other third-party libraries:
	--     Intel IPP:                   2017.0.3 [2017.0.3]
	--            at:                   /Users/jarvis/Downloads/opencv-3.4.2/release/3rdparty/ippicv/ippicv_mac
	--     Intel IPP IW:                sources (2017.0.3)
	--               at:                /Users/jarvis/Downloads/opencv-3.4.2/release/3rdparty/ippicv/ippiw_mac
	--     Lapack:                      YES (/System/Library/Frameworks/Accelerate.framework /System/Library/Frameworks/Accelerate.framework)
	--     Eigen:                       YES (ver 3.3.5)
	--     Custom HAL:                  NO
	--     Protobuf:                    build (3.5.1)
	--
	--   OpenCL:                        YES (no extra features)
	--     Include path:                NO
	--     Link libraries:              -framework OpenCL
	--
	--   Python (for build):            /usr/local/bin/python2.7
	--
	--   Java:
	--     ant:                         NO
	--     JNI:                         /System/Library/Frameworks/JavaVM.framework/Headers /System/Library/Frameworks/JavaVM.framework/Headers /System/Library/Frameworks/JavaVM.framework/Headers
	--     Java wrappers:               NO
	--     Java tests:                  NO
	--
	--   Matlab:                        YES
	--     mex:                         /Applications/MATLAB_R2017b.app/bin/mex
	--     Compiler/generator:          Not working (bindings will not be generated)
	--
	--   Install to:                    /usr/local
	-- -----------------------------------------------------------------
	--
	-- Configuring done
	-- Generating done
	-- Build files have been written to: /Users/jarvis/Downloads/opencv-3.4.2/release
	```
	
2. opencv make install result

	```bash
	[  0%] Built target gen-pkgconfig
	[  2%] Built target zlib
	[  8%] Built target libjpeg-turbo
	[ 13%] Built target libtiff
	[ 25%] Built target libwebp
	[ 29%] Built target libjasper
	[ 31%] Built target libpng
	[ 39%] Built target IlmImf
	[ 42%] Built target ippiw
	[ 50%] Built target libprotobuf
	[ 51%] Built target ittnotify
	[ 60%] Built target opencv_core
	[ 60%] Built target opencv_flann
	[ 67%] Built target opencv_imgproc
	[ 69%] Built target opencv_ml
	[ 70%] Built target opencv_objdetect
	[ 72%] Built target opencv_photo
	[ 73%] Built target opencv_video
	[ 80%] Built target opencv_dnn
	[ 83%] Built target opencv_imgcodecs
	[ 83%] Built target opencv_shape
	[ 84%] Built target opencv_videoio
	[ 84%] Built target opencv_highgui
	[ 85%] Built target opencv_superres
	[ 88%] Built target opencv_features2d
	[ 91%] Built target opencv_calib3d
	[ 93%] Built target opencv_stitching
	[ 95%] Built target opencv_videostab
	[ 97%] Built target opencv_traincascade
	[ 98%] Built target opencv_createsamples
	[ 99%] Built target opencv_annotation
	[ 99%] Built target opencv_visualisation
	[100%] Built target opencv_interactive-calibration
	[100%] Built target opencv_version
	Install the project...
	-- Install configuration: "RELEASE"
	-- Installing: /usr/local/share/OpenCV/licenses/ippicv-readme.htm
	-- Installing: /usr/local/share/OpenCV/licenses/ippicv-ippEULA.txt
	-- Installing: /usr/local/share/OpenCV/licenses/ippiw-EULA.txt
	-- Installing: /usr/local/share/OpenCV/licenses/ippiw-redist.txt
	-- Installing: /usr/local/share/OpenCV/licenses/ippiw-support.txt
	-- Installing: /usr/local/share/OpenCV/licenses/ippiw-third-party-programs.txt
	-- Installing: /usr/local/include/opencv2/cvconfig.h
	-- Installing: /usr/local/include/opencv2/opencv_modules.hpp
	-- Installing: /usr/local/lib/pkgconfig/opencv.pc
	-- Old export file "/usr/local/share/OpenCV/OpenCVModules.cmake" will be replaced.  Removing files [/usr/local/share/OpenCV/OpenCVModules-release.cmake].
	-- Installing: /usr/local/share/OpenCV/OpenCVModules.cmake
	-- Installing: /usr/local/share/OpenCV/OpenCVModules-release.cmake
	-- Installing: /usr/local/share/OpenCV/OpenCVConfig-version.cmake
	-- Installing: /usr/local/share/OpenCV/OpenCVConfig.cmake
	-- Up-to-date: /usr/local/share/OpenCV/valgrind.supp
	-- Up-to-date: /usr/local/share/OpenCV/valgrind_3rdparty.supp
	-- Installing: /usr/local/share/OpenCV/licenses/zlib-README
	-- Up-to-date: /usr/local/share/OpenCV/licenses/libjpeg-turbo-README.md
	-- Up-to-date: /usr/local/share/OpenCV/licenses/libjpeg-turbo-LICENSE.md
	-- Up-to-date: /usr/local/share/OpenCV/licenses/libjpeg-turbo-README.ijg
	-- Installing: /usr/local/share/OpenCV/licenses/libtiff-COPYRIGHT
	-- Installing: /usr/local/share/OpenCV/licenses/jasper-LICENSE
	-- Installing: /usr/local/share/OpenCV/licenses/jasper-README
	-- Installing: /usr/local/share/OpenCV/licenses/jasper-copyright
	-- Installing: /usr/local/share/OpenCV/licenses/libpng-LICENSE
	-- Installing: /usr/local/share/OpenCV/licenses/libpng-README
	-- Installing: /usr/local/share/OpenCV/licenses/libpng-opencv-libpng.patch
	-- Installing: /usr/local/share/OpenCV/licenses/openexr-LICENSE
	-- Installing: /usr/local/share/OpenCV/licenses/openexr-AUTHORS.ilmbase
	-- Installing: /usr/local/share/OpenCV/licenses/openexr-AUTHORS.openexr
	-- Installing: /usr/local/share/OpenCV/licenses/openexr-fix_msvc2013_errors.patch
	-- Up-to-date: /usr/local/share/OpenCV/licenses/protobuf-LICENSE
	-- Up-to-date: /usr/local/share/OpenCV/licenses/protobuf-README.md
	-- Up-to-date: /usr/local/share/OpenCV/licenses/ittnotify-LICENSE.BSD
	-- Up-to-date: /usr/local/share/OpenCV/licenses/ittnotify-LICENSE.GPL
	-- Up-to-date: /usr/local/include/opencv/cv.h
	-- Up-to-date: /usr/local/include/opencv/cv.hpp
	-- Up-to-date: /usr/local/include/opencv/cvaux.h
	-- Up-to-date: /usr/local/include/opencv/cvaux.hpp
	-- Up-to-date: /usr/local/include/opencv/cvwimage.h
	-- Up-to-date: /usr/local/include/opencv/cxcore.h
	-- Up-to-date: /usr/local/include/opencv/cxcore.hpp
	-- Up-to-date: /usr/local/include/opencv/cxeigen.hpp
	-- Up-to-date: /usr/local/include/opencv/cxmisc.h
	-- Up-to-date: /usr/local/include/opencv/highgui.h
	-- Up-to-date: /usr/local/include/opencv/ml.h
	-- Up-to-date: /usr/local/include/opencv2/opencv.hpp
	-- Installing: /usr/local/lib/libopencv_core.3.4.2.dylib
	-- Installing: /usr/local/lib/libopencv_core.3.4.dylib
	-- Installing: /usr/local/lib/libopencv_core.dylib
	-- Up-to-date: /usr/local/include/opencv2/core/opencl/ocl_defs.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/opencl/opencl_info.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/opencl/opencl_svm.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/opencl/runtime/autogenerated/opencl_clamdblas.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/opencl/runtime/autogenerated/opencl_clamdfft.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/opencl/runtime/autogenerated/opencl_core.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/opencl/runtime/autogenerated/opencl_core_wrappers.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/opencl/runtime/autogenerated/opencl_gl.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/opencl/runtime/autogenerated/opencl_gl_wrappers.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/opencl/runtime/opencl_clamdblas.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/opencl/runtime/opencl_clamdfft.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/opencl/runtime/opencl_core.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/opencl/runtime/opencl_core_wrappers.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/opencl/runtime/opencl_gl.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/opencl/runtime/opencl_gl_wrappers.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/opencl/runtime/opencl_svm_20.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/opencl/runtime/opencl_svm_definitions.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/opencl/runtime/opencl_svm_hsa_extension.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/cuda/block.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/cuda/border_interpolate.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/cuda/color.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/cuda/common.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/cuda/datamov_utils.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/cuda/dynamic_smem.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/cuda/emulation.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/cuda/filters.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/cuda/funcattrib.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/cuda/functional.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/cuda/limits.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/cuda/reduce.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/cuda/saturate_cast.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/cuda/scan.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/cuda/simd_functions.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/cuda/transform.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/cuda/type_traits.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/cuda/utility.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/cuda/vec_distance.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/cuda/vec_math.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/cuda/vec_traits.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/cuda/warp.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/cuda/warp_reduce.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/cuda/warp_shuffle.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/cuda/detail/color_detail.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/cuda/detail/reduce.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/cuda/detail/reduce_key_val.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/cuda/detail/transform_detail.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/cuda/detail/type_traits_detail.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/cuda/detail/vec_distance_detail.hpp
	-- Up-to-date: /usr/local/include/opencv2/core.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/affine.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/base.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/bufferpool.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/check.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/core.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/core_c.h
	-- Up-to-date: /usr/local/include/opencv2/core/cuda.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/cuda.inl.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/cuda_stream_accessor.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/cuda_types.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/cv_cpu_dispatch.h
	-- Up-to-date: /usr/local/include/opencv2/core/cv_cpu_helper.h
	-- Up-to-date: /usr/local/include/opencv2/core/cvdef.h
	-- Up-to-date: /usr/local/include/opencv2/core/cvstd.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/cvstd.inl.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/directx.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/eigen.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/fast_math.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/hal/hal.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/hal/interface.h
	-- Up-to-date: /usr/local/include/opencv2/core/hal/intrin.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/hal/intrin_cpp.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/hal/intrin_neon.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/hal/intrin_sse.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/hal/intrin_vsx.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/ippasync.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/mat.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/mat.inl.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/matx.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/neon_utils.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/ocl.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/ocl_genbase.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/opengl.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/operations.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/optim.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/ovx.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/persistence.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/ptr.inl.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/saturate.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/softfloat.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/sse_utils.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/traits.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/types.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/types_c.h
	-- Up-to-date: /usr/local/include/opencv2/core/utility.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/utils/filesystem.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/utils/logger.defines.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/utils/logger.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/utils/trace.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/va_intel.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/version.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/vsx_utils.hpp
	-- Up-to-date: /usr/local/include/opencv2/core/wimage.hpp
	-- Up-to-date: /usr/local/share/OpenCV/licenses/SoftFloat-COPYING.txt
	-- Installing: /usr/local/lib/libopencv_flann.3.4.2.dylib
	-- Installing: /usr/local/lib/libopencv_flann.3.4.dylib
	-- Installing: /usr/local/lib/libopencv_flann.dylib
	-- Up-to-date: /usr/local/include/opencv2/flann.hpp
	-- Up-to-date: /usr/local/include/opencv2/flann/all_indices.h
	-- Up-to-date: /usr/local/include/opencv2/flann/allocator.h
	-- Up-to-date: /usr/local/include/opencv2/flann/any.h
	-- Up-to-date: /usr/local/include/opencv2/flann/autotuned_index.h
	-- Up-to-date: /usr/local/include/opencv2/flann/composite_index.h
	-- Up-to-date: /usr/local/include/opencv2/flann/config.h
	-- Up-to-date: /usr/local/include/opencv2/flann/defines.h
	-- Up-to-date: /usr/local/include/opencv2/flann/dist.h
	-- Up-to-date: /usr/local/include/opencv2/flann/dummy.h
	-- Up-to-date: /usr/local/include/opencv2/flann/dynamic_bitset.h
	-- Up-to-date: /usr/local/include/opencv2/flann/flann.hpp
	-- Up-to-date: /usr/local/include/opencv2/flann/flann_base.hpp
	-- Up-to-date: /usr/local/include/opencv2/flann/general.h
	-- Up-to-date: /usr/local/include/opencv2/flann/ground_truth.h
	-- Up-to-date: /usr/local/include/opencv2/flann/hdf5.h
	-- Up-to-date: /usr/local/include/opencv2/flann/heap.h
	-- Up-to-date: /usr/local/include/opencv2/flann/hierarchical_clustering_index.h
	-- Up-to-date: /usr/local/include/opencv2/flann/index_testing.h
	-- Up-to-date: /usr/local/include/opencv2/flann/kdtree_index.h
	-- Up-to-date: /usr/local/include/opencv2/flann/kdtree_single_index.h
	-- Up-to-date: /usr/local/include/opencv2/flann/kmeans_index.h
	-- Up-to-date: /usr/local/include/opencv2/flann/linear_index.h
	-- Up-to-date: /usr/local/include/opencv2/flann/logger.h
	-- Up-to-date: /usr/local/include/opencv2/flann/lsh_index.h
	-- Up-to-date: /usr/local/include/opencv2/flann/lsh_table.h
	-- Up-to-date: /usr/local/include/opencv2/flann/matrix.h
	-- Up-to-date: /usr/local/include/opencv2/flann/miniflann.hpp
	-- Up-to-date: /usr/local/include/opencv2/flann/nn_index.h
	-- Up-to-date: /usr/local/include/opencv2/flann/object_factory.h
	-- Up-to-date: /usr/local/include/opencv2/flann/params.h
	-- Up-to-date: /usr/local/include/opencv2/flann/random.h
	-- Up-to-date: /usr/local/include/opencv2/flann/result_set.h
	-- Up-to-date: /usr/local/include/opencv2/flann/sampling.h
	-- Up-to-date: /usr/local/include/opencv2/flann/saving.h
	-- Up-to-date: /usr/local/include/opencv2/flann/simplex_downhill.h
	-- Up-to-date: /usr/local/include/opencv2/flann/timer.h
	-- Installing: /usr/local/lib/libopencv_imgproc.3.4.2.dylib
	-- Installing: /usr/local/lib/libopencv_imgproc.3.4.dylib
	-- Installing: /usr/local/lib/libopencv_imgproc.dylib
	-- Up-to-date: /usr/local/include/opencv2/imgproc.hpp
	-- Up-to-date: /usr/local/include/opencv2/imgproc/hal/hal.hpp
	-- Up-to-date: /usr/local/include/opencv2/imgproc/hal/interface.h
	-- Up-to-date: /usr/local/include/opencv2/imgproc/imgproc.hpp
	-- Up-to-date: /usr/local/include/opencv2/imgproc/imgproc_c.h
	-- Up-to-date: /usr/local/include/opencv2/imgproc/types_c.h
	-- Up-to-date: /usr/local/include/opencv2/imgproc/detail/distortion_model.hpp
	-- Installing: /usr/local/lib/libopencv_ml.3.4.2.dylib
	-- Installing: /usr/local/lib/libopencv_ml.3.4.dylib
	-- Installing: /usr/local/lib/libopencv_ml.dylib
	-- Up-to-date: /usr/local/include/opencv2/ml.hpp
	-- Up-to-date: /usr/local/include/opencv2/ml/ml.hpp
	-- Up-to-date: /usr/local/include/opencv2/ml/ml.inl.hpp
	-- Installing: /usr/local/lib/libopencv_objdetect.3.4.2.dylib
	-- Installing: /usr/local/lib/libopencv_objdetect.3.4.dylib
	-- Installing: /usr/local/lib/libopencv_objdetect.dylib
	-- Up-to-date: /usr/local/include/opencv2/objdetect.hpp
	-- Up-to-date: /usr/local/include/opencv2/objdetect/detection_based_tracker.hpp
	-- Up-to-date: /usr/local/include/opencv2/objdetect/objdetect.hpp
	-- Up-to-date: /usr/local/include/opencv2/objdetect/objdetect_c.h
	-- Installing: /usr/local/lib/libopencv_photo.3.4.2.dylib
	-- Installing: /usr/local/lib/libopencv_photo.3.4.dylib
	-- Installing: /usr/local/lib/libopencv_photo.dylib
	-- Up-to-date: /usr/local/include/opencv2/photo.hpp
	-- Up-to-date: /usr/local/include/opencv2/photo/cuda.hpp
	-- Up-to-date: /usr/local/include/opencv2/photo/photo.hpp
	-- Up-to-date: /usr/local/include/opencv2/photo/photo_c.h
	-- Installing: /usr/local/lib/libopencv_video.3.4.2.dylib
	-- Installing: /usr/local/lib/libopencv_video.3.4.dylib
	-- Installing: /usr/local/lib/libopencv_video.dylib
	-- Up-to-date: /usr/local/include/opencv2/video.hpp
	-- Up-to-date: /usr/local/include/opencv2/video/background_segm.hpp
	-- Up-to-date: /usr/local/include/opencv2/video/tracking.hpp
	-- Up-to-date: /usr/local/include/opencv2/video/tracking_c.h
	-- Up-to-date: /usr/local/include/opencv2/video/video.hpp
	-- Installing: /usr/local/lib/libopencv_dnn.3.4.2.dylib
	-- Installing: /usr/local/lib/libopencv_dnn.3.4.dylib
	-- Installing: /usr/local/lib/libopencv_dnn.dylib
	-- Up-to-date: /usr/local/include/opencv2/dnn.hpp
	-- Up-to-date: /usr/local/include/opencv2/dnn/all_layers.hpp
	-- Up-to-date: /usr/local/include/opencv2/dnn/dict.hpp
	-- Up-to-date: /usr/local/include/opencv2/dnn/dnn.hpp
	-- Up-to-date: /usr/local/include/opencv2/dnn/dnn.inl.hpp
	-- Up-to-date: /usr/local/include/opencv2/dnn/layer.details.hpp
	-- Up-to-date: /usr/local/include/opencv2/dnn/layer.hpp
	-- Up-to-date: /usr/local/include/opencv2/dnn/shape_utils.hpp
	-- Installing: /usr/local/lib/libopencv_imgcodecs.3.4.2.dylib
	-- Installing: /usr/local/lib/libopencv_imgcodecs.3.4.dylib
	-- Installing: /usr/local/lib/libopencv_imgcodecs.dylib
	-- Up-to-date: /usr/local/include/opencv2/imgcodecs.hpp
	-- Up-to-date: /usr/local/include/opencv2/imgcodecs/imgcodecs.hpp
	-- Up-to-date: /usr/local/include/opencv2/imgcodecs/imgcodecs_c.h
	-- Up-to-date: /usr/local/include/opencv2/imgcodecs/ios.h
	-- Installing: /usr/local/lib/libopencv_shape.3.4.2.dylib
	-- Installing: /usr/local/lib/libopencv_shape.3.4.dylib
	-- Installing: /usr/local/lib/libopencv_shape.dylib
	-- Up-to-date: /usr/local/include/opencv2/shape.hpp
	-- Up-to-date: /usr/local/include/opencv2/shape/emdL1.hpp
	-- Up-to-date: /usr/local/include/opencv2/shape/hist_cost.hpp
	-- Up-to-date: /usr/local/include/opencv2/shape/shape.hpp
	-- Up-to-date: /usr/local/include/opencv2/shape/shape_distance.hpp
	-- Up-to-date: /usr/local/include/opencv2/shape/shape_transformer.hpp
	-- Installing: /usr/local/lib/libopencv_videoio.3.4.2.dylib
	-- Installing: /usr/local/lib/libopencv_videoio.3.4.dylib
	-- Installing: /usr/local/lib/libopencv_videoio.dylib
	-- Up-to-date: /usr/local/include/opencv2/videoio.hpp
	-- Up-to-date: /usr/local/include/opencv2/videoio/cap_ios.h
	-- Up-to-date: /usr/local/include/opencv2/videoio/videoio.hpp
	-- Up-to-date: /usr/local/include/opencv2/videoio/videoio_c.h
	-- Installing: /usr/local/lib/libopencv_highgui.3.4.2.dylib
	-- Installing: /usr/local/lib/libopencv_highgui.3.4.dylib
	-- Installing: /usr/local/lib/libopencv_highgui.dylib
	-- Up-to-date: /usr/local/include/opencv2/highgui.hpp
	-- Up-to-date: /usr/local/include/opencv2/highgui/highgui.hpp
	-- Up-to-date: /usr/local/include/opencv2/highgui/highgui_c.h
	-- Installing: /usr/local/lib/libopencv_superres.3.4.2.dylib
	-- Installing: /usr/local/lib/libopencv_superres.3.4.dylib
	-- Installing: /usr/local/lib/libopencv_superres.dylib
	-- Up-to-date: /usr/local/include/opencv2/superres.hpp
	-- Up-to-date: /usr/local/include/opencv2/superres/optical_flow.hpp
	-- Installing: /usr/local/lib/libopencv_features2d.3.4.2.dylib
	-- Installing: /usr/local/lib/libopencv_features2d.3.4.dylib
	-- Installing: /usr/local/lib/libopencv_features2d.dylib
	-- Up-to-date: /usr/local/include/opencv2/features2d.hpp
	-- Up-to-date: /usr/local/include/opencv2/features2d/features2d.hpp
	-- Up-to-date: /usr/local/include/opencv2/features2d/hal/interface.h
	-- Installing: /usr/local/lib/libopencv_calib3d.3.4.2.dylib
	-- Installing: /usr/local/lib/libopencv_calib3d.3.4.dylib
	-- Installing: /usr/local/lib/libopencv_calib3d.dylib
	-- Up-to-date: /usr/local/include/opencv2/calib3d.hpp
	-- Up-to-date: /usr/local/include/opencv2/calib3d/calib3d.hpp
	-- Up-to-date: /usr/local/include/opencv2/calib3d/calib3d_c.h
	-- Installing: /usr/local/lib/libopencv_stitching.3.4.2.dylib
	-- Installing: /usr/local/lib/libopencv_stitching.3.4.dylib
	-- Installing: /usr/local/lib/libopencv_stitching.dylib
	-- Up-to-date: /usr/local/include/opencv2/stitching.hpp
	-- Up-to-date: /usr/local/include/opencv2/stitching/warpers.hpp
	-- Up-to-date: /usr/local/include/opencv2/stitching/detail/autocalib.hpp
	-- Up-to-date: /usr/local/include/opencv2/stitching/detail/blenders.hpp
	-- Up-to-date: /usr/local/include/opencv2/stitching/detail/camera.hpp
	-- Up-to-date: /usr/local/include/opencv2/stitching/detail/exposure_compensate.hpp
	-- Up-to-date: /usr/local/include/opencv2/stitching/detail/matchers.hpp
	-- Up-to-date: /usr/local/include/opencv2/stitching/detail/motion_estimators.hpp
	-- Up-to-date: /usr/local/include/opencv2/stitching/detail/seam_finders.hpp
	-- Up-to-date: /usr/local/include/opencv2/stitching/detail/timelapsers.hpp
	-- Up-to-date: /usr/local/include/opencv2/stitching/detail/util.hpp
	-- Up-to-date: /usr/local/include/opencv2/stitching/detail/util_inl.hpp
	-- Up-to-date: /usr/local/include/opencv2/stitching/detail/warpers.hpp
	-- Up-to-date: /usr/local/include/opencv2/stitching/detail/warpers_inl.hpp
	-- Installing: /usr/local/lib/libopencv_videostab.3.4.2.dylib
	-- Installing: /usr/local/lib/libopencv_videostab.3.4.dylib
	-- Installing: /usr/local/lib/libopencv_videostab.dylib
	-- Up-to-date: /usr/local/include/opencv2/videostab.hpp
	-- Up-to-date: /usr/local/include/opencv2/videostab/deblurring.hpp
	-- Up-to-date: /usr/local/include/opencv2/videostab/fast_marching.hpp
	-- Up-to-date: /usr/local/include/opencv2/videostab/fast_marching_inl.hpp
	-- Up-to-date: /usr/local/include/opencv2/videostab/frame_source.hpp
	-- Up-to-date: /usr/local/include/opencv2/videostab/global_motion.hpp
	-- Up-to-date: /usr/local/include/opencv2/videostab/inpainting.hpp
	-- Up-to-date: /usr/local/include/opencv2/videostab/log.hpp
	-- Up-to-date: /usr/local/include/opencv2/videostab/motion_core.hpp
	-- Up-to-date: /usr/local/include/opencv2/videostab/motion_stabilizing.hpp
	-- Up-to-date: /usr/local/include/opencv2/videostab/optical_flow.hpp
	-- Up-to-date: /usr/local/include/opencv2/videostab/outlier_rejection.hpp
	-- Up-to-date: /usr/local/include/opencv2/videostab/ring_buffer.hpp
	-- Up-to-date: /usr/local/include/opencv2/videostab/stabilizer.hpp
	-- Up-to-date: /usr/local/include/opencv2/videostab/wobble_suppression.hpp
	-- Up-to-date: /usr/local/share/OpenCV/haarcascades/haarcascade_eye.xml
	-- Up-to-date: /usr/local/share/OpenCV/haarcascades/haarcascade_eye_tree_eyeglasses.xml
	-- Up-to-date: /usr/local/share/OpenCV/haarcascades/haarcascade_frontalcatface.xml
	-- Up-to-date: /usr/local/share/OpenCV/haarcascades/haarcascade_frontalcatface_extended.xml
	-- Up-to-date: /usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml
	-- Up-to-date: /usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt2.xml
	-- Up-to-date: /usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt_tree.xml
	-- Up-to-date: /usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml
	-- Up-to-date: /usr/local/share/OpenCV/haarcascades/haarcascade_fullbody.xml
	-- Up-to-date: /usr/local/share/OpenCV/haarcascades/haarcascade_lefteye_2splits.xml
	-- Up-to-date: /usr/local/share/OpenCV/haarcascades/haarcascade_licence_plate_rus_16stages.xml
	-- Up-to-date: /usr/local/share/OpenCV/haarcascades/haarcascade_lowerbody.xml
	-- Up-to-date: /usr/local/share/OpenCV/haarcascades/haarcascade_profileface.xml
	-- Up-to-date: /usr/local/share/OpenCV/haarcascades/haarcascade_righteye_2splits.xml
	-- Up-to-date: /usr/local/share/OpenCV/haarcascades/haarcascade_russian_plate_number.xml
	-- Up-to-date: /usr/local/share/OpenCV/haarcascades/haarcascade_smile.xml
	-- Up-to-date: /usr/local/share/OpenCV/haarcascades/haarcascade_upperbody.xml
	-- Up-to-date: /usr/local/share/OpenCV/lbpcascades/lbpcascade_frontalcatface.xml
	-- Up-to-date: /usr/local/share/OpenCV/lbpcascades/lbpcascade_frontalface.xml
	-- Up-to-date: /usr/local/share/OpenCV/lbpcascades/lbpcascade_frontalface_improved.xml
	-- Up-to-date: /usr/local/share/OpenCV/lbpcascades/lbpcascade_profileface.xml
	-- Up-to-date: /usr/local/share/OpenCV/lbpcascades/lbpcascade_silverware.xml
	-- Installing: /usr/local/bin/opencv_traincascade
	-- Installing: /usr/local/bin/opencv_createsamples
	-- Installing: /usr/local/bin/opencv_annotation
	-- Installing: /usr/local/bin/opencv_visualisation
	-- Installing: /usr/local/bin/opencv_interactive-calibration
	-- Installing: /usr/local/bin/opencv_version
	```
	

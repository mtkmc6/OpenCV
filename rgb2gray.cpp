#include <iostream>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <string>

using namespace std;
using namespace cv;


int main(int argc, char* argv[])
{
	std::string input = "";

	if (argc != 3)
	{
		std::cout << "Incorrect Program Arguments\nPlease use format:"
			" ./rgb2gray input_color_image_filename output_grayscale_image_filename " << std::endl;
		return 0;
	}

	std::string input_color_image_filename = argv[1];
	std::string output_grayscale_image_filename = argv[2];

    Mat src = imread(input_color_image_filename, cv::IMREAD_COLOR); //load  image
	Mat modified= imread(input_color_image_filename, cv::IMREAD_COLOR); //load  image
	Mat gray= imread(input_color_image_filename, 0); //load  image grayscale


	
	for (int r = 0; r < modified.rows; r++) {
		for (int c = 0; c < modified.cols; c++) {
			gray.at<uint8_t>(r, c) = modified.at<cv::Vec3b>(r, c)[0] * .1140 +  modified.at<cv::Vec3b>(r, c)[1] * .5871 +  modified.at<cv::Vec3b>(r, c)[2] * .2989 ; //Each channel multiplied
			

		}
	}


   
	
	
	imshow("Original", src);
	imshow("GreyScale",gray);
	imwrite(output_grayscale_image_filename, gray);
	waitKey();








    return 0;
}


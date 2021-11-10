#include <iostream>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>

using namespace std;
using namespace cv;


int main(int argc, char* argv[]) {

	if (argc != 5)
	{
		std::cout << "Incorrect Program Arguments\nPlease use format:"
			"./contrast min_value max_value input_image_filename output_image_filename" << std::endl;
		return 0;
	}

	std::string input_image_filename = argv[3];
	std::string output_image_filename = argv[4];
	float intensity = atof(argv[1]);

	Mat img = imread(input_image_filename, 0); // load grayscale
	Mat modified = imread(input_image_filename, 0); // load grayscale
	imshow("Before", img);
	
	float min = atof(argv[1]);
	float max = atof(argv[2]);

	float slope = 255 / (max - min);
	float b = (-1) * slope * min;


	for (int r = 0; r < modified.rows; r++) {
		for (int c = 0; c < modified.cols; c++) {
			if (modified.at<uint8_t>(r, c) > max) {
				modified.at<uint8_t>(r, c) = 255;
			}

			else if (modified.at<uint8_t>(r, c) < min) {
				modified.at<uint8_t>(r, c) = 0;
			}

			else{
		
				modified.at<uint8_t>(r, c)= (modified.at<uint8_t>(r, c) * slope) + b; // Changes contrast and brightness
			}


		}
	}

	imshow("After", modified);
	imwrite(output_image_filename, modified);
	waitKey();

	return 0;

}

#include <iostream>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>

using namespace std;
using namespace cv;

int main(int argc, char* argv[]) {
	if (argc != 4)
	{
		std::cout << "Incorrect Program Arguments\nPlease use format:"
			"./brightness intensity_value input_image_filename output_image_filename " << std::endl;
		return 0;
	}

	std::string input_image_filename = argv[2];
	std::string output_image_filename = argv[3];
	float intensity = atof(argv[1]);

	if (intensity < -100 || intensity> 100) {
		std::cout << "Incorrect Intensity Value, must be between -100 and 100" << endl;
		return 0;
	}


	Mat img = imread(input_image_filename, 0); // load grayscale
	Mat modified = imread(input_image_filename, 0); // load grayscale
	imshow("Before", img);

	for (int r = 0; r < modified.rows; r++) {
		for (int c = 0; c < modified.cols; c++) {
			if ((intensity > 0) && (modified.at<uint8_t>(r, c) > (255 - intensity))) {
				modified.at<uint8_t>(r, c) = 255;
			}

			else if (intensity < 0 && modified.at<uint8_t>(r, c) < (intensity * -1)) {
				modified.at<uint8_t>(r, c) = 0;
			}


		

			else {
				modified.at<uint8_t>(r, c) += intensity; // Increase Brightness
			}


		}
	}

	imshow("After", modified);
	imwrite(output_image_filename, modified);
	waitKey();

	return 0;

}

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
			"./gray2binary input_grayscale_image_filename output_binary_image_filename threshold_value input_ground_truth_image" << std::endl;
		return 0;
	}

	std::string input_grayscale_image_filename = argv[1];
	std::string output_binary_image_filename = argv[2];
	float threshold = atof(argv[3]);
	std::string input_ground_truth_image = argv[4];

	int TP = 0;
	int TN = 0;
	int FP = 0;
	int FN = 0;

	Mat img = imread(input_grayscale_image_filename, 0); // load grayscale
	Mat modified = imread(input_grayscale_image_filename, 0); // load grayscale
	Mat groundtruth= imread(input_ground_truth_image, 0);
	imshow("Before", img);
	
	


	for (int r = 0; r < modified.rows; r++) {
		for (int c = 0; c < modified.cols; c++) {

			if (modified.at<uint8_t>(r, c) <= threshold) {
				modified.at<uint8_t>(r, c) = 0;

				if (groundtruth.at<uint8_t>(r, c) == 0) {

					TN++;
				}
				else {

					FN++;
				}
			}



			if (modified.at<uint8_t>(r, c) > threshold) {
				modified.at<uint8_t>(r, c) = 255;

				if (groundtruth.at<uint8_t>(r, c) == 255) {

					TP++;
				}
				else {

					FP++;
				}
			}
		
		}	
	}
	

	imshow("After", modified);
	imwrite(output_binary_image_filename, modified);
	cout << "TP:" << TP << endl << "TN " << TN << endl << "FP:" << FP << endl << "FN:" << FN << endl;
	waitKey();

	return 0;
}


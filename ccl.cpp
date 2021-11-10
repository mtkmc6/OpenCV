#include <iostream>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <string>

using namespace std;
using namespace cv;


int Parent[2000]; //Parent Array



int find(int X) { //Recursive Function used to find Root parent of an Independent Label

	if ((Parent[X] != X)) {
		return find(Parent[X]);
	}
	else {
		return X;
	}

}



//First argument is input image filename
//Second argument is whether or not to invert. If you want to envert pass '1', if not pass '0'
//Third argument is output image filename 
int main(int argc, char* argv[]) {

	if (argc != 4) {
		cout << "Incorrect Program Arguments\nPlease use format:\n"
			"\"./ccl input_binary_image_filename invert output_rgb_image_filename\"" << endl;
		return 0;
	}

	std::string input_binary_image_filename = argv[1];
	int invert = atoi(argv[2]);
	std::string output_rgb_image_filename = argv[3];

	Mat src = imread(input_binary_image_filename, 0); //load  image grayscale
	

	Mat modified = imread(input_binary_image_filename, 0); //load  image grayscale
	Mat Output = imread(input_binary_image_filename, cv::IMREAD_COLOR); //load  image rgb

	imshow("Original", src);



	//invert binary image if invert=1
	if (invert == 1) {
		for (int r = 0; r < modified.rows; r++) {
			for (int c = 0; c < modified.cols; c++) {
				if (modified.at<uint8_t>(r, c) == 255) {
					src.at<uint8_t>(r, c) = 0;
					modified.at<uint8_t>(r, c) = 0;
				}
				else {
					modified.at<uint8_t>(r, c) = 255;
					src.at<uint8_t>(r, c) = 255;
				}


			}
		}
	}
	
	

	int r = modified.rows;
	int c = modified.cols;

	int** LabelArray = new int* [modified.rows];
	for (int i = 0; i < modified.rows; ++i) {
		LabelArray[i] = new int[modified.cols];
	}



	for (int i = 0; i < 2000; i++) {
		Parent[i] = 0; //Initialize parent array so that all Independent labels are their own parent
	}

	for (int r = 0; r < modified.rows; r++) {
		for (int c = 0; c < modified.cols; c++) {
			LabelArray[r][c] = 0; //Initialize array to 0
		}
	}

	int IL = 1; //Counter for Independt Labels
	int NoNeighbors = 0; //If there are neighbors, set to 0, else set to 1
	for (int r = 0; r < modified.rows; r++) {  //first pass
		for (int c = 0; c < modified.cols; c++) {
			if (modified.at<uint8_t>(r, c) == 255) {
				if (r != 0 && c != 0) {
					if ((modified.at<uint8_t>(r - 1, c - 1) == 255)) { //If r or c is 0, goes out of array bounds
						NoNeighbors = 1;
						LabelArray[r][c] = LabelArray[r - 1][c - 1];
					}
				}

				 if (r != 0) {

					if ((modified.at<uint8_t>(r - 1, c) == 255) && (r != 0)) {
						NoNeighbors = 1;
						if ((LabelArray[r][c] != 0) && (LabelArray[r][c] != LabelArray[r-1][c])) {//Already got labeled by previous neighbor
							if (LabelArray[r][c] < LabelArray[r - 1][c]) {
								Parent[LabelArray[r-1][c]] = LabelArray[r][c]; //Smaller label is set to parent, Union lables
							}
							else {
								Parent[LabelArray[r][c]] = LabelArray[r-1][c];
							}
						}

						else {
							LabelArray[r][c] = LabelArray[r - 1][c];

						}

					
					}
				}

				 if (r != 0 && c != 255) {
					if ((modified.at<uint8_t>(r - 1, c + 1) == 255) && (r != 0)) {
						NoNeighbors = 1;
						if ((LabelArray[r][c] != 0) && (LabelArray[r][c] != LabelArray[r - 1][c+1])) {//Already got labeled by previous neighbor
							if (LabelArray[r][c] < LabelArray[r - 1][c+1]) {
								Parent[LabelArray[r - 1][c+1]] = LabelArray[r][c]; //Smaller label is set to parent
							}
							else {
								Parent[LabelArray[r][c]] = LabelArray[r - 1][c+1];
							}
						}

						else {
							LabelArray[r][c] = LabelArray[r - 1][c+1];

						}
					}
				}

				 if (c != 0) {
					if ((modified.at<uint8_t>(r, c - 1) == 255) && (c != 0)) {
						NoNeighbors = 1;
						if ((LabelArray[r][c] != 0) && (LabelArray[r][c] != LabelArray[r][c-1])) {//Already got labeled by previous neighbor
							if (LabelArray[r][c] < LabelArray[r][c-1]) {
								Parent[LabelArray[r][c-1]] = LabelArray[r][c]; //Smaller label is set to parent
							}
							else {
								Parent[LabelArray[r][c]] = LabelArray[r][c-1];
							}
						}

						else {
							LabelArray[r][c] = LabelArray[r][c-1];

						}
					}
				}

				if(NoNeighbors == 0) {
					LabelArray[r][c] = IL;
					Parent[IL] = IL; //If no neighbors, it becomes its own parent
					IL++; //Increment for each new label
				}
				
			
			}
			NoNeighbors = 0; //Reset back to 0 after each iteration
			//cout << LabelArray[r][c] << endl;
		}
	}

	
	
	int temp = 0;
	int Label = 1;
	int flag = 0;
	int FinalLabels[25];
	for (int i = 0; i < 25; i++) {
		FinalLabels[i] = 0;
	}

	int max = 0;

	for (int r = 0; r < modified.rows; r++) {
		for (int c = 0; c < modified.cols; c++) {
			if (LabelArray[r][c] > max) {
				max = LabelArray[r][c];
			}
		}
	}

	for (int r = 0; r < modified.rows; r++) {  //second pass
		for (int c = 0; c < modified.cols; c++) {
			if (LabelArray[r][c] != 0) {

				
				temp= find(LabelArray[r][c]); 
				
				
				for (int i = 0; i < 25; i++) {
					if (temp == FinalLabels[i]) { //Assigns each independent Label a Component index in FinalLabels
						LabelArray[r][c] = i;
						flag = 1; 
						break;
					}
					
				

				}
				if (flag == 0) { //If flag is 0, that means independent label becomes its own component
					Label++;
					FinalLabels[Label] = LabelArray[r][c];
				}
				flag = 0;
			}
		}
	}
	


	for (int r = 0; r < modified.rows; r++) {  //Colorize different labels BGR
		for (int c = 0; c < modified.cols; c++) {

			if (LabelArray[r][c] == 1) { //Sets to Blue
				Output.at<cv::Vec3b>(r, c)[0] = 255; //Blue
				Output.at<cv::Vec3b>(r, c)[1] = 32;//Green
				Output.at<cv::Vec3b>(r, c)[2] = 0;//Red
			}

			else if (LabelArray[r][c] == 2) { //Sets to Green
				Output.at<cv::Vec3b>(r, c)[0] = 0; //Blue
				Output.at<cv::Vec3b>(r, c)[1] = 192;//Green
				Output.at<cv::Vec3b>(r, c)[2] = 0;//Red
			}



			else if (LabelArray[r][c] == 3) { //Sets to Purple
				Output.at<cv::Vec3b>(r, c)[0] = 255; //Blue
				Output.at<cv::Vec3b>(r, c)[1] = 32;//Green
				Output.at<cv::Vec3b>(r, c)[2] = 160;//Red
			}

			else if (LabelArray[r][c] == 4) { //Sets to Yellow
				Output.at<cv::Vec3b>(r, c)[0] = 32; //Blue
				Output.at<cv::Vec3b>(r, c)[1] = 224;//Green
				Output.at<cv::Vec3b>(r, c)[2] = 255;//Red
			}

			else if (LabelArray[r][c] == 5) { //Sets to Orange
				Output.at<cv::Vec3b>(r, c)[0] = 16; //Blue
				Output.at<cv::Vec3b>(r, c)[1] = 160;//Green
				Output.at<cv::Vec3b>(r, c)[2] = 255;//Red
			}

			else if (LabelArray[r][c] == 6) { //Sets to Brown
				Output.at<cv::Vec3b>(r, c)[0] = 96; //Blue
				Output.at<cv::Vec3b>(r, c)[1] = 128;//Green
				Output.at<cv::Vec3b>(r, c)[2] = 160;//Red
			}

			else if (LabelArray[r][c] == 7) { //Sets to Pink
				Output.at<cv::Vec3b>(r, c)[0] = 208; //Blue
				Output.at<cv::Vec3b>(r, c)[1] = 96;//Green
				Output.at<cv::Vec3b>(r, c)[2] = 255;//Red
			}

			else if (LabelArray[r][c] == 8) { //Sets to Dark yellow
				Output.at<cv::Vec3b>(r, c)[0] = 6; //Blue
				Output.at<cv::Vec3b>(r, c)[1] = 127;//Green
				Output.at<cv::Vec3b>(r, c)[2] = 127;//Red
			}

			else if (LabelArray[r][c] == 9) { //Sets to Dark Green
				Output.at<cv::Vec3b>(r, c)[0] = 57; //Blue
				Output.at<cv::Vec3b>(r, c)[1] = 127;//Green
				Output.at<cv::Vec3b>(r, c)[2] = 80;//Red
			}

			else if (LabelArray[r][c] == 10) { //Sets to Baby BLue
				Output.at<cv::Vec3b>(r, c)[0] = 252; //Blue
				Output.at<cv::Vec3b>(r, c)[1] = 244;//Green
				Output.at<cv::Vec3b>(r, c)[2] = 12;//Red
			}

			else if (LabelArray[r][c] == 11) { //Sets to Dark Red
				Output.at<cv::Vec3b>(r, c)[0] = 6; //Blue
				Output.at<cv::Vec3b>(r, c)[1] = 6;//Green
				Output.at<cv::Vec3b>(r, c)[2] = 127;//Red
			}

			else if (LabelArray[r][c] == 12) { //Sets to Light Purple
				Output.at<cv::Vec3b>(r, c)[0] = 255; //Blue
				Output.at<cv::Vec3b>(r, c)[1] = 127;//Green
				Output.at<cv::Vec3b>(r, c)[2] = 229;//Red
			}

			else if (LabelArray[r][c] == 13) { //Sets to Light Green
				Output.at<cv::Vec3b>(r, c)[0] = 89; //Blue
				Output.at<cv::Vec3b>(r, c)[1] = 255;//Green
				Output.at<cv::Vec3b>(r, c)[2] = 89;//Red
			}

			else if (LabelArray[r][c] == 14) { //Sets to Gray
				Output.at<cv::Vec3b>(r, c)[0] = 102; //Blue
				Output.at<cv::Vec3b>(r, c)[1] = 102;//Green
				Output.at<cv::Vec3b>(r, c)[2] = 102;//Red
			}

			else if (LabelArray[r][c] == 15) { //Sets to Salmon COlor
				Output.at<cv::Vec3b>(r, c)[0] = 57; //Blue
				Output.at<cv::Vec3b>(r, c)[1] = 57;//Green
				Output.at<cv::Vec3b>(r, c)[2] = 229;//Red
			}

			else if (LabelArray[r][c] == 16) { //Sets light Purple
				Output.at<cv::Vec3b>(r, c)[0] = 255; //Blue
				Output.at<cv::Vec3b>(r, c)[1] = 127;//Green
				Output.at<cv::Vec3b>(r, c)[2] = 229;//Red
			}

			else if (LabelArray[r][c] == 17) { //Sets to greenis blue
				Output.at<cv::Vec3b>(r, c)[0] = 160; //Blue
				Output.at<cv::Vec3b>(r, c)[1] = 252;//Green
				Output.at<cv::Vec3b>(r, c)[2] = 12;//Red
			}

			else if (LabelArray[r][c] == 18) { //Sets to Light Gray
				Output.at<cv::Vec3b>(r, c)[0] = 191; //Blue
				Output.at<cv::Vec3b>(r, c)[1] = 191;//Green
				Output.at<cv::Vec3b>(r, c)[2] = 191;//Red
			}

			else if (LabelArray[r][c] == 19) { //Sets to Wine Red
				Output.at<cv::Vec3b>(r, c)[0] = 8; //Blue
				Output.at<cv::Vec3b>(r, c)[1] = 0;//Green
				Output.at<cv::Vec3b>(r, c)[2] = 51;//Red
			}

			else if (LabelArray[r][c] == 20) { //Sets to light orange
				Output.at<cv::Vec3b>(r, c)[0] = 89; //Blue
				Output.at<cv::Vec3b>(r, c)[1] = 192;//Green
				Output.at<cv::Vec3b>(r, c)[2] = 255;//Red
			}

			else { //Sets to Black or white, since it is background (not a label).
			if (invert == 1) { //Set background to white
				Output.at<cv::Vec3b>(r, c)[0] = 255; //Blue
				Output.at<cv::Vec3b>(r, c)[1] = 255;//Green
				Output.at<cv::Vec3b>(r, c)[2] = 255;//Red
				}
			else {
				Output.at<cv::Vec3b>(r, c)[0] = 0; //Blue
				Output.at<cv::Vec3b>(r, c)[1] = 0;//Green
				Output.at<cv::Vec3b>(r, c)[2] = 0;//Red
			}
			}

		}
	}


	//Part B
	//Number of Objects
	for (int i = 2; i < 25; i++) {
		if (FinalLabels[i] == 0) {
			cout << "Number of Components: " << i - 2 << endl;
			break;
		}
	}


	//Number of IL's
	
	cout << "Number of Independent Labels: " << max << endl;

	//Component Statistics
	for (int i = 2; i < 25; i++) {
		int component = FinalLabels[i];
		if (component == 0) {
			break;
		}
		cout << "Object label " << i - 1 << " is : " << endl;

		//Area
		int area = 0;
		for (int r = 0; r < modified.rows; r++) {
			for (int c = 0; c < modified.cols; c++) {
				if (LabelArray[r][c] == i) {
					area++; //Counts each pixel
				}
			}
		}

		cout << "Area : " << area << endl;


		//Centroid
		int rmax = 0;
		int cmax = 0;
		int rmin = 255;
		int cmin = 255;
		for (int r = 0; r < modified.rows; r++) {
			for (int c = 0; c < modified.cols; c++) {
				if (LabelArray[r][c] == i) { //Looks for max/min row and col values
					if (r > rmax) {
						rmax = r;
					}
					if (c > cmax) {
						cmax = c;
					}

					if (r < rmin) {
						rmin = r;
					}

					if (c < cmin) {
						cmin = c;
					}
				}

			}
		}

		float cr = (((float)rmax - (float)rmin) / 2) + rmin;	//Average of min and max values
		float cc= (((float)cmax - (float)cmin) / 2) + cmin;
		cout << "Centroid(r,c) : " << cr << ", " << cc << endl;

		//Convariance Matrix
		int sumr = 0; // Variance Sums
		int sumc = 0;
		int cosum = 0; //Covariance Sum
		for (int r = 0; r < modified.rows; r++) {
			for (int c = 0; c < modified.cols; c++) {
				if (LabelArray[r][c] == i) {
					sumr = sumr + ((r - cr) * (r - cr));
					sumc = sumc + ((c - cc) * (c - cc));
					cosum = cosum + ((r - cr) * (c - cr));
				}
			}
		}

		float rvariance = ((float)sumr) / ((float)area);
		float cvariance = ((float)sumc) / ((float)area);
		float covariance = ((float)cosum) / ((float)area);
		cout << "Covariance (2 X 2 Matrix) (vr vrc vrc vc) : " << rvariance << " " << covariance << " " << covariance << " " << cvariance << endl;

	}

	imwrite(output_rgb_image_filename, modified);
	
	for (int i = 0; i < modified.rows; ++i) { //Deallocate memory
		delete[] LabelArray[i];
	}
	delete[] LabelArray;

	
	imshow("Colorized Blob Output", Output);



	


	waitKey();




	return 0;

}


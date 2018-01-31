// main.cpp

#include<opencv2/core.hpp>
#include<opencv2/highgui.hpp>
#include<opencv2/imgproc.hpp>

#include<iostream>
//#include<conio.h>           // it may be necessary to change or remove this line if not using Windows

//#include "Blob.h"

#define SHOW_STEPS            // un-comment or comment this line to show steps or not

//////////////////////////////////////////NETWORKING///////////////////////////////////////////////
#include<bits/stdc++.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <unistd.h>
#include <arpa/inet.h>
#define lli long long 

using namespace std;

#define SERVER_PORT htons(50007)



// global variables ///////////////////////////////////////////////////////////////////////////////
const cv::Scalar SCALAR_BLACK = cv::Scalar(0.0, 0.0, 0.0);

const cv::Scalar SCALAR_WHITE = cv::Scalar(255.0, 255.0, 255.0);
const cv::Scalar SCALAR_YELLOW = cv::Scalar(0.0, 255.0, 255.0);
const cv::Scalar SCALAR_GREEN = cv::Scalar(0.0, 200.0, 0.0);
const cv::Scalar SCALAR_RED = cv::Scalar(0.0, 0.0, 255.0);


///////////////////////////////////////////////////////////////////////////////////////////////////

class Blob {
public:
	// member variables ///////////////////////////////////////////////////////////////////////////
	std::vector<cv::Point> currentContour;

	cv::Rect currentBoundingRect;

	std::vector<cv::Point> centerPositions;

	double dblCurrentDiagonalSize;
	double dblCurrentAspectRatio;

	bool blnCurrentMatchFoundOrNewBlob;

	bool blnStillBeingTracked;

	int intNumOfConsecutiveFramesWithoutAMatch;

	cv::Point predictedNextPosition;

	// function prototypes ////////////////////////////////////////////////////////////////////////
	Blob(std::vector<cv::Point> _contour);
	void predictNextPosition(void);

};

/////////////////////////////////////////////////////////////////////////////////////////////////////


Blob::Blob(std::vector<cv::Point> _contour) {

	currentContour = _contour;

	currentBoundingRect = cv::boundingRect(currentContour);

	cv::Point currentCenter;

	currentCenter.x = (currentBoundingRect.x + currentBoundingRect.x + currentBoundingRect.width) / 2;
	currentCenter.y = (currentBoundingRect.y + currentBoundingRect.y + currentBoundingRect.height) / 2;

	centerPositions.push_back(currentCenter);

	dblCurrentDiagonalSize = sqrt(pow(currentBoundingRect.width, 2) + pow(currentBoundingRect.height, 2));

	dblCurrentAspectRatio = (float)currentBoundingRect.width / (float)currentBoundingRect.height;

	blnStillBeingTracked = true;
	blnCurrentMatchFoundOrNewBlob = true;

	intNumOfConsecutiveFramesWithoutAMatch = 0;
}

///////////////////////////////////////////////////////////////////////////////////////////////////
void Blob::predictNextPosition(void) {

	int numPositions = (int)centerPositions.size();

	if (numPositions == 1) {

		predictedNextPosition.x = centerPositions.back().x;
		predictedNextPosition.y = centerPositions.back().y;

	}
	else if (numPositions == 2) {

		int deltaX = centerPositions[1].x - centerPositions[0].x;
		int deltaY = centerPositions[1].y - centerPositions[0].y;

		predictedNextPosition.x = centerPositions.back().x + deltaX;
		predictedNextPosition.y = centerPositions.back().y + deltaY;

	}
	else if (numPositions == 3) {

		int sumOfXChanges = ((centerPositions[2].x - centerPositions[1].x) * 2) +
			((centerPositions[1].x - centerPositions[0].x) * 1);

		int deltaX = (int)std::round((float)sumOfXChanges / 3.0);

		int sumOfYChanges = ((centerPositions[2].y - centerPositions[1].y) * 2) +
			((centerPositions[1].y - centerPositions[0].y) * 1);

		int deltaY = (int)std::round((float)sumOfYChanges / 3.0);

		predictedNextPosition.x = centerPositions.back().x + deltaX;
		predictedNextPosition.y = centerPositions.back().y + deltaY;

	}
	else if (numPositions == 4) {

		int sumOfXChanges = ((centerPositions[3].x - centerPositions[2].x) * 3) +
			((centerPositions[2].x - centerPositions[1].x) * 2) +
			((centerPositions[1].x - centerPositions[0].x) * 1);

		int deltaX = (int)std::round((float)sumOfXChanges / 6.0);

		int sumOfYChanges = ((centerPositions[3].y - centerPositions[2].y) * 3) +
			((centerPositions[2].y - centerPositions[1].y) * 2) +
			((centerPositions[1].y - centerPositions[0].y) * 1);

		int deltaY = (int)std::round((float)sumOfYChanges / 6.0);

		predictedNextPosition.x = centerPositions.back().x + deltaX;
		predictedNextPosition.y = centerPositions.back().y + deltaY;

	}
	else if (numPositions >= 5) {

		int sumOfXChanges = ((centerPositions[numPositions - 1].x - centerPositions[numPositions - 2].x) * 4) +
			((centerPositions[numPositions - 2].x - centerPositions[numPositions - 3].x) * 3) +
			((centerPositions[numPositions - 3].x - centerPositions[numPositions - 4].x) * 2) +
			((centerPositions[numPositions - 4].x - centerPositions[numPositions - 5].x) * 1);

		int deltaX = (int)std::round((float)sumOfXChanges / 10.0);

		int sumOfYChanges = ((centerPositions[numPositions - 1].y - centerPositions[numPositions - 2].y) * 4) +
			((centerPositions[numPositions - 2].y - centerPositions[numPositions - 3].y) * 3) +
			((centerPositions[numPositions - 3].y - centerPositions[numPositions - 4].y) * 2) +
			((centerPositions[numPositions - 4].y - centerPositions[numPositions - 5].y) * 1);

		int deltaY = (int)std::round((float)sumOfYChanges / 10.0);

		predictedNextPosition.x = centerPositions.back().x + deltaX;
		predictedNextPosition.y = centerPositions.back().y + deltaY;

	}
	else {
		// should never get here
	}

}
// function prototypes ////////////////////////////////////////////////////////////////////////////
void matchCurrentFrameBlobsToExistingBlobs(std::vector<Blob> &existingBlobs, std::vector<Blob> &currentFrameBlobs);
void addBlobToExistingBlobs(Blob &currentFrameBlob, std::vector<Blob> &existingBlobs, int &intIndex);
void addNewBlob(Blob &currentFrameBlob, std::vector<Blob> &existingBlobs);
double distanceBetweenPoints(cv::Point point1, cv::Point point2);
void drawAndShowContours(cv::Size imageSize, std::vector<std::vector<cv::Point> > contours, std::string strImageName);
void drawAndShowContours(cv::Size imageSize, std::vector<Blob> blobs, std::string strImageName);
bool checkIfBlobsCrossedTheLine(std::vector<Blob> &blobs, int &intHorizontalLinePosition, int &carCount, int n, int serverSock, int clientSock);
void drawBlobInfoOnImage(std::vector<Blob> &blobs, cv::Mat &imgFrame2Copy);
void drawCarCountOnImage(int &carCount, cv::Mat &imgFrame2Copy);

char buffer[150];
char test[150];

string to_stringl(int x)
{
 	int temp=x;
	int Reverse=0;
	
	string s="";
	if (temp==0)
		s="0";
	while(temp)
	{
		s.push_back((char)(temp%10)+48);
		temp/=10;
	}  
	
	reverse(s.begin(),s.end());
	
 return s;
}

/////////////////////////////////////////////////////////////////////////////////////////////////////

int main(void) {

	cv::VideoCapture capVideo;

	cv::Mat imgFrame1;
	cv::Mat imgFrame2;

	std::vector<Blob> blobs;

	cv::Point crossingLine[2];

	int carCount = 0;

	capVideo.open("CarsDrivingUnderBridge.mp4");

	if (!capVideo.isOpened()) {                                                 // if unable to open video file
		std::cout << "error reading video file" << std::endl << std::endl;      // show error message
		//_getch();                   // it may be necessary to change or remove this line if not using Windows
		return(0);                                                              // and exit program
	}

	if (capVideo.get(CV_CAP_PROP_FRAME_COUNT) < 2) {
		std::cout << "error: video file must have at least two frames";
		//_getch();                   // it may be necessary to change or remove this line if not using Windows
		return(0);
	}

	capVideo.read(imgFrame1);
	capVideo.read(imgFrame2);

	int intHorizontalLinePosition = (int)std::round((double)imgFrame1.rows * 0.35);

	crossingLine[0].x = 0;
	crossingLine[0].y = intHorizontalLinePosition;

	crossingLine[1].x = imgFrame1.cols - 1;
	crossingLine[1].y = intHorizontalLinePosition;

	char chCheckForEscKey = 0;

	bool blnFirstFrame = true;

	int frameCount = 2;
	
/////////////////////////////////////////////////NETWORKING//////////////////////////////////////////////////////////
	
	

	int n;

        int serverSock=socket(AF_INET, SOCK_STREAM, 0);

        sockaddr_in serverAddr;
        serverAddr.sin_family = AF_INET;
        serverAddr.sin_port = SERVER_PORT;
        serverAddr.sin_addr.s_addr = INADDR_ANY;

        /* bind (this socket, local address, address length)
           bind server socket (serverSock) to server address (serverAddr).  
           Necessary so that server can use a specific port */ 
        bind(serverSock, (struct sockaddr*)&serverAddr, sizeof(struct sockaddr));

        // wait for a client
        /* listen (this socket, request queue length) */
        listen(serverSock,1);

	bzero(buffer, 150);

                sockaddr_in clientAddr;
                socklen_t sin_size=sizeof(struct sockaddr_in);
                int clientSock=accept(serverSock,(struct sockaddr*)&clientAddr, &sin_size);

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

	while (capVideo.isOpened() && chCheckForEscKey != 27) {

		std::vector<Blob> currentFrameBlobs;

		cv::Mat imgFrame1Copy = imgFrame1.clone();
		cv::Mat imgFrame2Copy = imgFrame2.clone();

		cv::Mat imgDifference;
		cv::Mat imgThresh;

		cv::cvtColor(imgFrame1Copy, imgFrame1Copy, CV_BGR2GRAY);
		cv::cvtColor(imgFrame2Copy, imgFrame2Copy, CV_BGR2GRAY);

		cv::GaussianBlur(imgFrame1Copy, imgFrame1Copy, cv::Size(5, 5), 0);
		cv::GaussianBlur(imgFrame2Copy, imgFrame2Copy, cv::Size(5, 5), 0);

		cv::absdiff(imgFrame1Copy, imgFrame2Copy, imgDifference);

		cv::threshold(imgDifference, imgThresh, 30, 255.0, CV_THRESH_BINARY);

		cv::imshow("imgThresh", imgThresh);

		cv::Mat structuringElement3x3 = cv::getStructuringElement(cv::MORPH_RECT, cv::Size(3, 3));
		cv::Mat structuringElement5x5 = cv::getStructuringElement(cv::MORPH_RECT, cv::Size(5, 5));
		cv::Mat structuringElement7x7 = cv::getStructuringElement(cv::MORPH_RECT, cv::Size(7, 7));
		cv::Mat structuringElement15x15 = cv::getStructuringElement(cv::MORPH_RECT, cv::Size(15, 15));

		for (unsigned int i = 0; i < 2; i++) {
			cv::dilate(imgThresh, imgThresh, structuringElement5x5);
			cv::dilate(imgThresh, imgThresh, structuringElement5x5);
			cv::erode(imgThresh, imgThresh, structuringElement5x5);
		}

		cv::Mat imgThreshCopy = imgThresh.clone();

		std::vector<std::vector<cv::Point> > contours;

		cv::findContours(imgThreshCopy, contours, cv::RETR_EXTERNAL, cv::CHAIN_APPROX_SIMPLE);

		drawAndShowContours(imgThresh.size(), contours, "imgContours");

		std::vector<std::vector<cv::Point> > convexHulls(contours.size());

		for (unsigned int i = 0; i < contours.size(); i++) {
			cv::convexHull(contours[i], convexHulls[i]);
		}

		drawAndShowContours(imgThresh.size(), convexHulls, "imgConvexHulls");

		for (auto &convexHull : convexHulls) {
			Blob possibleBlob(convexHull);

			if (possibleBlob.currentBoundingRect.area() > 400 &&
				possibleBlob.dblCurrentAspectRatio > 0.2 &&
				possibleBlob.dblCurrentAspectRatio < 4.0 &&
				possibleBlob.currentBoundingRect.width > 30 &&
				possibleBlob.currentBoundingRect.height > 30 &&
				possibleBlob.dblCurrentDiagonalSize > 60.0 &&
				(cv::contourArea(possibleBlob.currentContour) / (double)possibleBlob.currentBoundingRect.area()) > 0.50) {
				currentFrameBlobs.push_back(possibleBlob);
			}
		}

		drawAndShowContours(imgThresh.size(), currentFrameBlobs, "imgCurrentFrameBlobs");

		if (blnFirstFrame == true) {
			for (auto &currentFrameBlob : currentFrameBlobs) {
				blobs.push_back(currentFrameBlob);
			}
		}
		else {
			matchCurrentFrameBlobsToExistingBlobs(blobs, currentFrameBlobs);
		}

		drawAndShowContours(imgThresh.size(), blobs, "imgBlobs");

		imgFrame2Copy = imgFrame2.clone();          // get another copy of frame 2 since we changed the previous frame 2 copy in the processing above

		drawBlobInfoOnImage(blobs, imgFrame2Copy);

		bool blnAtLeastOneBlobCrossedTheLine = checkIfBlobsCrossedTheLine(blobs, intHorizontalLinePosition, carCount, n, serverSock, clientSock);

		if (blnAtLeastOneBlobCrossedTheLine == true) {
			cv::line(imgFrame2Copy, crossingLine[0], crossingLine[1], SCALAR_GREEN, 2);
		}
		else {
			cv::line(imgFrame2Copy, crossingLine[0], crossingLine[1], SCALAR_RED, 2);
		}

		drawCarCountOnImage(carCount, imgFrame2Copy);

		cv::imshow("imgFrame2Copy", imgFrame2Copy);

		//cv::waitKey(0);                 // uncomment this line to go frame by frame for debugging

		// now we prepare for the next iteration

		currentFrameBlobs.clear();

		imgFrame1 = imgFrame2.clone();           // move frame 1 up to where frame 2 is

		if ((capVideo.get(CV_CAP_PROP_POS_FRAMES) + 1) < capVideo.get(CV_CAP_PROP_FRAME_COUNT)) {
			capVideo.read(imgFrame2);
		}
		else {
			std::cout << "end of video\n";
			///////////////////////////////////////////////////////////////////////////////////////////////
			memset(buffer,0,sizeof(buffer));		
			memset(test,0,sizeof(test));
			int endx=0;			
			int endy=0;
			int curx=0;
			int cury=0;
			int state=0;
			int dirn=0;
			int startangle=0;
			int lane=0;
			int lanestate=0;
			int sf=0;
			/*int rand_start,rand_end;
			int ex,ey,sx,sy;
			srand((unsigned)time(0));
			do
			{
				rand_start=(rand() % 10);
				rand_end=(rand() % 10);
				lane=(rand() % 3)+1;
			}while(rand_start == rand_end);
			switch(rand_start)
			{
				case 0:sx=0;sy=1;dirn=3;
					switch(lane)
					{
					case 1:curx=233;cury=0;break;
					case 2:curx=248;cury=0;break;
					case 3:curx=263;cury=0;break;
					}			
					break;
				case 1:sx=0;sy=2;dirn=3;
					switch(lane)
					{
					case 1:curx=503;cury=0;break;
					case 2:curx=518;cury=0;break;
					case 3:curx=533;cury=0;break;
					}		
					break;
				case 2:sx=0;sy=3;dirn=3;
					switch(lane)
					{
					case 1:curx=773;cury=0;break;
					case 2:curx=788;cury=0;break;
					case 3:curx=803;cury=0;break;
					}		
					break;
				case 3:sx=1;sy=0;dirn=2;
					switch(lane)
					{
					case 3:curx=0;cury=187;break;
					case 2:curx=0;cury=202;break;
					case 1:curx=0;cury=217;break;
					}		
					break;
				case 4:sx=1;sy=4;dirn=4;
					switch(lane)
					{
					case 1:curx=990;cury=233;break;
					case 2:curx=990;cury=248;break;
					case 3:curx=990;cury=263;break;
					}			
					break;
				case 5:sx=2;sy=0;dirn=2;
					switch(lane)
					{
					case 3:curx=0;cury=457;break;
					case 2:curx=0;cury=472;break;
					case 1:curx=0;cury=487;break;
					}			
					break;
				case 6:sx=2;sy=4;dirn=4;
					switch(lane)
					{
					case 1:curx=990;cury=503;break;
					case 2:curx=990;cury=518;break;
					case 3:curx=990;cury=533;break;
					}			
					break;
				case 7:sx=3;sy=1;dirn=1;
					switch(lane)
					{
					case 3:curx=187;cury=720;break;
					case 2:curx=202;cury=720;break;
					case 1:curx=217;cury=720;break;
					}
					break;
				case 8:sx=3;sy=2;dirn=1;
					switch(lane)
					{
					case 3:curx=457;cury=720;break;
					case 2:curx=472;cury=720;break;
					case 1:curx=487;cury=720;break;
					}			
					break;
				case 9:sx=3;sy=3;dirn=1;
					switch(lane)
					{
					case 3:curx=727;cury=720;break;
					case 2:curx=742;cury=720;break;
					case 1:curx=757;cury=720;break;
					}			
					break;	
			}
			switch(rand_end)
			{
				case 0:ex=0;ey=1;
					switch(lane)
					{
					case 3:endx=187;endy=0;break;
					case 2:endx=202;endy=0;break;
					case 1:endx=217;endy=0;break;
					}			
					break;
				case 1:ex=0;ey=2;
					switch(lane)
					{
					case 3:endx=457;endy=0;break;
					case 2:endx=472;endy=0;break;
					case 1:endx=487;endy=0;break;
					}			
					break;
				case 2:ex=0;ey=3;
					switch(lane)
					{
					case 3:endx=727;endy=0;break;
					case 2:endx=742;endy=0;break;
					case 1:endx=757;endy=0;break;
					}			
					break;
				case 3:ex=1;ey=0;
					switch(lane)
					{
					case 1:endx=0;endy=233;break;
					case 2:endx=0;endy=248;break;
					case 3:endx=0;endy=263;break;
					}
					break;
				case 4:ex=1;ey=4;
					switch(lane)
					{
					case 3:endx=990;endy=187;break;
					case 2:endx=990;endy=202;break;
					case 1:endx=990;endy=217;break;
					}			
					break;
				case 5:ex=2;ey=0;
					switch(lane)
					{
					case 1:endx=0;endy=503;break;
					case 2:endx=0;endy=518;break;
					case 3:endx=0;endy=533;break;
					}			
					break;
				case 6:ex=2;ey=4;
					switch(lane)
					{
					case 3:endx=990;endy=457;break;
					case 2:endx=990;endy=472;break;
					case 1:endx=990;endy=487;break;
					}
					break;
				case 7:ex=3;ey=1;
					switch(lane)
					{
					case 1:endx=233;endy=720;break;
					case 2:endx=248;endy=720;break;
					case 3:endx=263;endy=720;break;
					}
					break;
				case 8:ex=3;ey=2;
					switch(lane)
					{
					case 1:endx=503;endy=720;break;
					case 2:endx=518;endy=720;break;
					case 3:endx=533;endy=720;break;
					}
					break;
				case 9:ex=3;ey=3;
					switch(lane)
					{
					case 1:endx=773;endy=720;break;
					case 2:endx=788;endy=720;break;
					case 3:endx=803;endy=720;break;
					}
					break;	
			}*/
			//cout<<sx<<"\t"<<sy<<"\t"<<ex<<"\t"<<ey<<endl;
	
			int path[4][5]={
					0,0,0,0,0,
					0, 0 , 0 , 0 ,0,
					0, 0 , 0 , 0 ,0,
					0,0,0,0,0
					};
			//path[ex][ey]=0;
			/*for(int i=0;i<4;i++)
			{	
				for(int j=0;j<5;j++)
				{
					if(path[i][j]==200)
						path[i][j]=200;
					else
						path[i][j]=abs(ex-i)+abs(ey-j);
				
				}
			}*/
	

			string s,s_endx,s_endy,s_curx,s_cury,s_state,s_dirn,s_startangle,s_lane,s_lanestate,s_sf;
			s_endx=to_stringl(endx);
			s_endy=to_stringl(endy);
			s_curx=to_stringl(curx);
			s_cury=to_stringl(cury);
			s_state=to_stringl(state);
			s_dirn=to_stringl(dirn);
			s_startangle=to_stringl(startangle);
			s_lane=to_stringl(lane);
			s_lanestate=to_stringl(lanestate);
			s_sf=to_stringl(sf);

			//cout<<s<<"\t"<<s1<<endl;
			s+=s_endx;s+="/";
			s+=s_endy;s+="/";
			s+=s_curx;s+="/";
			s+=s_cury;s+="/";
			s+=s_state;s+="/";
			s+=s_dirn;s+="/";
			s+=s_startangle;s+="/";
			s+=s_lane;s+="/";
			s+=s_lanestate;s+="/";
			s+=s_sf;	
			s+="*";
			for(int i=0;i<4;i++)
				{
				string tem;
				for(int j=0;j<5;j++)
					{
					tem=to_stringl(path[i][j]);
					s+=tem;
					if(j<4)
						s+="/";
					cout<<path[i][j]<<"\t";
					}
				s+="*";
				cout<<"\n";
				} 
	
			cout<<s<<endl;
			for(int i=0;i<s.length();i++)
			{
			     test[i]=s[i];
			//	cout<<test[i]<<"\t"<<endl;
			}	


		/*	strcat(test,ar);
			strcat(test,"/");*/
	
			//strcpy(buffer,test);
			cout<<test<<endl;
		

				//receive a message from a client
				n = read(clientSock, buffer, 75);
				cout << "Confirmation code  " << n << endl;
				cout << "Server received:  " << buffer << endl;

				strcpy(buffer, test);
				n = write(clientSock, buffer, strlen(buffer));
				cout << "Confirmation code  " << n << endl;
			///////////////////////////////////////////////////////////////////////////////////////////////				
			//break;
		}

		blnFirstFrame = false;
		frameCount++;
		chCheckForEscKey = cv::waitKey(1);
	}

	if (chCheckForEscKey != 27) {               // if the user did not press esc (i.e. we reached the end of the video)
		cv::waitKey(0);                         // hold the windows open to allow the "end of video" message to show
	}
	// note that if the user did press esc, we don't need to hold the windows open, we can simply let the program end which will close the windows

	return(0);
}

///////////////////////////////////////////////////////////////////////////////////////////////////
void matchCurrentFrameBlobsToExistingBlobs(std::vector<Blob> &existingBlobs, std::vector<Blob> &currentFrameBlobs) {

	for (auto &existingBlob : existingBlobs) {

		existingBlob.blnCurrentMatchFoundOrNewBlob = false;

		existingBlob.predictNextPosition();
	}

	for (auto &currentFrameBlob : currentFrameBlobs) {

		int intIndexOfLeastDistance = 0;
		double dblLeastDistance = 100000.0;

		for (unsigned int i = 0; i < existingBlobs.size(); i++) {

			if (existingBlobs[i].blnStillBeingTracked == true) {

				double dblDistance = distanceBetweenPoints(currentFrameBlob.centerPositions.back(), existingBlobs[i].predictedNextPosition);

				if (dblDistance < dblLeastDistance) {
					dblLeastDistance = dblDistance;
					intIndexOfLeastDistance = i;
				}
			}
		}

		if (dblLeastDistance < currentFrameBlob.dblCurrentDiagonalSize * 0.5) {
			addBlobToExistingBlobs(currentFrameBlob, existingBlobs, intIndexOfLeastDistance);
		}
		else {
			addNewBlob(currentFrameBlob, existingBlobs);
		}

	}

	for (auto &existingBlob : existingBlobs) {

		if (existingBlob.blnCurrentMatchFoundOrNewBlob == false) {
			existingBlob.intNumOfConsecutiveFramesWithoutAMatch++;
		}

		if (existingBlob.intNumOfConsecutiveFramesWithoutAMatch >= 5) {
			existingBlob.blnStillBeingTracked = false;
		}

	}

}

///////////////////////////////////////////////////////////////////////////////////////////////////
void addBlobToExistingBlobs(Blob &currentFrameBlob, std::vector<Blob> &existingBlobs, int &intIndex) {

	existingBlobs[intIndex].currentContour = currentFrameBlob.currentContour;
	existingBlobs[intIndex].currentBoundingRect = currentFrameBlob.currentBoundingRect;

	existingBlobs[intIndex].centerPositions.push_back(currentFrameBlob.centerPositions.back());

	existingBlobs[intIndex].dblCurrentDiagonalSize = currentFrameBlob.dblCurrentDiagonalSize;
	existingBlobs[intIndex].dblCurrentAspectRatio = currentFrameBlob.dblCurrentAspectRatio;

	existingBlobs[intIndex].blnStillBeingTracked = true;
	existingBlobs[intIndex].blnCurrentMatchFoundOrNewBlob = true;
}

///////////////////////////////////////////////////////////////////////////////////////////////////
void addNewBlob(Blob &currentFrameBlob, std::vector<Blob> &existingBlobs) {

	currentFrameBlob.blnCurrentMatchFoundOrNewBlob = true;

	existingBlobs.push_back(currentFrameBlob);
}

///////////////////////////////////////////////////////////////////////////////////////////////////
double distanceBetweenPoints(cv::Point point1, cv::Point point2) {

	int intX = abs(point1.x - point2.x);
	int intY = abs(point1.y - point2.y);

	return(sqrt(pow(intX, 2) + pow(intY, 2)));
}

///////////////////////////////////////////////////////////////////////////////////////////////////
void drawAndShowContours(cv::Size imageSize, std::vector<std::vector<cv::Point> > contours, std::string strImageName) {
	cv::Mat image(imageSize, CV_8UC3, SCALAR_BLACK);

	cv::drawContours(image, contours, -1, SCALAR_WHITE, -1);

	cv::imshow(strImageName, image);
}

///////////////////////////////////////////////////////////////////////////////////////////////////
void drawAndShowContours(cv::Size imageSize, std::vector<Blob> blobs, std::string strImageName) {

	cv::Mat image(imageSize, CV_8UC3, SCALAR_BLACK);

	std::vector<std::vector<cv::Point> > contours;

	for (auto &blob : blobs) {
		if (blob.blnStillBeingTracked == true) {
			contours.push_back(blob.currentContour);
		}
	}

	cv::drawContours(image, contours, -1, SCALAR_WHITE, -1);

	cv::imshow(strImageName, image);
}

///////////////////////////////////////////////////////////////////////////////////////////////////
bool checkIfBlobsCrossedTheLine(std::vector<Blob> &blobs, int &intHorizontalLinePosition, int &carCount, int n, int serverSock, int clientSock) {
	bool blnAtLeastOneBlobCrossedTheLine = false;

	for (auto blob : blobs) {

		if (blob.blnStillBeingTracked == true && blob.centerPositions.size() >= 2) {
			int prevFrameIndex = (int)blob.centerPositions.size() - 2;
			int currFrameIndex = (int)blob.centerPositions.size() - 1;

			if (blob.centerPositions[prevFrameIndex].y > intHorizontalLinePosition && blob.centerPositions[currFrameIndex].y <= intHorizontalLinePosition) {
				carCount++;
				//////////////////////////////////////////////////////////////
			memset(buffer,0,sizeof(buffer));		
			memset(test,0,sizeof(test));
			int endx;			
			int endy;
			int curx;
			int cury;
			int state=1;
			int dirn;
			int startangle=0;
			int lane;
			int lanestate=0;
			int sf=0;
			int rand_start,rand_end;
			int ex,ey,sx,sy;
			srand((unsigned)time(0));
			do
			{
				rand_start=(rand() % 10);
				rand_end=(rand() % 10);
				lane=(rand() % 3)+1;
			}while(rand_start == rand_end);
			switch(rand_start)
			{
				case 0:sx=0;sy=1;dirn=3;
					switch(lane)
					{
					case 1:curx=233;cury=0;break;
					case 2:curx=248;cury=0;break;
					case 3:curx=263;cury=0;break;
					}			
					break;
				case 1:sx=0;sy=2;dirn=3;
					switch(lane)
					{
					case 1:curx=503;cury=0;break;
					case 2:curx=518;cury=0;break;
					case 3:curx=533;cury=0;break;
					}		
					break;
				case 2:sx=0;sy=3;dirn=3;
					switch(lane)
					{
					case 1:curx=773;cury=0;break;
					case 2:curx=788;cury=0;break;
					case 3:curx=803;cury=0;break;
					}		
					break;
				case 3:sx=1;sy=0;dirn=2;
					switch(lane)
					{
					case 3:curx=0;cury=187;break;
					case 2:curx=0;cury=202;break;
					case 1:curx=0;cury=217;break;
					}		
					break;
				case 4:sx=1;sy=4;dirn=4;
					switch(lane)
					{
					case 1:curx=990;cury=233;break;
					case 2:curx=990;cury=248;break;
					case 3:curx=990;cury=263;break;
					}			
					break;
				case 5:sx=2;sy=0;dirn=2;
					switch(lane)
					{
					case 3:curx=0;cury=457;break;
					case 2:curx=0;cury=472;break;
					case 1:curx=0;cury=487;break;
					}			
					break;
				case 6:sx=2;sy=4;dirn=4;
					switch(lane)
					{
					case 1:curx=990;cury=503;break;
					case 2:curx=990;cury=518;break;
					case 3:curx=990;cury=533;break;
					}			
					break;
				case 7:sx=3;sy=1;dirn=1;
					switch(lane)
					{
					case 3:curx=187;cury=720;break;
					case 2:curx=202;cury=720;break;
					case 1:curx=217;cury=720;break;
					}
					break;
				case 8:sx=3;sy=2;dirn=1;
					switch(lane)
					{
					case 3:curx=457;cury=720;break;
					case 2:curx=472;cury=720;break;
					case 1:curx=487;cury=720;break;
					}			
					break;
				case 9:sx=3;sy=3;dirn=1;
					switch(lane)
					{
					case 3:curx=727;cury=720;break;
					case 2:curx=742;cury=720;break;
					case 1:curx=757;cury=720;break;
					}			
					break;	
			}
			switch(rand_end)
			{
				case 0:ex=0;ey=1;
					switch(lane)
					{
					case 3:endx=187;endy=0;break;
					case 2:endx=202;endy=0;break;
					case 1:endx=217;endy=0;break;
					}			
					break;
				case 1:ex=0;ey=2;
					switch(lane)
					{
					case 3:endx=457;endy=0;break;
					case 2:endx=472;endy=0;break;
					case 1:endx=487;endy=0;break;
					}			
					break;
				case 2:ex=0;ey=3;
					switch(lane)
					{
					case 3:endx=727;endy=0;break;
					case 2:endx=742;endy=0;break;
					case 1:endx=757;endy=0;break;
					}			
					break;
				case 3:ex=1;ey=0;
					switch(lane)
					{
					case 1:endx=0;endy=233;break;
					case 2:endx=0;endy=248;break;
					case 3:endx=0;endy=263;break;
					}
					break;
				case 4:ex=1;ey=4;
					switch(lane)
					{
					case 3:endx=990;endy=187;break;
					case 2:endx=990;endy=202;break;
					case 1:endx=990;endy=217;break;
					}			
					break;
				case 5:ex=2;ey=0;
					switch(lane)
					{
					case 1:endx=0;endy=503;break;
					case 2:endx=0;endy=518;break;
					case 3:endx=0;endy=533;break;
					}			
					break;
				case 6:ex=2;ey=4;
					switch(lane)
					{
					case 3:endx=990;endy=457;break;
					case 2:endx=990;endy=472;break;
					case 1:endx=990;endy=487;break;
					}
					break;
				case 7:ex=3;ey=1;
					switch(lane)
					{
					case 1:endx=233;endy=720;break;
					case 2:endx=248;endy=720;break;
					case 3:endx=263;endy=720;break;
					}
					break;
				case 8:ex=3;ey=2;
					switch(lane)
					{
					case 1:endx=503;endy=720;break;
					case 2:endx=518;endy=720;break;
					case 3:endx=533;endy=720;break;
					}
					break;
				case 9:ex=3;ey=3;
					switch(lane)
					{
					case 1:endx=773;endy=720;break;
					case 2:endx=788;endy=720;break;
					case 3:endx=803;endy=720;break;
					}
					break;	
			}
			cout<<sx<<"\t"<<sy<<"\t"<<ex<<"\t"<<ey<<endl;
	
			int path[4][5]={
					200,200,200,200,200,
					200, 1 , 1 , 1 ,200,
					200, 1 , 1 , 1 ,200,
					200,200,200,200,200
					};
			path[ex][ey]=0;
			for(int i=0;i<4;i++)
			{	
				for(int j=0;j<5;j++)
				{
					if(path[i][j]==200)
						path[i][j]=200;
					else
						path[i][j]=abs(ex-i)+abs(ey-j);
				
				}
			}
	

			string s,s_endx,s_endy,s_curx,s_cury,s_state,s_dirn,s_startangle,s_lane,s_lanestate,s_sf;
			s_endx=to_stringl(endx);
			s_endy=to_stringl(endy);
			s_curx=to_stringl(curx);
			s_cury=to_stringl(cury);
			s_state=to_stringl(state);
			s_dirn=to_stringl(dirn);
			s_startangle=to_stringl(startangle);
			s_lane=to_stringl(lane);
			s_lanestate=to_stringl(lanestate);
			s_sf=to_stringl(sf);

			//cout<<s<<"\t"<<s1<<endl;
			s+=s_endx;s+="/";
			s+=s_endy;s+="/";
			s+=s_curx;s+="/";
			s+=s_cury;s+="/";
			s+=s_state;s+="/";
			s+=s_dirn;s+="/";
			s+=s_startangle;s+="/";
			s+=s_lane;s+="/";
			s+=s_lanestate;s+="/";
			s+=s_sf;	
			s+="*";
			for(int i=0;i<4;i++)
				{
				string tem;
				for(int j=0;j<5;j++)
					{
					tem=to_stringl(path[i][j]);
					s+=tem;
					if(j<4)
						s+="/";
					cout<<path[i][j]<<"\t";
					}
				s+="*";
				cout<<"\n";
				} 
	
			cout<<s<<endl;
			for(int i=0;i<s.length();i++)
			{
			     test[i]=s[i];
			//	cout<<test[i]<<"\t"<<endl;
			}	


		/*	strcat(test,ar);
			strcat(test,"/");*/
	
			//strcpy(buffer,test);
			cout<<test<<endl;
		

				//receive a message from a client
				n = read(clientSock, buffer, 75);
				cout << "Confirmation code  " << n << endl;
				cout << "Server received:  " << buffer << endl;

				strcpy(buffer, test);
				n = write(clientSock, buffer, strlen(buffer));
				cout << "Confirmation code  " << n << endl;
				//////////////////////////////////////////////////////////////
				blnAtLeastOneBlobCrossedTheLine = true;
			}
		}

	}

	return blnAtLeastOneBlobCrossedTheLine;
}

///////////////////////////////////////////////////////////////////////////////////////////////////
void drawBlobInfoOnImage(std::vector<Blob> &blobs, cv::Mat &imgFrame2Copy) {

	for (unsigned int i = 0; i < blobs.size(); i++) {

		if (blobs[i].blnStillBeingTracked == true) {
			cv::rectangle(imgFrame2Copy, blobs[i].currentBoundingRect, SCALAR_RED, 2);

			int intFontFace = CV_FONT_HERSHEY_SIMPLEX;
			double dblFontScale = blobs[i].dblCurrentDiagonalSize / 60.0;
			int intFontThickness = (int)std::round(dblFontScale * 1.0);

			cv::putText(imgFrame2Copy, std::to_string(i), blobs[i].centerPositions.back(), intFontFace, dblFontScale, SCALAR_GREEN, intFontThickness);
		}
	}
}

///////////////////////////////////////////////////////////////////////////////////////////////////
void drawCarCountOnImage(int &carCount, cv::Mat &imgFrame2Copy) {

	int intFontFace = CV_FONT_HERSHEY_SIMPLEX;
	double dblFontScale = (imgFrame2Copy.rows * imgFrame2Copy.cols) / 300000.0;
	int intFontThickness = (int)std::round(dblFontScale * 1.5);

	cv::Size textSize = cv::getTextSize(std::to_string(carCount), intFontFace, dblFontScale, intFontThickness, 0);

	cv::Point ptTextBottomLeftPosition;

	ptTextBottomLeftPosition.x = imgFrame2Copy.cols - 1 - (int)((double)textSize.width * 1.25);
	ptTextBottomLeftPosition.y = (int)((double)textSize.height * 1.25);

	cv::putText(imgFrame2Copy, std::to_string(carCount), ptTextBottomLeftPosition, intFontFace, dblFontScale, SCALAR_GREEN, intFontThickness);

}

//////////////////////////////////////////////////////////////////////////////////////////////////////










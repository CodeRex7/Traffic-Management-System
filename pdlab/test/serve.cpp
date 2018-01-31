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
//int counter = 0;
string to_string(int x)
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

void draw();

int main() {
		char buffer[1000];
	char test[1000];
	

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

bzero(buffer, 1000);

                sockaddr_in clientAddr;
                socklen_t sin_size=sizeof(struct sockaddr_in);
                int clientSock=accept(serverSock,(struct sockaddr*)&clientAddr, &sin_size);
	

        while (1 == 1) {
                /*char endx[5]="500";
	char endy[5]="0";
	char curx[5]="0";
	char cury[5]="280";
	char state[5]="1";
	char dirn[5]="2";
	char startangle[5]="1";
	char lane[5]="2";
	char lane_state[5]="1";*/
	
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
	s_endx=to_string(endx);
	s_endy=to_string(endy);
	s_curx=to_string(curx);
	s_cury=to_string(cury);
	s_state=to_string(state);
	s_dirn=to_string(dirn);
	s_startangle=to_string(startangle);
	s_lane=to_string(lane);
	s_lanestate=to_string(lanestate);
	s_sf=to_string(sf);

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
	s+="//";
	for(int i=0;i<4;i++)
		{
		string tem;
		for(int j=0;j<5;j++)
			{
			tem=to_string(path[i][j]);
			s+=tem;
			if(j!=4)
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
                n = read(clientSock, buffer, 500);
                cout << "Confirmation code  " << n << endl;
                cout << "Server received:  " << buffer << endl;

                strcpy(buffer, test);
                n = write(clientSock, buffer, strlen(buffer));
                cout << "Confirmation code  " << n << endl;
        }

	
	
                return 0;
}

	


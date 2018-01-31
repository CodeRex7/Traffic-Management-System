#include <sys/socket.h>
#include <arpa/inet.h>

// this is our proto of foo
#include "foo.pb.h"

int main(int argc, char **argv)
{
  struct sockaddr_in addr;

  addr.sin_family = AF_INET;
  inet_aton("127.0.0.1", &addr.sin_addr);
  addr.sin_port = htons(5555);

  // initialise a foo and set some properties
  GOOGLE_PROTOBUF_VERIFY_VERSION;
  prototest::Foo foo;
  foo.set_id(4);
  foo.set_bar("narf");

  // serialise to string, this one is obvious ; )    
  std::string buf;
  foo.SerializeToString(&buf);

  int sock = socket(PF_INET, SOCK_DGRAM, 0);
  sendto(sock, buf.data(), buf.size(), 0, (struct sockaddr *)&addr, sizeof(addr));

  return 0;
}

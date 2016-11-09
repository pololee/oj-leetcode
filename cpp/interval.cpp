

[0, 1, 2, 50, 52, 75]


"3-49,51,53-74,76-99"
#include<iostream>
#include<string>
#include<vector>

string GetMissingInteval(const vector<int> &vec)
{
  string result;
  std::vector<int>::iterator it=vec.begin();
  if(*it != 0 ){
    if(*it == 1)
      result = result + "0,";
    else {
      result = result + "0-";
      result = result + ('0'+ (*it-1));
      result = result + ","
    }
  }
  it++;
  for( ;it!=vec.end(); it++){
    int dis = *(it) - *(it-1);
    if(dis == 2){
      result = result + ('0'+(*(it-1) + 1));
      result = result + ',';
    } else if(dis > 2) {
      result = result + ('0'+(*(it-1) + 1));
      result = result + '-';
      result = result + ('0'+(*it - 1));
      result = result + ',';
    }
  }
  if(*it < 98){
    result = result + ('0'+(*it +1));
    result = result + '-';
    result = result + "99";
  } else if (*it == 98) {
    result = result + "99";
  } else {
    result = result.substr(0, result.size()-1);
  }
  return result;
}

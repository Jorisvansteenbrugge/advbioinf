#include <iostream>
#include <sparsehash/dense_hash_map>
#include <tr1/functional>
#include <string.h>

using google::dense_hash_map;
using std::cout;
using std::endl;
using std::tr1::hash;

struct eqstr{
    bool operator()(const char* s1, const char* s2) const{
        return (s1 == s2) || (s1 && s2 && strcmp(s1,s2) == 0);
    }
};

int main(){
    dense_hash_map<const char*, int, hash<const char*>, eqstr> months;

    months.set_empty_key(NULL);
    months["january"] = 31;

    cout << "january -> " << months["september"] << endl;
}

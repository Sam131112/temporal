#include "stdafx.h"
#include<iostream>
#include<fstream>
using namespace std;
#include<math.h>


void PrintGraphStat(const PUNGraph& G) {
  int FullDiam;
  double EffDiam;
  TSnap::GetBfsEffDiam(G, 1000, false, EffDiam, FullDiam);
  printf("%d", FullDiam);
  //printf("90-percentile effective diameter\t%.2g\n", EffDiam);
}
  


int main(int argc, char* argv[]) {


Env = TEnv(argc, argv, TNotify::StdNotify);
  //const TStr InFNm = Env.GetIfArgPrefixStr("-i:", "../as20graph.txt", "Input un/directed graph");
  //const TStr OutFNm = Env.GetIfArgPrefixStr("-o:", "node_centrality.tab", "Output file");
  const TStr InFNm = argv[2];
  //printf("Loading %s...", InFNm.CStr());
  PNGraph Graph = TSnap::LoadEdgeList<PNGraph>(InFNm);
  //PNGraph Graph = TSnap::GenRndGnm<PNGraph>(10, 10);
  //TGraphViz::Plot(Graph, gvlNeato, InFNm+".gif", InFNm, true);
  //printf("nods:%d  edges:%d\n", Graph->GetNodes(), Graph->GetEdges());
  PUNGraph UGraph = TSnap::ConvertGraph<PUNGraph>(Graph); // undirected version of the graph 
  //printf("nodes:%d  edges:%d\n", UGraph->GetNodes(), UGraph->GetEdges());
  //PrintGraphStat(UGraph);a


TIntV Ns;
int temp;
ifstream seed;
seed.open(argv[1]);
if(seed.is_open())
        {
                while(seed>>temp)
                        {
                                Ns.Add(temp);
                        }

        }
  for(int i=0;i<Ns.Len();i++)
		{
				if(UGraph->IsNode(Ns[i].Val))
					{
						UGraph->DelNode(Ns[i].Val);
					}

		}
/*
  for(int i=0;i<Ns.Len();i++)
                {
			try {
			printf("%d\n",Ns[i].Val);
                       UGraph->DelNode(Ns[i].Val);
			}
			catch(exception& e) {
			}

                } */
  //printf("nodes:%d  edges:%d\n", UGraph->GetNodes(), UGraph->GetEdges());
  //printf("%d ",Ns.Len()); 
  //TSnap::DelNodes(UGraph,Ns);
  PrintGraphStat(UGraph);
  return 0;
}

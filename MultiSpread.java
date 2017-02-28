/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
import java.io.*;
import java.util.*;

/**
 *
 * @author Soumya
 */
public class MultiSpread {

    public static class Node {

        int id = 0;
        double src = 0;
        ArrayList<Integer> neighbor = new ArrayList<Integer>();
    }

    public static void main(String args[]) throws FileNotFoundException, IOException {


        String[] kinds = {"close"};
        for (String kind : kinds)     {
            //System.out.println(kind);

        int size = Integer.parseInt(args[0]);
	int no_of_nodes = size;
	String test = args[1];
	Set<Integer> myset = new HashSet<Integer>();
	Map<Integer,Integer> mymap = new HashMap<Integer,Integer>();
	Map<Integer,Integer> revmap = new HashMap<Integer,Integer>();
	String[] temp;String strLine;
	try {
                FileInputStream fs = new FileInputStream(test);
                DataInputStream in = new DataInputStream(fs);
             
                //System.out.println(i);
                BufferedReader br = new BufferedReader(new InputStreamReader(in));
                while ((strLine = br.readLine()) != null) {
                    //System.out.println(strLine);
                    temp = strLine.split(" ");
                    myset.add(Integer.parseInt(temp[0]));
		    myset.add(Integer.parseInt(temp[1]));
                }   
                fs.close();
		//System.out.println("My set is is "+myset.size());
		//System.out.println("My network size is "+ size);
		

            } catch (Exception e) {
                System.out.println("here in the 1st exception ");
                System.out.println("Error is: " + e);
            }
	int n_id = 0;
	for(Integer ins:myset)
		{
			mymap.put(ins,n_id);
			revmap.put(n_id,ins);
			n_id = n_id+1;
			
		}
	/*
		printing the hashmap here
		for(Integer i:mymap.keySet())
		{
			System.out.println(i+" : "+mymap.get(i));
		}
	*/
	//System.out.println("Map Size is " + mymap.size());
	//System.out.println("Counter is "+n_id);	
		
	Set<Integer> seed_set = new HashSet<Integer>();
		String seeds = "seed_" + kind + ".txt";
		ArrayList<Integer> sources = new ArrayList<Integer>();
                   //System.out.println("Going for " + seeds);
		try {
                    FileInputStream fs = new FileInputStream(seeds);
                    DataInputStream in = new DataInputStream(fs);
                    BufferedReader br = new BufferedReader(new InputStreamReader(in));
                    while ((strLine = br.readLine()) != null) {
                            seed_set.add(Integer.parseInt(strLine));
			    if (mymap.get(Integer.parseInt(strLine)) !=null) {
			    sources.add(mymap.get(Integer.parseInt(strLine)));
				}
                    }
		  fs.close();
		 } catch (Exception e) {
                System.out.println("here in the 2nd exception ");
                System.out.println("Error is: " + e);
			}
		
	  //System.out.println("Seed Sets ");
	   //System.out.println(seed_set);
	   //System.out.println(sources);
           
            Node[] nod = new Node[no_of_nodes];
            for (int i = 0; i < no_of_nodes; i++) {
                nod[i] = new Node();
            }
            for (int i = 0; i < no_of_nodes; i++) {
                nod[i].id = i;
                nod[i].src = 0;
            }
	    for(Integer x:sources)
		{
			nod[x].src = 1;
		}
            //System.out.println("Reading the network file " +test);
            try {
                FileInputStream fs = new FileInputStream(test);
                /* int i = 0;
                
                while((i = fs.read()) != -1)
                {
                    char c=(char)i;
                    System.out.println(c);
                }*/
                DataInputStream in = new DataInputStream(fs);
                
                //System.out.println(i);
                BufferedReader br = new BufferedReader(new InputStreamReader(in));
                while ((strLine = br.readLine()) != null) {
                    //System.out.println(strLine);
                    temp = strLine.split(" ");
		    //System.out.println(temp[0]+" "+temp[1]);
		    int id1 = Integer.parseInt(temp[0]);
		    int id2 = Integer.parseInt(temp[1]);
		    //System.out.println(id1+" "+id2);
		     if (id1 == id2)
			continue;
                    /*
                    for ( String x : temp)
                    {
                        //System.out.println(x);
                    }*/
                    nod[mymap.get(id1)].neighbor.add(mymap.get(id2));
                    nod[mymap.get(id2)].neighbor.add(mymap.get(id1));
                }
                fs.close();

            } catch (Exception e) {
		System.out.println("here in the 3rd exception ");
                System.out.println("Error is: " + e);
            } /*
	     for(int i=0;i<5;i++)
			{
				System.out.println(i+"Neighbors of " + revmap.get(i)+" are");
				for(Integer ns:nod[i].neighbor)
					{
						System.out.print(revmap.get(ns)+"  ");
					}
				System.out.println();
			} */
            //System.out.println("THe Network is now ready");
	    //System.out.println(nod.length);
            int sims = 1;
            int lls = 20;
	    ArrayList<Double> std = new ArrayList<Double>();
            double s_r = 0.0;
            for (int sim = 0; sim < sims; sim++) {
                double total_r = 0.0;
                for (int ll = 0; ll < lls; ll++) {
		    double tmp = 0;
                    ArrayList<Integer> source = new ArrayList<Integer>();
		    ArrayList<Integer> check = new ArrayList<Integer>();
		    for(int nodeid = 0;nodeid<no_of_nodes;nodeid++)
				{
					if (sources.contains(nodeid))
						{
							nod[nodeid].src = 1;
							check.add(nodeid);
						}
					else	{
							nod[nodeid].src = 0;
						}
				
				}
		   /* for(Integer sd: seed_set)
			{
				System.out.print(mymap.get(sd)+ " ");
			}
		    System.out.println();
		    System.out.println(sources);
		    System.out.println(check);
		    System.out.println();*/
		    for(Integer sr:sources)
			{
				source.add(sr);
			}
		    
                    ArrayList<Integer> intm = new ArrayList<Integer>();
                    int minimum = 0;
                    int maximum = no_of_nodes;
                    int round = 0;
                    /*
                    for (Integer a : source)
                    {
                        System.out.print(a+" ");
                    }*/
                    //System.out.println(source.size());
                    Random rn = new Random();
		    int count =  0;
	            double n1 = no_of_nodes*1;
                    while (source.size() < n1) {
                        count = count + 1;
			//System.out.println(source.size());
                        for (int i = 0; i < source.size(); i++) {
                            int m = source.get(i);
			    //System.out.println("Inside calc ");
			    //System.out.println(nod[m].neighbor.size()+" "+revmap.get(m)+" "+source.size());
                            minimum = 0;
                            maximum = nod[m].neighbor.size() - 1;
                            int range = maximum - minimum + 1;
                            int randomNum = rn.nextInt(range) + minimum;
                            int n = nod[m].neighbor.get(randomNum);
                            if (nod[n].src == 0) {
                                nod[n].src = 1;
                                intm.add(n);
                            }
 			}
                        
                        for (int i = 0; i < intm.size(); i++) {
                            int m = intm.get(i);
                            if (source.contains(m)) {
                                System.out.println("This should not print");
                                continue;
                            } else {
                                source.add(m);
                            }
                        }
                        intm.clear();
                        round++;
                        if (count > no_of_nodes*2)
                            break;
                //System.out.println(round + "\t" + source.size());
                    }
                    total_r += round;
		  std.add((double)round);
                } // simulation of a particular seed for 100 times
//                    System.out.println(sim + " " + total_r / lls);
                s_r += total_r / lls;
            } // simulation of the 10 different seed 
            System.out.print( s_r / sims + "\t");
	    System.out.print(sd(std));

         }// kinds

    }

	public static double mean (ArrayList<Double> table)
    {
        double total = 0.0;

        for ( int i= 0;i < table.size(); i++)
        {
            double currentNum = table.get(i);
            total+= currentNum;
        }
	//System.out.println("Mean is " + total/table.size());
        return total/table.size();
    }

    public static double sd (ArrayList<Double> table)
    {
        double mean= mean(table);
        double temp =0;
	//System.out.println("Size of List "+table.size());
	//System.out.println("Size of List "+table);
        for ( int i= 0; i <table.size(); i++)
        {
            temp= temp + Math.pow(table.get(i)-mean, 2);
        }

        return Math.sqrt(temp/table.size());
    }
   	

}

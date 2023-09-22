using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Graph{
	
	/// <summary>
	/// A class whose objects find the shortest path to traverse the graph using the annealing method
	/// </summary>
	public class Annealing{
		Dictionary<string, Dictionary<string, double>> Verteces;
		int T = 1100;
		double w = 0.9;
		int itter = 0;
		
		/// <summary>
		/// A constructor that initiates an Annealing object with the passed parameters
		/// </summary>
		/// <param name="Verteces - dictionary with graph"></param>
		/// <param name="T - initial annealing temperature"></param>
		/// <param name="w - temperature reduction factor"></param>
		public Annealing(Dictionary<string, Dictionary<string, double>> Verteces, int T, double w, int itter){
			this.Verteces = Verteces;
			this.T = T;
			this.w = w;
			this.itter = itter;
		}
		
		/// <summary>
		/// Simulated annealing algorithm
		/// </summary>
		/// <returns>A string with a path and its length</returns>
		public string GetPath(){
			int ArrayLength = Verteces.Count;
			string[] NowPath = new String[ArrayLength];
			Random rnd = new Random();
			
			int r = 0;
			foreach(var n in Verteces){
				NowPath[r] = n.Key;
				r++;
			}
			
			for (int i = NowPath.Length - 1; i >= 1; i--){
				int j = rnd.Next(i + 1);
  				var temp = NowPath[j];
   				NowPath[j] = NowPath[i];
   				NowPath[i] = temp;
			}
			
			for (int i = 0; i < itter; i++) {
				int	NowPathLength = GetPathLength(NowPath) + Convert.ToInt32(Verteces[NowPath[ArrayLength - 1]][NowPath[0]]);
				string[] NewPath = Swap(NowPath);
				int NewPathLength = GetPathLength(NewPath) + Convert.ToInt32(Verteces[NewPath[ArrayLength - 1]][NewPath[0]]);
				if(NewPathLength < NowPathLength){
					NowPathLength = NewPathLength;
				}
				else{
					double P = Math.Exp(-(NewPathLength - NowPathLength)/T);
					double P1 = rnd.NextDouble();
					if(P < P1){
						NowPath = NewPath;
					}			
				}	
				T = T*Convert.ToInt32(w);
			}
			string Path = "";
			for (int i = 0; i < NowPath.Length; i++){
				Path += NowPath[i] + " ";
			}
			Path += NowPath[0]; 
			return("Annealing Algorithm:\nShortest path: ( " + Path + " ) is equal: " + (GetPathLength(NowPath) + Convert.ToInt32(Verteces[NowPath[ArrayLength - 1]][NowPath[0]])));
		}
		
		/// <summary>
		/// Calculating path length from a sequence of vertices
		/// </summary>
		/// <param name="path -array of vertices"></param>
		/// <returns></returns>
		public int GetPathLength(string[] path){
			int count = 0;
			for (int i = 1; i < path.Length; i++) {
				count += Convert.ToInt32(Verteces[path[i-1]][path[i]]);
			}
			return(count);
		}
		
		/// <summary>
		/// Swap two vertices randomly
		/// </summary>
		/// <param name="path - array of vertices"></param>
		/// <returns> Processed array</returns>
		public string[] Swap(string[] path){
			Random rnd = new Random();
			int h = rnd.Next(path.Length);
			int z = rnd.Next(path.Length);
				if(h != z){
					string str = path[h];
					path[h] = path[z];
					path[z] = str;
				}
				else{
					Swap(path);
				}	
			return(path);
		}
	}
	
	/// <summary>
	/// Brute force all possible paths on the graph
	/// </summary>
	public class BruteForceGraph{ // not my code
		Dictionary<string, Dictionary<string, double>> Verteces;
		public BruteForceGraph(Dictionary<string, Dictionary<string, double>> Verteces){
			this.Verteces = Verteces;
			Console.WriteLine("All path options:");
		}
		string strr = "";
        int count = 0;
        string now = "";
        int sss = 0;
		public void Method(int[] a, int n, int l)
        {			
			int s = 0;
			string[] arr = new string[l];
        	foreach(var v in Verteces){
        		arr[s] = v.Key;
        		s++;
        	}
            for (int i = 0; i < l; i++)
            {
                int j;
                for (j = 0; j < n; j++)
                    if (a[j] == i + 1) break;
                if (j == n)
                {
                    a[n] = i + 1;
                    if (n < l - 1) Method(a, n + 1, l);
                    else
                    {
                    	for (int k = 0; k < l; k++){
                    		strr += (arr[a[k]-1] + " ");
                    		now = arr[a[k]-1];
                    		sss++;
                    		if (sss > 1){
                    			int g = strr.Split(' ').Length - 1;
                    			count += Convert.ToInt32(Verteces[strr.Split(' ')[g - 2]][now]);
                    		}
                    		
                    	}
                    	count += Convert.ToInt32(Verteces[now][strr.Split(' ')[0]]);
                    	strr += strr.Split(' ')[0];
                    	sss = 0;
                    	Console.WriteLine("Path " + strr + " is equal " + count);
                    	strr = "";
                    	count = 0;
                    }
                }
            }
        }
		
	}
	
	/// <summary>
	/// Dijkstra's algorithm
	/// </summary>
	public class Dijkstra{
		Graph gr;
		Dictionary<string, double> vek;
        Dictionary<string, string> slow;
        
		public Dijkstra(Graph obj){
			vek = new Dictionary<string, double>();
            slow = new  Dictionary<string, string>();
            gr = obj;
		}
        
		/// <summary>
		/// Finding the shortest path between two Verteces
		/// </summary>
		/// <param name="start - starting vertex"></param>
		/// <param name="end - final vertex"></param>
		/// <returns>Length of shortest path from start to end</returns>       
		public string GetDis(string start, string end){
        	Queue<string> q = new Queue <string>();
            if (gr.Verteces.ContainsKey(start) & gr.Verteces.ContainsKey(end)){
                vek.Add(start, 0);
                slow.Add(start, start);
                q.Enqueue(start);
                while (q.Count != 0){
                    foreach (var n in gr.Verteces[q.Peek()]){
                        if (!vek.ContainsKey(n.Key)){
                            vek.Add(n.Key, n.Value + vek[q.Peek()]);
                            slow.Add(n.Key, q.Peek());
                            if (!q.Contains(n.Key)){
                                q.Enqueue(n.Key);
                            }          
                        }
                        else{
                            if (vek[n.Key] > n.Value + vek[q.Peek()]){
                                vek[n.Key] = n.Value + vek[q.Peek()];
                                slow[n.Key] = n.Key;
                            }
                        }
                    }
                    q.Dequeue();
                }
            }
        	string res = end;
            string now = end;
            while (now != start){
                res += " - " + slow[now];
                now = slow[now];
            }
            char[] arr = res.ToCharArray();
            Array.Reverse(arr);
            string path = new string (arr);
            return("The shortest path " + start + " в " + end + ": " + "(" + path + ")" + " is equal " + vek[end].ToString() + "\n");
        } 
		
		/// <summary>
		/// Graph output to console
		/// </summary>
		/// <returns>String with graph</returns>
		public string PrintGraph(){
			return(gr.ToString());
		}
	}
	
	/// <summary>
	/// Algorithm for traversing a chess field with a knight
	/// </summary>
	public class Knight{
		Graph Graph = new Graph();
		Dijkstra Dij;
		
		public Knight(){
			FillKnightGraph();
			Dij = new Dijkstra(Graph);
		}
		
		public string GetDis(string start, string end){
			return(Dij.GetDis(start, end));
		}
		
		/// <summary>
        /// adding a link between two vertices
        /// </summary>
        /// <param name="V1 - имя первой вершины"></param>
        /// <param name="V2 - имя второй вершины"></param>
        /// <param name="weigth - длина пути между врешинами V1 и V2"></param> 
        public void AddRel(string V1, string V2, int weigth)
        {
                Graph.AddVertex(V1);
                Graph.AddVertex(V2);
                Graph.AddEdge(V1, V2, weigth);
        }
		
        /// <summary>
		/// Creating a graph with all possible knight moves from each vertex
		/// </summary>
		public void FillKnightGraph()
        {
            string[] x = { "A", "B", "C", "D", "E", "F", "G", "H" };
            string[] y = { "1", "2", "3", "4", "5", "6", "7", "8" };
            for (int i = 0; i < 8; i++)
            {
                for (int j = 0; j < 8; j++)
                {
                    if ((i + 2 <= 7) && (j + 1 <= 7))
                    {
                        AddRel(x[i] + y[j], x[i + 2] + y[j + 1], 1); 
                    }
                    if ((i - 2 >= 0) && (j + 1 <= 7))
                    {
                        AddRel(x[i] + y[j], x[i - 2] + y[j + 1], 1);
                    }
                    if ((i + 1 <= 7) && (j + 2 <= 7))
                    {
                        AddRel(x[i] + y[j], x[i + 1] + y[j + 2], 1);
                    }
                    if ((i - 1 >= 0) && (j + 2 <= 7))
                    {
                        AddRel(x[i] + y[j], x[i - 1] + y[j + 2], 1);
                    }

                }
            }
        }
		
		/// <summary>
		/// Creating a string with a path to traverse the entire checkerboard
		/// </summary>
		/// <param name="start - starting cell"></param>
		/// <returns>String with a path to traverse the entire checkrboard</returns>
		public string Round(string start)
        {
            string res = start;
            for (int i = 0; i < 63; i++)
            {
                int count = 100;
                string str = "";
                foreach(var n in Graph.Verteces[start])
                {
                    if(Graph.Verteces[n.Key].Count < count)
                    {
                        count = Graph.Verteces[n.Key].Count;
                        str = n.Key;   
                    }
                }
                foreach (var v in Graph.Verteces) {
                    Graph.Verteces[v.Key].Remove(start);
                }
                Graph.Verteces.Remove(start);
                start = str;
                res += " " + str;
            }
            return (res);
        }
	}
	
	public class Test{
		public void TestAlgDijkstra(string start, string end){
			    Graph Graph = new Graph();
			    Graph.AddVertex("A"); 
             	Graph.AddVertex("B"); 
             	Graph.AddVertex("C");
             	Graph.AddVertex("D");
             	Graph.AddVertex("E");
             	Graph.AddVertex("F");
             	Graph.AddVertex("Z");
             	Graph.AddEdge("A", "B", 3, false);
             	Graph.AddEdge("A", "C", 4, false);
             	Graph.AddEdge("B", "E", 3, false);
             	Graph.AddEdge("B", "D", 4, false);
             	Graph.AddEdge("B", "F", 2, false);
             	Graph.AddEdge("C", "F", 5, false);
            	Graph.AddEdge("E", "Z", 1, false);
             	Graph.AddEdge("D", "Z", 4, false);
            	Graph.AddEdge("F", "Z", 3, false);
            	Dijkstra Dij = new Dijkstra(Graph);  
			    Console.WriteLine("Graph: \n"  + Dij.PrintGraph() + "\n" + Dij.GetDis(start, end));
		}
		
		public void TestKnight(string start1, string start, string end){
			Knight Knight = new Knight();
			Console.WriteLine("Knight test:\n" + Knight.GetDis(start, end));
			Console.WriteLine("Path " + start + ":\n" + Knight.Round(start));
		}
		
        public void TestAnnealign(int T, double w, Graph Graph, int itter){                
                Annealing A = new Annealing(Graph.Verteces, T, w, itter);
                Console.WriteLine("Graph:\n" + Graph);
        		Console.WriteLine("\n" + A.GetPath());
        }
		
		public void TestBrute(Graph Graph){
			 Console.WriteLine("Graph:\n" + Graph);
			 int l = Graph.Verteces.Count;
             int n = 0;
             int[] a = new int[l];
             BruteForceGraph Brute = new BruteForceGraph(Graph.Verteces);
             Brute.Method(a, n, l);
		}
	}
	
    public class Graph{
        public Dictionary<string, Dictionary<string, double>> Verteces;
        
        public Graph(){
            Verteces = new Dictionary<string, Dictionary<string, double>>();
        }   
		
        /// <summary>
		/// Add new vertex
		/// </summary>
		/// <param name="V - vertex name"></param>	   
        public void AddVertex(string V){
            if (!Verteces.ContainsKey(V))
                Verteces.Add(V, new Dictionary<string, double>());
        }
		
		/// <summary>
		/// Delete vertex
		/// </summary>
		/// <param name="V - vertex name"></param>       
		public void RemoveVertex(string V){
            if (Verteces.ContainsKey(V)){
                foreach (var v in Verteces)
                    if (Verteces[v.Key].ContainsKey(V))
                        RemoveEdge(v.Key, V);
                Verteces.Remove(V);
            }
        }
		
		/// <summary>
		/// Add new link
		/// </summary>
		/// <param name="V1 - first vertex name"></param>
		/// <param name="V2 - second vertex name"></param>
		/// <param name="weight - path length"></param>
		/// <param name="underected - if true,then two-way communication"></param>  
		public void AddEdge(string V1, string V2, double weight = 1, bool underected = true){
            if (Verteces.ContainsKey(V1) && Verteces.ContainsKey(V2))
                if (!Verteces[V1].ContainsKey(V2))
                    Verteces[V1].Add(V2, weight);
                else
                    Verteces[V1][V2] = weight;
            if (underected)
                AddEdge(V2, V1, weight, false);
        }
		
		/// <summary>
		/// Delete ling
		/// </summary>
		/// <param name="V1 - first vertex name"></param>
		/// <param name="V2 - second vertex name"></param>
		public void RemoveEdge(string V1, string V2){
            if (Verteces.ContainsKey(V1) && Verteces.ContainsKey(V2))
                if (Verteces[V1].ContainsKey(V2))
                    Verteces[V1].Remove(V2);
        }
		
		/// <summary>
		/// Get path length between two verteces
		/// </summary>
		/// <param name="V1 - first vertex name"></param>
		/// <param name="V2 - second vertex name"></param>
		/// <returns> Path length</returns>
		public double GetWeight(string V1, string V2){
            return (Verteces.ContainsKey(V1) && Verteces.ContainsKey(V2) ? Verteces[V1][V2] : Double.PositiveInfinity);
        }

		/// <summary>
		/// Get vertex neighbors
		/// </summary>
		/// <param name="V - vertex name"></param>
		/// <returns>String with neighbors list</returns>
		public string Nei(string V){
            string res = string.Empty;
            if (Verteces.ContainsKey(V)){
                foreach (var v in Verteces[V])
                    res += v.Key + " (" + v.Value + ")" + " ";
            }
            return (res);
        }
		 
		public override string ToString(){
            string res = string.Empty;
            foreach (var v in Verteces)
                res += v.Key + " : " + Nei(v.Key) + "\n";
            return (res);
        }
	}

    class Program{
    	static void Main(string[] args){
			Test Test = new Test();
			Console.ForegroundColor = ConsoleColor.Green; 
			Console.WriteLine("Dijkstra test");
			Console.ResetColor();
			Test.TestAlgDijkstra("A", "Z");
			Console.ForegroundColor = ConsoleColor.Green; 
			Console.WriteLine("Knight test");
			Console.ResetColor();
			Test.TestKnight("A", "A1", "H8"); 
			Console.WriteLine();
			Graph Graph = new Graph();
            Graph.AddVertex("A");
            Graph.AddVertex("B"); 
            Graph.AddVertex("C");
            Graph.AddVertex("D");
            Graph.AddEdge("A", "B", 5, true);
            Graph.AddEdge("A", "C", 7, true);
            Graph.AddEdge("A", "D", 8, true);
            Graph.AddEdge("B", "C", 9, true);
            Graph.AddEdge("B", "D", 6, true);
            Graph.AddEdge("C", "D", 7, true);
            Console.ForegroundColor = ConsoleColor.Green; 
			Console.WriteLine("Annealing algorithm test (Sometimes it doesn't work, you need to set it up better)");
			Console.ResetColor();
			Test.TestAnnealign(100, 0.9, Graph, 100);
			Console.WriteLine();
			Console.ForegroundColor = ConsoleColor.Green; 
			Console.WriteLine("Brutforse test");
			Console.ResetColor();
			Test.TestBrute(Graph); 
			Console.ReadKey();
    	 }
	}
}
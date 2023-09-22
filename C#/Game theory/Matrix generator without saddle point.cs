using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;

	
namespace Matrix_generator_without_saddle_point{
	class Program{
		
		public static int row_len = 0;
		public static int col_len = 0;
		public static int[,] matrix;
		public static Random rnd = new Random();
		public static bool res1 = false;
		public static bool res2 = false;
		
		public static void Main(string[] args){
			do{
				Console.Write("Enter the number of rows of the matrix (number from 0 to 10 000): ");
				if(int.TryParse(Console.ReadLine(), out row_len)){
					res1 = true;
				   }
			} while(row_len < 0 || row_len > 10000 || res1 != true);
			
			do{
				Console.Write("Enter the number of columns of the matrix (number from 0 to 10 000): ");
				if(int.TryParse(Console.ReadLine(), out col_len)){
					res2 = true;
				   }
			} while(col_len < 0 || col_len > 10000 || res2 != true);
			
			
			do{
				Fill_Matrix(row_len, col_len);
			} while(Min_Max(matrix) == Max_Min(matrix)); // so bad
			
			Console.WriteLine("\nThe following matrix was generated:");
			Console.WriteLine("\n" + Show_Matrix(matrix));
			
			Console.WriteLine("\nMax_Min = " + Max_Min(matrix).ToString());
			Console.WriteLine("Min_Max = " + Min_Max(matrix).ToString());
			
			Print_To_File(Show_Matrix(matrix));
			Console.WriteLine("\nThe matrix has been successfully saved to the program folder.");
			
			Console.Write("\nPress any key to exit. . . ");
			Console.ReadKey(true);
		}
		
		public static void Print_To_File(string text){
			string filename = row_len.ToString() + " " + col_len.ToString() + ".txt";
			string writepath = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, filename);
			try
            {
                using (StreamWriter sw = new StreamWriter(writepath, false, System.Text.Encoding.Default))
                {
                    sw.WriteLine(text);
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
		}
		
		public static string Show_Matrix(int [,] matrix){
			int row_len = matrix.GetLength(0);
			int col_len = matrix.GetLength(1);
			string str = "";
			for (int i = 0; i < row_len; i++){
	            for (int j = 0; j < col_len; j++){
					if(j != col_len - 1){
	                	str += string.Format("{0} ", matrix[i, j]);
					}
					else{
						str += string.Format("{0}", matrix[i, j]);
					}
				}
				if(i != row_len - 1){
	                str += Environment.NewLine;
				}         
	        }
			return(str);
		}
		
		public static void Fill_Matrix(int row_len, int col_len){
			matrix = new int[row_len, col_len];
			for(int i = 0; i < row_len; i++){
				for(int j = 0; j < col_len; j++){
					matrix[i, j] = rnd.Next(0, 20);
				}
			}
		}
		
		public static int Max_Min(int[,] matrix){
			List<int> lst = new List<int>();
			int[] temp = new int[col_len];
			for(int i = 0; i < row_len; i++){
				for(int j = 0; j < col_len; j++){
					temp[j] = matrix[i, j];
				}
				lst.Add(temp.Min());
			}
			return(lst.Max());
		}
		
		public static int Min_Max(int[,] matrix){
			List<int> lst = new List<int>();
			int[] temp = new int[row_len];
			for(int i = 0; i < col_len; i++){
				for(int j = 0; j < row_len; j++){
					temp[j] = matrix[j, i];
				}
				lst.Add(temp.Max());
			}
			return(lst.Min());
		}
	}
}
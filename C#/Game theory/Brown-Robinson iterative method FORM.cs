using System;
using System.IO;
using System.Linq;
using System.Data;
using System.Drawing;
using System.Windows.Forms;
using System.Collections.Generic;
using System.Windows.Forms.DataVisualization;

namespace Brown_Method
{
	public partial class MainForm : Form	{
		public double[,] matrix;
		public int matrixrow;
		public int matrixcolumn;
		public double[] first_loss;
		public int[] first_strat;
		public double[] for_first;
		public double[] p_first;
		public double[] second_loss;
		public int[] second_strat;
		public double[] for_second;
		public double[] p_second;
		
		public RichTextBox RichBox;
		public OpenFileDialog openFileDialog1;
		public Label stop_cond;
		public Label Label2;
		public Label Label3;
		public Label Label4;
		public TextBox Stop_Itteration;
		public TextBox Stop_Accuracy;
		public Button Open_File;
		public Button Start_itter;
		public Button Start_accu;
		public SaveFileDialog saveFileDialog1;
		public CheckBox checkbox1;
		public CheckBox checkbox2;
		
		public MainForm(){
			InitializeComponent();
			int left1 = 15;
			int down1 = 15;

			Open_File = new Button();
			Open_File.Text = "Load matrix";
			Open_File.Location = new Point(left1, down1);
			Open_File.Size = new Size(350, 25);
			Open_File.Font = new Font("Times New Roman", 10);
			Open_File.Click += new EventHandler(Open_File_Click);
			this.Controls.Add(Open_File);
			
   			int down2 = 50;
   			stop_cond = new Label();
   			stop_cond.Text = "Enter the condition for stopping the algorithm:";
   			stop_cond.Location = new Point(left1, down2);
   			stop_cond.Font = new Font("Times New Roman", 10);
   			stop_cond.Size = new Size(300, 20);
   			this.Controls.Add(stop_cond);
 
   			int down3 = 80;
   			Label3 = new Label();
   			Label3.Text = "Number of iterations:";
   			Label3.Location = new Point(left1, down3);
   			Label3.Font = new Font("Times New Roman", 10);
   			Label3.Size = new Size(150, 20);
   			this.Controls.Add(Label3);
   			
   			int left2 = 165;
   			Stop_Itteration = new TextBox();
   			Stop_Itteration.Text = "0";
   			Stop_Itteration.Location = new Point(left2, down3);
   			Stop_Itteration.Font = new Font("Times New Roman", 10);
   			Stop_Itteration.Size = new Size(50, 20);
   			this.Controls.Add(Stop_Itteration);
   			int left3 = 265;
   			Start_itter = new Button();
			Start_itter.Text = "Calculate";
			Start_itter.Location = new Point(left3, down3);
			Start_itter.Size = new Size(100, 25);
			Start_itter.Font = new Font("Times New Roman", 10);
			Start_itter.Click += new EventHandler(Start_itter_Click);
			this.Controls.Add(Start_itter);
   			
			int down4 = 120;
   			Label4 = new Label();
   			Label4.Text = "Accuracy:";
   			Label4.Location = new Point(left1, down4);
   			Label4.Font = new Font("Times New Roman", 10);
   			Label4.Size = new Size(150, 20);
   			this.Controls.Add(Label4);
   			
   			Stop_Accuracy= new TextBox();
   			Stop_Accuracy.Text = "0";
   			Stop_Accuracy.Location = new Point(left2, down4);
   			Stop_Accuracy.Font = new Font("Times New Roman", 10);
   			Stop_Accuracy.Size = new Size(50, 20);
   			this.Controls.Add(Stop_Accuracy);
   			
   			Start_accu = new Button();
			Start_accu.Text = "Calculate";
			Start_accu.Location = new Point(left3, down4);
			Start_accu.Size = new Size(100, 25);
			Start_accu.Font = new Font("Times New Roman", 10);
			Start_accu.Click += new EventHandler(Start_accu_Click);
			this.Controls.Add(Start_accu);
   			
			int down5 = 150;
			checkbox1 = new CheckBox();  
			checkbox1.Text = "Save iterations to file";  
			checkbox1.Location = new Point(left1, down5);
			checkbox1.Size = new Size(200, 20);
			checkbox1.Font = new Font("Times New Roman", 10); 
			this.Controls.Add(checkbox1);
			
			int down6 = 180;
			checkbox2 = new CheckBox();  
			checkbox2.Text = "Save final results to file";  
			checkbox2.Location = new Point(left1, down6);
			checkbox2.Size = new Size(300, 20);
			checkbox2.Font = new Font("Times New Roman", 10); 
			this.Controls.Add(checkbox2);
			
			int down7 = 210;
   			Label2 = new Label();
   			Label2.Text = "The result of the program:";
   			Label2.Location = new Point(left1, down7);
   			Label2.Font = new Font("Times New Roman", 10);
   			Label2.Size = new Size(200, 20);
   			this.Controls.Add(Label2);
   			
   			int down8 = 230;
			RichBox = new RichTextBox();
			RichBox.Location = new Point(left1, down8);  
			RichBox.Width = 360;  
			RichBox.Height = 150;  
			RichBox.BackColor = Color.White;  
			RichBox.ForeColor = Color.Black;  
			RichBox.Name = "RichBox";  
			RichBox.Font = new Font("Times New Roman", 10);  
			Controls.Add(RichBox);   
			
			openFileDialog1 = new OpenFileDialog(); 
			openFileDialog1.InitialDirectory = AppDomain.CurrentDomain.BaseDirectory;
			openFileDialog1.RestoreDirectory = true;  
			openFileDialog1.Title = "Open .txt";
			openFileDialog1.DefaultExt = "txt";
			openFileDialog1.Filter = "txt files (*.txt)|*.txt|All files (*.*)|*.*";
			openFileDialog1.CheckFileExists = true;
			openFileDialog1.CheckPathExists = true;
			
			saveFileDialog1 = new SaveFileDialog();
			saveFileDialog1.InitialDirectory = AppDomain.CurrentDomain.BaseDirectory;  
			saveFileDialog1.RestoreDirectory = true;
			saveFileDialog1.Title = "Save .txt";
			saveFileDialog1.DefaultExt = "txt";
			saveFileDialog1.Filter = "txt files (*.txt)|*.txt|All files (*.*)|*.*";
			saveFileDialog1.CheckPathExists = true;			
		}
		
		void Open_File_Click(object sender, EventArgs e){
			Init();
		}
		
		void Start_itter_Click(object sender, EventArgs e){
			RichBox.Text = "";
			BROWN(0, 10, Convert.ToInt32(Stop_Itteration.Text));
			}
		
		void Start_accu_Click(object sender, EventArgs e){
			RichBox.Text = "";
			BROWN(10, Convert.ToDouble(Stop_Accuracy.Text), 0);
		}
		
		void Print_To_File(string text, string filename){
			string writepath = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, filename);
			try
            {
                using (StreamWriter sw = new StreamWriter(writepath, true, System.Text.Encoding.UTF8))
                {
                    sw.WriteLine(text);
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
		}
		
		void Init(){
			if (openFileDialog1.ShowDialog() == DialogResult.Cancel)
            	return;
	        string filename = openFileDialog1.FileName;
	        string[] readtext = File.ReadAllLines(filename);
	        matrixrow = readtext.Length;
	        matrixcolumn = readtext[0].Split(' ').Length;
	        matrix = new double[matrixrow, matrixcolumn];
	        first_loss = new double[matrixcolumn];
	        for_first = new double[matrixcolumn];
	        first_strat = new int[matrixrow];
	        p_first = new double[matrixrow];
	        second_loss = new double[matrixrow];
	        for_second = new double[matrixrow];
	        second_strat = new int[matrixcolumn];
	        p_second = new double[matrixcolumn];
	        for(int i = 0; i < matrixrow; i++){
	        	for(int j = 0; j < matrixcolumn; j++){
	        		matrix[i,j] = System.Convert.ToDouble(readtext[i].Split(' ')[j]);
	        	}
	        }
	        MessageBox.Show("Matrix loaded successfully.");
		}
		
		void BROWN(double accuracy, double stop_accuracy, int stop_itteration){
			first_strat = new int[matrixrow];
			second_strat = new int[matrixcolumn];
			int itterations = 1;
			double v_min = 0;
	        double v_max = 0;
	        double v_mean = 0;
			for(int i = 0; i < matrixcolumn; i++){
	        	first_loss[i] = matrix[0, i];
	        }
			first_strat[0] = 1;
	        for(int i = 0; i < matrixrow; i++){
	        	second_loss[i] = matrix[i, 1];
	        }
			second_strat[0] = 1;
			if(checkbox1.Checked){
				Print_To_File(String.Format("{0, 4}{1, 2}{2, 15}{3, 4}{4, 15}{5, 5}{6, 5}{7, 5}", 
	        	                                	0, 1, string.Join(" ", first_loss), 1, 
	        	                                	string.Join(" ", second_loss), 0, 0, 0), "iteration.txt");
			}
			while(accuracy > stop_accuracy || stop_itteration > 0){
				double first_max = second_loss.ToList().Max();
		        int first_max_index = Array.IndexOf(second_loss, first_max);
	        	first_strat[first_max_index] += 1;
	        	for(int j = 0; j < matrixcolumn; j++){
	        		for_first[j] = matrix[first_max_index, j];
	        	}
	        	first_loss = first_loss.Select ((x, index) => x + for_first[index]).ToArray();
	        	double second_min = first_loss.ToList().Min();
	        	int second_min_index = Array.IndexOf(first_loss, second_min);
	        	second_strat[second_min_index] += 1;
	        	for(int j = 0; j < matrixrow; j++){
	        		for_second[j] = matrix[j, second_min_index];
	        	}
	        	second_loss = second_loss.Select ((x, index) => x + for_second[index]).ToArray();
	        	if(itterations > 0){
		        	v_min = (double)first_loss.Min() / (double)itterations;
		       		v_max = (double)second_loss.Max() / (double)itterations;
		        	v_mean = (double)(v_min + v_max) / (double)2;
	        		accuracy = v_max - v_min;
	        	}
	        	if(checkbox1.Checked){
	        		Print_To_File(String.Format("{0, 4}{1, 2}{2, 15}{3, 4}{4, 15}{5, 5:0.0}{6, 5:0.0}{7, 5:0.0}", 
	        	                              	  itterations, first_max_index + 1, string.Join(" ", first_loss), second_min_index + 1, 
	        	                              	  string.Join(" ", second_loss), v_min, v_mean, v_max), "iteration.txt");
	        	}
	        	itterations += 1;
	        	stop_itteration -= 1;
			}
			string res = "";
			string ps_first = "";
			for(int i = 0; i < matrixrow; i++){
				p_first[i] = (double)first_strat[i] / (double)itterations;
				ps_first += String.Format(" {0:0.00}", p_first[i]);
			}
			res += "Probabilities of choosing strategies for the first player:\n";
			res += ps_first + "\n";
			string ps_second = "";
			for(int i = 0; i < matrixcolumn; i++){
				p_second[i] = (double)second_strat[i] / (double)itterations;
				ps_second += String.Format(" {0:0.00}", p_second[i]);
			}
			res += "Probabilities of choosing strategies for the second player:\n";
			res += ps_second + "\n";
			res += "The lower limit of the game: ";
			res += String.Format("{0:0.00}\n", v_min);
			res += "The upper limit of the game: ";
			res += String.Format("{0:0.00}\n", v_max);
			res += "Difference between upper and lower game limits: ";
			res += String.Format("{0:0.00}", v_max - v_min);
			RichBox.Text = res;
			if(checkbox2.Checked){
				Print_To_File(res, "results.txt");
			}
			MessageBox.Show("Calculations completed successfully.");
		}
	}
}